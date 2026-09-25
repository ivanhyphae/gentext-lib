"""Asset inventory: discovery and acquisition manifest (DR-0010, module M11).

The canonical store is `inventory/assets.yaml` (one list of asset records) plus
`inventory/sweeps.yaml` (a log of discovery runs). Both are plain YAML in git;
`inventory/index.md` is generated from them.
"""

from __future__ import annotations

import datetime as dt
import hashlib
from collections import Counter
from enum import Enum
from pathlib import Path
from typing import Annotated

import yaml
from pydantic import BaseModel, ConfigDict, Field, StringConstraints, model_validator

Slug = Annotated[str, StringConstraints(pattern=r"^[a-z0-9][a-z0-9-]*$")]

INVENTORY_DIR = Path("inventory")
ASSETS_FILE = INVENTORY_DIR / "assets.yaml"
SWEEPS_FILE = INVENTORY_DIR / "sweeps.yaml"
INDEX_FILE = INVENTORY_DIR / "index.md"


class Kind(str, Enum):
    solicitation = "solicitation"        # RFP / NOFA / guidelines / forms
    proposal = "proposal"                # a submitted or final proposal
    proposal_draft = "proposal-draft"    # working drafts, pre-apps
    working_doc = "working-doc"          # mixed strategy/notes/drafts docs (like the pilot)
    award_list = "award-list"            # funded-project lists, winners
    guidance = "guidance"                # funder FAQs, webinars, tools, rubrics outside the RFP
    report = "report"                    # project deliverables, studies, plans
    presentation = "presentation"
    dataset = "dataset"
    template = "template"
    notes = "notes"                      # meeting notes (context only by default, DR-0004)
    other = "other"


class Status(str, Enum):
    wanted = "wanted"          # known or suspected to exist; not yet located
    discovered = "discovered"  # located; not yet triaged
    include = "include"        # triaged: acquire it
    defer = "defer"            # triaged: maybe later
    exclude = "exclude"        # triaged: not useful (kept so sweeps skip it)
    acquired = "acquired"      # a local copy or text export exists (see `local`)
    ingested = "ingested"      # converted by M0 (see `ingest_id`)
    harvested = "harvested"    # chunks promoted into the library


class System(str, Enum):
    gdrive = "gdrive"
    web = "web"
    local = "local"
    email = "email"
    other = "other"


class _Model(BaseModel):
    model_config = ConfigDict(extra="forbid", use_enum_values=True)


class Location(_Model):
    system: System
    id: str | None = None          # Drive file id, etc.
    url: str | None = None
    mime: str | None = None
    size: int | None = None        # bytes, as reported by the source system
    modified: dt.date | None = None
    owner: str | None = None       # source-system owner (who to ask)
    parent: str | None = None      # Drive folder id


class Relevance(_Model):
    programs: list[str] = []
    funders: list[str] = []
    places: list[str] = []
    projects: list[str] = []
    note: str = ""


class Discovered(_Model):
    date: dt.date
    by: str                        # person or model id
    sweep: str | None = None       # sweeps.yaml id


class Local(_Model):
    path: str                      # repo-relative
    sha256: str | None = None
    acquired: dt.date | None = None
    via: str | None = None         # connector-text | drive-api | manual | web


class Asset(_Model):
    id: Slug
    title: str
    kind: Kind
    status: Status
    priority: int | None = Field(default=None, ge=1, le=3)
    location: Location | None = None
    hint: str | None = None        # for `wanted`: where it might be / who might have it
    relevance: Relevance = Relevance()
    discovered: Discovered | None = None
    local: Local | None = None
    ingest_id: str | None = None
    steward: str | None = None
    notes: str = ""

    @model_validator(mode="after")
    def _status_rules(self) -> "Asset":
        s = self.status
        if s != Status.wanted.value and self.location is None and self.local is None:
            raise ValueError(f"{self.id}: status '{s}' needs a location or local copy")
        if s in (Status.acquired.value, Status.ingested.value, Status.harvested.value) and self.local is None:
            raise ValueError(f"{self.id}: status '{s}' needs `local`")
        if s == Status.wanted.value and not (self.hint or self.relevance.note):
            raise ValueError(f"{self.id}: wanted assets need a hint or relevance note")
        return self


class Sweep(_Model):
    id: Slug
    date: dt.date
    by: str
    system: System
    method: str                    # e.g. "gdrive search_files", "web search"
    queries: list[str] = []
    found: int | None = None
    recorded: int | None = None
    notes: str = ""


class Inventory(_Model):
    assets: list[Asset]
    sweeps: list[Sweep] = []

    @model_validator(mode="after")
    def _unique(self) -> "Inventory":
        dup = [k for k, n in Counter(a.id for a in self.assets).items() if n > 1]
        if dup:
            raise ValueError(f"duplicate asset ids: {dup}")
        keys = [(a.location.system, a.location.id) for a in self.assets if a.location and a.location.id]
        dupk = [k for k, n in Counter(keys).items() if n > 1]
        if dupk:
            raise ValueError(f"duplicate source ids: {dupk}")
        sweep_ids = {s.id for s in self.sweeps}
        missing = {a.discovered.sweep for a in self.assets if a.discovered and a.discovered.sweep} - sweep_ids
        if missing:
            raise ValueError(f"assets reference unknown sweeps: {sorted(missing)}")
        return self

    def find_source(self, system: str, source_id: str) -> Asset | None:
        for a in self.assets:
            if a.location and a.location.system == system and a.location.id == source_id:
                return a
        return None


def load(root: Path = Path(".")) -> Inventory:
    assets = yaml.safe_load((root / ASSETS_FILE).read_text()) or []
    sweeps_path = root / SWEEPS_FILE
    sweeps = (yaml.safe_load(sweeps_path.read_text()) or []) if sweeps_path.exists() else []
    return Inventory(assets=assets, sweeps=sweeps)


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


STATUS_ORDER = [s.value for s in Status]


def render_index(inv: Inventory) -> str:
    """Progressive-disclosure index: counts first, then open work, then everything."""
    counts = Counter(a.status for a in inv.assets)
    lines = [
        "# Asset inventory",
        "",
        "> Generated by `uv run gentext inventory index` from `assets.yaml` and `sweeps.yaml`. Do not edit by hand.",
        "",
        "| Status | Count |",
        "|---|---|",
    ]
    lines += [f"| {s} | {counts[s]} |" for s in STATUS_ORDER if counts[s]]

    def table(title: str, items: list[Asset]) -> list[str]:
        if not items:
            return []
        out = ["", f"## {title}", "", "| P | id | kind | status | title | note |", "|---|---|---|---|---|---|"]
        for a in sorted(items, key=lambda a: (a.priority or 9, a.id)):
            link = a.location.url if a.location and a.location.url else None
            name = f"[{a.title}]({link})" if link else a.title
            note = (a.relevance.note or a.hint or a.notes).replace("|", "/").replace("\n", " ")
            out.append(f"| {a.priority or ''} | `{a.id}` | {a.kind} | {a.status} | {name} | {note} |")
        return out

    open_work = [a for a in inv.assets if a.status in ("wanted", "discovered", "include")]
    have = [a for a in inv.assets if a.status in ("acquired", "ingested", "harvested")]
    later = [a for a in inv.assets if a.status == "defer"]
    lines += table("Open: wanted, discovered, include", open_work)
    lines += table("In hand: acquired, ingested, harvested", have)
    lines += table("Deferred", later)
    excluded = [a for a in inv.assets if a.status == "exclude"]
    if excluded:
        lines += ["", f"## Excluded ({len(excluded)})", ""]
        lines += [f"- `{a.id}` — {a.title}: {a.notes or a.relevance.note}" for a in sorted(excluded, key=lambda a: a.id)]
    if inv.sweeps:
        lines += ["", "## Sweeps", "", "| id | date | system | method | found | recorded |", "|---|---|---|---|---|---|"]
        lines += [f"| `{s.id}` | {s.date} | {s.system} | {s.method} | {s.found or ''} | {s.recorded or ''} |" for s in inv.sweeps]
    return "\n".join(lines) + "\n"
