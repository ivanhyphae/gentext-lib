"""T3 extract (DR-0011): held sections → candidate library chunks, verbatim by construction.

For each section a card marked reuse_value high/medium in a `hold` document, Haiku reads the
full section and proposes chunks as *anchors* (first and last words), not text. Code slices the
exact source text between the anchors, so a candidate can never contain paraphrased or invented
prose. Facts are kept only if their supporting quote occurs verbatim in the chunk.

Sections whose text is ≥90% contained in a section already extracted from another held document
are skipped (the two ARPD pre-applications share ~97% of their text).

Output: library/_candidates/<asset-id>/<sid>-<n>-<slug>.md (frontmatter + verbatim body).
Candidates are NOT library chunks; promotion (T4) is a human/Opus step.
"""

from __future__ import annotations

import datetime as dt
import json
import re
import time
from pathlib import Path
from typing import Literal

import yaml
from pydantic import BaseModel, ConfigDict

from gentext import inventory as inv
from gentext.card import CARD_DIR, PRICES, _M as _Strict
from gentext.extract import redact
from gentext.profile import asset_text, shingles

CAND_DIR = Path("library/_candidates")
RUN_LOG = Path("library/_candidates/extract-runs.yaml")
# Sonnet 5 beat Haiku 4.5 on extraction in a 2026-09-25 test (finer chunks, more quoted facts, 3% vs ~11%
# anchor misses) at ~20x cost, still ~$1.5–3 per batch of ~45 sections. Haiku stays the card (T2) model.
MODEL = "claude-sonnet-5"
PROMPT_VERSION = "x1"
MAX_TOKENS = 16000  # Sonnet thinks adaptively; thinking counts toward max_tokens
MIN_CHUNK_WORDS = 25
MAX_SECTION_WORDS = 3500
SKIP_TYPES = {"solicitation-text", "admin", "notes"}
DUP_CONTAINMENT = 0.9
LONG_FORM_WORDS = 1000

ChunkType = Literal[
    "project-case", "capability", "network", "site-context", "need-statement", "method",
    "partner-role", "org-profile", "template", "boilerplate", "other",
]


class Fact(_Strict):
    claim: str
    quote: str


class ChunkProposal(_Strict):
    title: str
    type: ChunkType
    summary: str
    start_anchor: str
    end_anchor: str
    places: list[str]
    orgs: list[str]
    projects: list[str]
    facts: list[Fact]
    leakage: list[str]
    authorship: str
    quality_notes: str


class Extraction(_Strict):
    chunks: list[ChunkProposal]


def _schema() -> dict:
    def fix(node):
        if isinstance(node, dict):
            if node.get("type") == "object":
                node["additionalProperties"] = False
                node["required"] = list(node.get("properties", {}))
            if isinstance(node.get("title"), str):  # drop schema annotations, never a property named "title"
                node.pop("title")
            for v in node.values():
                fix(v)
        elif isinstance(node, list):
            for v in node:
                fix(v)
        return node

    return fix(Extraction.model_json_schema())


SYSTEM = """You split one section of a source document into reusable proposal-library chunks for Hyphae Design Lab,
a small urban-climate design and data firm that writes grant proposals with public agencies and community partners.

A chunk is a self-contained passage that could be reused (adapted) in a future proposal: a project case with outcomes,
a capability or method description, a site description, a need statement with data, a partner role or org profile,
an outreach template, or firm boilerplate. Skip meeting notes, action items, links lists, and solicitation text.

For each chunk give ANCHORS, not text:
- start_anchor: the exact first 6–12 words of the chunk, copied character-for-character from the section.
- end_anchor: the exact last 6–12 words of the chunk, copied character-for-character.
Code will cut the chunk out of the source between the anchors, so they must match exactly and appear in order.
Chunks must not overlap. It is fine to return zero chunks.

Also, per chunk:
- facts: specific checkable claims (numbers, dates, dollar amounts, named outcomes). `quote` must be an exact
  substring of the chunk that supports the claim. Never infer or invent.
- leakage: place, organization, or program names in the chunk that look like leftovers from a different client or
  project than the document's own context (e.g. "Fresno County" inside a Bay Point application). Empty if none.
- places / orgs / projects: names mentioned, as written.
- authorship: who appears to have written this passage (Hyphae, a named partner, an agency, unknown).
- quality_notes: one line on reuse readiness (e.g. "generic, needs site specifics", "unhedged boosters", "strong").
Contact details have been redacted to [email]/[phone].
"""


_MARKUP = re.compile(r"(\*\*|__|`|\u200b|\u200c|\ufeff)|^\s*(?:[-*+]|\d+[.)])\s+", re.M)


def _norm(s: str) -> str:
    """Whitespace- and markup-insensitive form used for anchor and quote matching (bold/italic markers,
    list bullets, zero-width characters are ignored). Candidate text is sliced from this form."""
    s = _MARKUP.sub("", s)
    s = s.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')
    return re.sub(r"\s+", " ", s).strip()


def slice_by_anchors(text: str, start: str, end: str) -> str | None:
    """Return the exact span from start anchor through end anchor (whitespace-normalized match)."""
    t = _norm(text)
    s, e = _norm(start), _norm(end)
    i = t.find(s)
    if i == -1 or not e:
        return None
    j = t.find(e, i)
    if j == -1:
        return None
    return t[i : j + len(e)]


def plan(asset_ids: list[str] | None = None) -> tuple[list[dict], list[dict]]:
    """Choose sections to extract; returns (todo, skipped)."""
    assets = {a.id: a for a in inv.load().assets if a.local}
    held = []
    for f in sorted(CARD_DIR.glob("*.yaml")):
        d = yaml.safe_load(f.read_text())
        if d["card"]["disposition"] == "hold" and d["asset_id"] in assets:
            if not asset_ids or d["asset_id"] in asset_ids:
                held.append(d)
    # Process larger/primary docs first so their shared text claims the dedup slot.
    held.sort(key=lambda d: (-(assets[d["asset_id"]].priority == 1), d["asset_id"]))
    seen: list[tuple[str, str, set[int]]] = []
    todo, skipped = [], []
    for d in held:
        a = assets[d["asset_id"]]
        _, sections = asset_text(a)
        for sc in d["card"]["sections"]:
            sid = sc.get("sid")
            if not sid:
                skipped.append({"asset": a.id, "sid": sid, "why": "no sid (old card)"})
                continue
            idx = int(sid[1:]) - 1
            if not 0 <= idx < len(sections):
                skipped.append({"asset": a.id, "sid": sid, "why": "sid out of range"})
                continue
            # Cards judge from section openings; a long "solicitation-text" section in a held working doc is usually
            # form questions followed by our answers (e.g. a pre-application tab), so extract it anyway.
            long_form = sc["type"] == "solicitation-text" and sections[idx].words >= LONG_FORM_WORDS
            if sc["type"] in SKIP_TYPES and not long_form:
                skipped.append({"asset": a.id, "sid": sid, "why": f"type {sc['type']}"})
                continue
            body = "\n".join(sections[idx].lines)
            words = body.split()
            if len(words) < 40:
                skipped.append({"asset": a.id, "sid": sid, "why": "under 40 words"})
                continue
            sh = shingles(body)
            dup = next((f"{oa}/{os}" for oa, os, osh in seen if sh and len(sh & osh) / len(sh) >= DUP_CONTAINMENT), None)
            if dup:
                skipped.append({"asset": a.id, "sid": sid, "why": f"duplicate of {dup}"})
                continue
            seen.append((a.id, sid, sh))
            if len(words) > MAX_SECTION_WORDS:
                body = " ".join(words[:MAX_SECTION_WORDS])
            todo.append({"asset": a, "sid": sid, "path": sections[idx].path, "type_hint": sc["type"],
                         "body": body, "source_sha": a.local.sha256})
    return todo, skipped


def _user(item: dict) -> str:
    a = item["asset"]
    return (f"DOCUMENT: {a.title} (asset {a.id}; places: {', '.join(a.relevance.places) or 'n/a'})\n"
            f"SECTION [{item['sid']}] {item['path']} (card type guess: {item['type_hint']})\n\n"
            f"{redact(item['body'])}")


def _params(item: dict) -> dict:
    return {
        "model": MODEL, "max_tokens": MAX_TOKENS,
        "system": [{"type": "text", "text": SYSTEM, "cache_control": {"type": "ephemeral"}}],
        "messages": [{"role": "user", "content": _user(item)}],
        "output_config": {"format": {"type": "json_schema", "schema": _schema()}},
    }


def _slug(s: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")[:48] or "chunk"


def write_candidates(item: dict, ext: Extraction, usage: dict) -> tuple[int, list[str]]:
    a, sid = item["asset"], item["sid"]
    out_dir = CAND_DIR / a.id
    out_dir.mkdir(parents=True, exist_ok=True)
    for old in out_dir.glob(f"{sid}-*.md"):
        old.unlink()
    source_text = redact(item["body"])
    written, problems = 0, []
    for n, ch in enumerate(ext.chunks, 1):
        text = slice_by_anchors(source_text, ch.start_anchor, ch.end_anchor)
        if not text:
            problems.append(f"{sid}#{n} anchors not found: {ch.title}")
            continue
        if len(text.split()) < MIN_CHUNK_WORDS:
            problems.append(f"{sid}#{n} under {MIN_CHUNK_WORDS} words: {ch.title}")
            continue
        facts = [f.model_dump() for f in ch.facts if _norm(f.quote) and _norm(f.quote) in text]
        dropped = len(ch.facts) - len(facts)
        fm = {
            "id": f"cand-{a.id}-{sid}-{n}",
            "status": "candidate",
            "title": ch.title,
            "type": ch.type,
            "summary": ch.summary,
            "words": len(text.split()),
            "places": ch.places, "orgs": ch.orgs, "projects": ch.projects,
            "facts": facts,
            "flags": ([f"context leakage: {x}" for x in ch.leakage] + ([f"{dropped} fact(s) dropped: quote not verbatim"] if dropped else [])),
            "quality_notes": ch.quality_notes,
            "provenance": {
                "origin": "extracted",
                "source": {"asset": a.id, "sha256": item["source_sha"], "section": sid, "path": item["path"]},
                "authors": [{"kind": "unknown", "id": ch.authorship or "unknown", "role": "wrote", "verified": False}],
                "extracted_by": {"model": MODEL, "prompt": PROMPT_VERSION, "date": dt.date.today().isoformat()},
                "verbatim": True,
            },
        }
        body = yaml.safe_dump(fm, sort_keys=False, allow_unicode=True, width=120)
        (out_dir / f"{sid}-{n}-{_slug(ch.title)}.md").write_text(f"---\n{body}---\n\n{text}\n")
        written += 1
    return written, problems


def item_for(asset_id: str, sid: str) -> dict:
    a = next(x for x in inv.load().assets if x.id == asset_id)
    _, sections = asset_text(a)
    sec = sections[int(sid[1:]) - 1]
    body = " ".join(" ".join(sec.lines).split()[:MAX_SECTION_WORDS]) if sec.words > MAX_SECTION_WORDS else "\n".join(sec.lines)
    return {"asset": a, "sid": sid, "path": sec.path, "type_hint": "", "body": body, "source_sha": a.local.sha256}


PROMPT_DIR = Path("build/extract-prompts")


def prepare(asset_ids: list[str] | None = None) -> int:
    """Sub-agent backend: one self-contained prompt file per section. A sub-agent must write the JSON object it
    produces (matching `schema`) to build/extract-raw/<run>/<asset>__<sid>.json; then run `gentext extract --revalidate`."""
    todo, _ = plan(asset_ids)
    PROMPT_DIR.mkdir(parents=True, exist_ok=True)
    for it in todo:
        key = f"{it['asset'].id}__{it['sid']}"
        (PROMPT_DIR / f"{key}.json").write_text(json.dumps(
            {"key": key, "system": SYSTEM, "user": _user(it), "schema": _schema()}, ensure_ascii=False))
    return len(todo)


def revalidate(raw_dir: Path) -> dict:
    """Re-run validation/slicing on saved raw outputs (no API calls)."""
    written, problems, errors = 0, [], {}
    for f in sorted(raw_dir.glob("*.json")):
        asset_id, sid = f.stem.split("__")
        try:
            ext = Extraction.model_validate_json(f.read_text())
        except ValueError as e:
            errors[f.stem] = str(e)[:300]
            continue
        n, p = write_candidates(item_for(asset_id, sid), ext, {})
        written += n
        problems += p
    return {"raw_dir": str(raw_dir), "candidates": written, "anchor_problems": problems, "errors": errors}


def run(asset_ids: list[str] | None = None, batch: bool = True, poll: int = 30) -> dict:
    import anthropic
    from anthropic.types.message_create_params import MessageCreateParamsNonStreaming
    from anthropic.types.messages.batch_create_params import Request

    todo, skipped = plan(asset_ids)
    if not todo:
        return {"sections": 0, "skipped": skipped}
    client = anthropic.Anthropic()
    key = {f"{it['asset'].id}__{it['sid']}": it for it in todo}
    raw, errors = {}, {}
    if batch:
        b = client.messages.batches.create(requests=[
            Request(custom_id=k, params=MessageCreateParamsNonStreaming(**_params(it))) for k, it in key.items()])
        print(f"batch {b.id}: {len(key)} sections", flush=True)
        while (b := client.messages.batches.retrieve(b.id)).processing_status != "ended":
            print(f"  {b.request_counts.processing} processing, {b.request_counts.succeeded} done", flush=True)
            time.sleep(poll)
        for r in client.messages.batches.results(b.id):
            if r.result.type != "succeeded":
                errors[r.custom_id] = r.result.type
                continue
            m = r.result.message
            if m.stop_reason in ("refusal", "max_tokens"):
                errors[r.custom_id] = f"stop_reason={m.stop_reason}"
                continue
            raw[r.custom_id] = (next(c.text for c in m.content if c.type == "text"), m.usage)
        run_id = b.id
    else:
        for k, it in key.items():
            m = client.messages.create(**_params(it))
            if m.stop_reason in ("refusal", "max_tokens"):
                errors[k] = f"stop_reason={m.stop_reason}"
                continue
            raw[k] = (next(c.text for c in m.content if c.type == "text"), m.usage)
        run_id = dt.datetime.now().strftime("sync-%Y%m%dT%H%M%S")
    written, problems, tin, tout = 0, [], 0, 0
    raw_dir = Path("build/extract-raw") / run_id
    raw_dir.mkdir(parents=True, exist_ok=True)
    for k, (text, u) in raw.items():
        (raw_dir / f"{k}.json").write_text(text)  # keep raw output: re-validate without paying again
        tin += u.input_tokens + (u.cache_read_input_tokens or 0) + (u.cache_creation_input_tokens or 0)
        tout += u.output_tokens
        try:
            ext = Extraction.model_validate_json(text)
        except ValueError as e:
            errors[k] = f"invalid: {str(e)[:300]}"
            continue
        n, p = write_candidates(key[k], ext, {})
        written += n
        problems += p
    entry = {"run": run_id, "date": dt.date.today().isoformat(), "model": MODEL, "prompt_version": PROMPT_VERSION,
             "sections": len(key), "candidates": written, "anchor_problems": problems, "errors": errors,
             "skipped": len(skipped), "input_tokens": tin, "output_tokens": tout,
             "est_cost_usd": round((tin * PRICES[MODEL][0] + tout * PRICES[MODEL][1]) / 1e6 * (0.5 if batch else 1), 4)}
    CAND_DIR.mkdir(parents=True, exist_ok=True)
    runs = (yaml.safe_load(RUN_LOG.read_text()) if RUN_LOG.exists() else None) or []
    RUN_LOG.write_text(yaml.safe_dump(runs + [entry], sort_keys=False, width=120))
    (CAND_DIR / "skipped.yaml").write_text(yaml.safe_dump(skipped, sort_keys=False, width=120))
    return entry
