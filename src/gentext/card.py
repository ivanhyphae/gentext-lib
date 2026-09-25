"""T2 cards (DR-0011): one bounded Haiku call per document → disposition + reusable sections.

Prompt building and output validation live here and are deterministic. Execution is a
pluggable backend:
  - api-batch / api-sync : Anthropic API (key from .env locally; Secret Manager on Cloud Run)
  - subagent             : `prepare` writes prompt files; Claude Code Haiku sub-agents return JSON;
                           `ingest` validates and saves (no API key needed)
"""

from __future__ import annotations

import datetime as dt
import hashlib
import json
import time
from pathlib import Path
from typing import Literal

import yaml
from pydantic import BaseModel, ConfigDict

from gentext import inventory as inv
from gentext.extract import redact
from gentext.profile import asset_text, load_profile

CARD_DIR = Path("inventory/cards")
PROMPT_DIR = Path("build/card-prompts")
RUN_LOG = Path("inventory/card-runs.yaml")
MODEL = "claude-haiku-4-5"
PROMPT_VERSION = "c3"
HEAD_WORDS = 120
MAX_HEAD_WORDS_TOTAL = 5000
MAX_TOKENS = 4000
# List price per MTok (claude-api skill, cached 2026-06-24); Batch API is 50% off.
PRICES = {"claude-haiku-4-5": (1.00, 5.00), "claude-sonnet-5": (2.00, 10.00), "claude-opus-5": (5.00, 25.00)}
PRICE_IN, PRICE_OUT = PRICES[MODEL]


def use_model(model: str, out_dir: Path | None = None) -> None:
    """Switch model (and optionally output dir, for side-by-side tests). Sonnet/Opus think adaptively, so allow more tokens."""
    global MODEL, PRICE_IN, PRICE_OUT, MAX_TOKENS, CARD_DIR, RUN_LOG
    MODEL = model
    PRICE_IN, PRICE_OUT = PRICES[model]
    MAX_TOKENS = 4000 if "haiku" in model else 16000
    if out_dir:
        CARD_DIR, RUN_LOG = out_dir, out_dir / "card-runs.yaml"

Disposition = Literal["hold", "reference", "ignore", "drop"]
SectionType = Literal[
    "project-case", "capability", "network", "site-context", "need-statement", "method", "partner-role",
    "org-profile", "template", "boilerplate", "solicitation-text", "evidence-data", "admin", "notes", "other",
]
Reuse = Literal["high", "medium", "low"]


class _M(BaseModel):
    model_config = ConfigDict(extra="forbid")


class NeedHit(_M):
    need_id: str
    how: str


class SectionCard(_M):
    sid: str
    path: str
    type: SectionType
    reuse_value: Reuse
    note: str


class Card(_M):
    summary: str
    doc_role: Literal[
        "solicitation", "submitted-proposal", "proposal-draft", "working-doc", "guidance", "report",
        "dataset", "presentation", "notes", "template", "other",
    ]
    authorship: str
    disposition: Disposition
    disposition_reason: str
    serves_needs: list[NeedHit]
    sections: list[SectionCard]
    fact_candidates: list[str]
    flags: list[str]


def _schema() -> dict:
    """JSON schema for structured outputs (every object: additionalProperties false, all fields required)."""
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

    return fix(Card.model_json_schema())


# ─── needs list (DR-0011 "pull" relevance) ───────────────────────────────────────────

def needs_text(solicitation_dir: Path = Path("solicitations/lci/ehcrp/round-2")) -> str:
    qs = yaml.safe_load((solicitation_dir / "questions.yaml").read_text())
    apps = [yaml.safe_load(p.read_text()) for p in sorted((solicitation_dir / "applications").glob("*.yaml"))]
    wanted = [a for a in inv.load().assets if a.status == "wanted"]
    lines = ["ACTIVE SOLICITATION: LCI EHCRP Round 2 (Early Infrastructure). Full application due 2026-10-13.", "",
             "Questions (need_id — section, limit — what a strong answer must show):"]
    for q in qs:
        lines.append(f"- {q['id']} — {q['section']}, {q['word_limit']} words — {'; '.join(q['evidence'])}")
    lines += ["", "Applications (site x partner permutations):"]
    for a in apps:
        lines.append(f"- {a['id']}: {a['site']}; lead {a['lead_applicant']}; status {a['status']}")
    lines += ["", "Wanted assets / evidence gaps (need_id — description):"]
    for w in wanted:
        lines.append(f"- {w.id} — {w.title}")
    lines += ["", "Library needs (need_id): lib-firm-experience (Hyphae project cases with citable outcomes), "
              "lib-methods (heat/UTCI modeling, monitoring, engagement, stewardship), lib-site-bay-point "
              "(Bay Point / Ambrose site facts), lib-partners (partner org profiles and track records), "
              "lib-glossary (canonical terms and acronyms)."]
    return "\n".join(lines)


SYSTEM_TEMPLATE = """You triage source documents for Hyphae Design Lab's proposal-writing library.
Hyphae is a small urban-climate design and data firm that writes grant proposals with public agencies and community partners.
Your job is to decide how much attention each document deserves, so that expensive reading is spent only where it pays off.

You will see a document's metadata, its outline (section paths with word counts), and the first ~{head} words of each
section. You never see the whole document. Judge from that evidence and say so when it is thin.
The metadata's inventory_note is a human's prior guess about why the document matters: use it to understand relevance,
but take the summary and every fact from the document excerpts only. If the excerpts contradict the note, say so in flags.

Dispositions:
- hold: contains reusable proposal prose or citable facts worth extracting into library chunks (submitted proposals,
  project deliverables with outcomes, current capability or method text, site descriptions, strong need statements).
- reference: authoritative but not prose to reuse (solicitations, guidelines, TA guides, cited reports, datasets).
  Keep the file; look things up in it when a question needs it.
- ignore: summarize and move on (administrative, superseded drafts, low-value notes, near-duplicates of held docs).
- drop: not relevant to Hyphae proposals at all; safe to delete the file.

Section types: project-case, capability, network, site-context, need-statement, method, partner-role, org-profile,
template, boilerplate, solicitation-text, evidence-data, admin, notes, other.

Rules:
- List in `sections` only sections with reuse_value high or medium. Identify each by its section id (`sid`, e.g. "s12",
  shown in square brackets before the path) and copy its path. Omit the rest.
- Match wanted-asset need ids only when this document IS or directly CONTAINS that asset, not when it is merely related.
- `serves_needs` uses need_id values from the needs list below; include only real matches, with a one-line why.
- `fact_candidates`: at most 12 short, specific, checkable claims visible in the excerpts (numbers, dates, dollar
  amounts, named outcomes), each prefixed with its section path. Copy facts; never infer or invent them.
- `authorship`: who appears to have written it (org or role), or "unknown".
- `flags` (free text, short): e.g. "contains contact data", "context leakage risk: names <place> in reused text",
  "possibly outdated", "near-duplicate of <asset id>", "internal/candid notes", "excerpt too thin to judge".
- Contact details have been redacted to [email]/[phone].

NEEDS LIST
{needs}
"""


def build_user_message(asset: inv.Asset) -> tuple[str, str]:
    text, sections = asset_text(asset)
    prof = load_profile(asset.id) or {}
    dup = prof.get("near_duplicates", [])
    meta = {
        "asset_id": asset.id, "title": asset.title, "kind": asset.kind, "inventory_note": asset.relevance.note,
        "owner": asset.location.owner if asset.location else None,
        "modified": str(asset.location.modified) if asset.location and asset.location.modified else None,
        "total_words": len(text.split()), "sections": len(sections),
        "near_duplicates": [f"{d['asset_id']} ({int(d['contained_in'] * 100)}% of this doc)" for d in dup[:3]],
    }
    # Budget: heads for the largest sections first, name-only for the rest.
    order = sorted(range(len(sections)), key=lambda i: -sections[i].words)
    budget, with_head = MAX_HEAD_WORDS_TOTAL, set()
    for i in order:
        if sections[i].words and budget > 0:
            with_head.add(i)
            budget -= min(HEAD_WORDS, sections[i].words)
    out = ["DOCUMENT METADATA", json.dumps(meta, ensure_ascii=False, indent=1), "", "OUTLINE AND SECTION OPENINGS"]
    for i, s in enumerate(sections):
        out.append(f"\n## [s{i + 1}] {s.path}  [{s.words} words]")
        if i in with_head:
            out.append(redact(s.head(HEAD_WORDS)) + (" …" if s.words > HEAD_WORDS else ""))
    msg = "\n".join(out)
    return msg, hashlib.sha256(text.encode()).hexdigest()


def _params(system: str, user: str) -> dict:
    return {
        "model": MODEL,
        "max_tokens": MAX_TOKENS,
        "system": [{"type": "text", "text": system, "cache_control": {"type": "ephemeral"}}],
        "messages": [{"role": "user", "content": user}],
        "output_config": {"format": {"type": "json_schema", "schema": _schema()}},
    }


def _is_current(asset_id: str, text_sha: str) -> bool:
    p = CARD_DIR / f"{asset_id}.yaml"
    if not p.exists():
        return False
    meta = (yaml.safe_load(p.read_text()) or {}).get("meta", {})
    return meta.get("text_sha256") == text_sha and meta.get("prompt_version") == PROMPT_VERSION


def save_card(asset_id: str, card: Card, text_sha: str, backend: str, usage: dict | None = None) -> None:
    CARD_DIR.mkdir(parents=True, exist_ok=True)
    doc = {
        "asset_id": asset_id,
        "card": card.model_dump(),
        "meta": {"model": MODEL, "prompt_version": PROMPT_VERSION, "backend": backend, "text_sha256": text_sha,
                 "created": dt.datetime.now().isoformat(timespec="seconds"), "usage": usage or {}},
    }
    (CARD_DIR / f"{asset_id}.yaml").write_text(yaml.safe_dump(doc, sort_keys=False, allow_unicode=True, width=120))


def plan(assets: list[inv.Asset], force: bool = False) -> tuple[str, list[tuple[inv.Asset, str, str]]]:
    system = SYSTEM_TEMPLATE.format(head=HEAD_WORDS, needs=needs_text())
    todo = []
    for a in assets:
        user, sha = build_user_message(a)
        if force or not _is_current(a.id, sha):
            todo.append((a, user, sha))
    return system, todo


def _log_run(entry: dict) -> None:
    runs = yaml.safe_load(RUN_LOG.read_text()) if RUN_LOG.exists() else []
    runs = (runs or []) + [entry]
    RUN_LOG.write_text(yaml.safe_dump(runs, sort_keys=False, width=120))


def _usage(u) -> dict:
    return {"input": u.input_tokens, "output": u.output_tokens,
            "cache_read": getattr(u, "cache_read_input_tokens", 0) or 0,
            "cache_write": getattr(u, "cache_creation_input_tokens", 0) or 0}


def _cost(usages: list[dict], batch: bool) -> float:
    tin = sum(u["input"] + u["cache_write"] * 1.25 + u["cache_read"] * 0.1 for u in usages)
    tout = sum(u["output"] for u in usages)
    return round((tin * PRICE_IN + tout * PRICE_OUT) / 1e6 * (0.5 if batch else 1.0), 4)


def run_api(assets: list[inv.Asset], batch: bool = True, force: bool = False, poll: int = 30) -> dict:
    import anthropic
    from anthropic.types.message_create_params import MessageCreateParamsNonStreaming
    from anthropic.types.messages.batch_create_params import Request

    system, todo = plan(assets, force)
    if not todo:
        return {"cards": 0, "skipped": len(assets)}
    client = anthropic.Anthropic()
    by_id = {a.id: (a, sha) for a, _, sha in todo}
    raw: dict[str, tuple[str, dict]] = {}
    errors: dict[str, str] = {}
    if batch:
        b = client.messages.batches.create(requests=[
            Request(custom_id=a.id, params=MessageCreateParamsNonStreaming(**_params(system, user)))
            for a, user, _ in todo
        ])
        print(f"batch {b.id}: {len(todo)} requests")
        while (b := client.messages.batches.retrieve(b.id)).processing_status != "ended":
            print(f"  {b.processing_status}: {b.request_counts.processing} processing, {b.request_counts.succeeded} done")
            time.sleep(poll)
        for r in client.messages.batches.results(b.id):
            if r.result.type == "succeeded":
                msg = r.result.message
                if msg.stop_reason in ("refusal", "max_tokens"):
                    errors[r.custom_id] = f"stop_reason={msg.stop_reason}"
                    continue
                raw[r.custom_id] = (next(c.text for c in msg.content if c.type == "text"), _usage(msg.usage))
            else:
                errors[r.custom_id] = r.result.type
        backend, run_id = "api-batch", b.id
    else:
        for a, user, _ in todo:
            try:
                msg = client.messages.create(**_params(system, user))
            except anthropic.APIStatusError as e:
                errors[a.id] = f"{e.status_code}: {e.message}"
                continue
            if msg.stop_reason in ("refusal", "max_tokens"):
                errors[a.id] = f"stop_reason={msg.stop_reason}"
                continue
            raw[a.id] = (next(c.text for c in msg.content if c.type == "text"), _usage(msg.usage))
        backend, run_id = "api-sync", dt.datetime.now().strftime("sync-%Y%m%dT%H%M%S")
    saved = []
    for aid, (text, usage) in raw.items():
        try:
            card = Card.model_validate_json(text)
        except ValueError as e:
            errors[aid] = f"invalid card: {e}"
            continue
        save_card(aid, card, by_id[aid][1], backend, usage)
        saved.append(usage)
    entry = {"run": run_id, "date": dt.date.today().isoformat(), "backend": backend, "model": MODEL,
             "prompt_version": PROMPT_VERSION, "requested": len(todo), "cards": len(saved),
             "input_tokens": sum(u["input"] + u["cache_read"] + u["cache_write"] for u in saved),
             "output_tokens": sum(u["output"] for u in saved), "est_cost_usd": _cost(saved, batch),
             "errors": errors}
    _log_run(entry)
    return entry


def prepare(assets: list[inv.Asset], force: bool = False) -> int:
    """Subagent backend: write one self-contained prompt file per document."""
    system, todo = plan(assets, force)
    PROMPT_DIR.mkdir(parents=True, exist_ok=True)
    for a, user, sha in todo:
        (PROMPT_DIR / f"{a.id}.json").write_text(json.dumps(
            {"asset_id": a.id, "text_sha256": sha, "system": system, "user": user, "schema": _schema()}, ensure_ascii=False))
    return len(todo)


def ingest(results: dict[str, dict]) -> tuple[list[str], dict[str, str]]:
    """Subagent backend: validate {asset_id: card-json} and save."""
    ok, errors = [], {}
    for aid, data in results.items():
        prompt = PROMPT_DIR / f"{aid}.json"
        try:
            sha = json.loads(prompt.read_text())["text_sha256"]
            save_card(aid, Card.model_validate(data), sha, "subagent")
            ok.append(aid)
        except (OSError, ValueError, KeyError) as e:
            errors[aid] = str(e)
    return ok, errors
