"""T1 profile (DR-0011): outline, section sizes, contact-data counts, near-duplicates. No LLM.

Writes one small YAML per asset to inventory/profiles/<id>.yaml (committed).
"""

from __future__ import annotations

import datetime as dt
import hashlib
import re
from dataclasses import dataclass, field
from pathlib import Path

import yaml

from gentext import inventory as inv
from gentext.extract import EMAIL, PHONE, cached_text

PROFILE_DIR = Path("inventory/profiles")
PROFILER_VERSION = "p2"
SHINGLE = 8
FALLBACK_PART_WORDS = 600

_MD_HEADING = re.compile(r"^(#{1,6})\s+(.*\S)\s*$")
_NUMBERED = re.compile(r"^(\d+(?:\.\d+)*)\.?\s+([A-Z].{2,80})$")


@dataclass
class Section:
    path: str
    level: int
    words: int = 0
    lines: list[str] = field(default_factory=list)

    def head(self, n_words: int) -> str:
        words = " ".join(self.lines).split()
        return " ".join(words[:n_words])


def _clean_heading(s: str) -> str:
    s = re.sub(r"[*_`]+", "", s)
    s = re.sub(r"\[(.*?)\]\(.*?\)", r"\1", s)
    return s.strip(" #:")


def _is_pdf_heading(line: str, prev_blank: bool) -> tuple[int, str] | None:
    s = line.strip()
    if not s or len(s) > 90 or s.endswith((".", ",", ";")) or not prev_blank:
        return None
    m = _NUMBERED.match(s)
    if m:
        return (m.group(1).count(".") + 1, s)
    letters = [c for c in s if c.isalpha()]
    words = s.split()
    if len(letters) >= 4 and len(words) <= 10 and s.upper() == s:
        return (1, s.title())
    if 2 <= len(words) <= 8 and all(w[0].isupper() for w in words if w[0].isalpha() and len(w) > 3):
        return (2, s)
    return None


def split_sections(text: str, markdown: bool) -> list[Section]:
    sections: list[Section] = [Section(path="(preamble)", level=0)]
    trail: list[str] = []
    prev_blank = True
    for raw in text.splitlines():
        hit = None
        if markdown:
            m = _MD_HEADING.match(raw)
            if m and _clean_heading(m.group(2)):
                hit = (len(m.group(1)), _clean_heading(m.group(2)))
        else:
            hit = _is_pdf_heading(raw, prev_blank)
        if hit:
            level, title = hit
            trail = trail[: level - 1] + [title]
            sections.append(Section(path=" > ".join(trail), level=level))
        elif raw.strip():
            sections[-1].lines.append(raw.strip())
        prev_blank = not raw.strip()
    for s in sections:
        s.words = len(" ".join(s.lines).split())
    sections = [s for s in sections if s.words or s.level]
    # Too few headings to be useful: fall back to fixed-size parts.
    if sum(1 for s in sections if s.words >= 30) < 3:
        words = text.split()
        sections = []
        for i in range(0, len(words), FALLBACK_PART_WORDS):
            chunk = words[i : i + FALLBACK_PART_WORDS]
            sections.append(Section(path=f"part {i // FALLBACK_PART_WORDS + 1}", level=1, words=len(chunk), lines=[" ".join(chunk)]))
    return sections


def shingles(text: str, k: int = SHINGLE) -> set[int]:
    w = re.findall(r"[a-z0-9']+", text.lower())
    return {
        int.from_bytes(hashlib.blake2b(" ".join(w[i : i + k]).encode(), digest_size=8).digest(), "big")
        for i in range(max(0, len(w) - k + 1))
    }


def asset_text(asset: inv.Asset) -> tuple[str, list[Section]]:
    path = Path(asset.local.path)
    text = cached_text(asset.id, path)
    markdown = path.suffix.lower() in (".md", ".docx", ".xlsx")
    return text, split_sections(text, markdown)


def profile_assets(assets: list[inv.Asset]) -> list[dict]:
    """Profile the given assets; near-duplicates are computed across all of them."""
    PROFILE_DIR.mkdir(parents=True, exist_ok=True)
    texts, sects, sh = {}, {}, {}
    for a in assets:
        texts[a.id], sects[a.id] = asset_text(a)
        sh[a.id] = shingles(texts[a.id])
    out = []
    for a in assets:
        dups = []
        mine = sh[a.id]
        for b in assets:
            if b.id == a.id or not mine or not sh[b.id]:
                continue
            inter = len(mine & sh[b.id])
            if not inter:
                continue
            jac = inter / len(mine | sh[b.id])
            contained = inter / len(mine)  # share of THIS doc found in the other
            if jac >= 0.3 or contained >= 0.5:
                dups.append({"asset_id": b.id, "jaccard": round(jac, 3), "contained_in": round(contained, 3)})
        text = texts[a.id]
        prof = {
            "asset_id": a.id,
            "source_path": a.local.path,
            "source_sha256": a.local.sha256,
            "text_sha256": hashlib.sha256(text.encode()).hexdigest(),
            "words": len(text.split()),
            "pii": {"emails": len(EMAIL.findall(text)), "phones": len(PHONE.findall(text))},
            "near_duplicates": sorted(dups, key=lambda d: -d["contained_in"]),
            "sections": [{"sid": f"s{i}", "path": s.path, "level": s.level, "words": s.words} for i, s in enumerate(sects[a.id][:400], 1)],
            "section_count": len(sects[a.id]),
            "profiled": dt.date.today().isoformat(),
            "profiler": PROFILER_VERSION,
        }
        (PROFILE_DIR / f"{a.id}.yaml").write_text(yaml.safe_dump(prof, sort_keys=False, allow_unicode=True, width=200))
        out.append(prof)
    return out


def load_profile(asset_id: str) -> dict | None:
    p = PROFILE_DIR / f"{asset_id}.yaml"
    return yaml.safe_load(p.read_text()) if p.exists() else None
