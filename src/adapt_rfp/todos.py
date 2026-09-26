"""Open items for an application round: decisions, questions and tasks (DR-0014).

The canonical store is one `todos.yaml` per solicitation round, for example
`solicitations/lci/ehcrp/round-2/todos.yaml`. Items collect between partner meetings.
`agenda` renders the open partner-meeting items as a shareable Markdown agenda, and `tk`
lists TK notes in drafts that no item covers yet.
"""

from __future__ import annotations

import datetime as dt
import re
from enum import Enum
from pathlib import Path
from typing import Annotated

import yaml
from pydantic import BaseModel, ConfigDict, Field, StringConstraints, model_validator

TodoId = Annotated[str, StringConstraints(pattern=r"^t-\d{3}$")]

ROUND_DIR = Path("solicitations/lci/ehcrp/round-2")
TODOS_FILE = ROUND_DIR / "todos.yaml"


class Kind(str, Enum):
    decision = "decision"  # a choice the team must make together
    question = "question"  # a fact or file one named person can supply
    task = "task"          # work someone does


class Status(str, Enum):
    open = "open"
    answered = "answered"  # resolution recorded; drafts/model not yet updated
    done = "done"          # resolution applied everywhere it matters
    dropped = "dropped"    # no longer needed (say why in resolution)


class Venue(str, Enum):
    partner_meeting = "partner-meeting"  # needs Brent + ARPD + co-applicants in one room
    ask = "ask"                          # one person can answer asynchronously
    internal = "internal"                # Hyphae / Claude work, no partner input needed


class Topic(str, Enum):
    partnership = "partnership"
    planning_document = "planning-document"
    scope = "scope"
    harm_reduction = "harm-reduction"
    belonging = "belonging"
    budget = "budget"
    evidence = "evidence"
    admin = "admin"


class _Model(BaseModel):
    model_config = ConfigDict(extra="forbid", use_enum_values=True)


class Added(_Model):
    date: dt.date
    by: str


class Resolution(_Model):
    date: dt.date
    decided_by: list[str]
    text: str


class Todo(_Model):
    id: TodoId
    title: str
    kind: Kind
    status: Status = Status.open
    venue: Venue
    topic: Topic
    priority: int = Field(ge=1, le=3)       # 1 = blocks drafting before Oct 13
    ask: list[str] = []                     # who must answer or decide
    owner: str | None = None                # who drives it to closure
    apps: list[str] = ["ambrose-center-park"]
    affects: list[str] = []                 # question ids, workbook, forms
    context: str                            # shareable wording: no contact details, no candid assessments
    options: list[str] = []
    proposal: str | None = None             # our recommendation, if any
    sources: list[str] = []                 # asset ids, file paths, feedback ids
    depends_on: list[TodoId] = []
    due: dt.date | None = None
    added: Added
    resolution: Resolution | None = None

    @model_validator(mode="after")
    def _rules(self):
        if self.status != "open" and not self.resolution:
            raise ValueError(f"{self.id}: status {self.status} needs a resolution")
        if self.venue in ("partner-meeting", "ask") and not self.ask:
            raise ValueError(f"{self.id}: venue {self.venue} needs `ask` (who answers)")
        return self


class TodoList(_Model):
    todos: list[Todo]

    @model_validator(mode="after")
    def _unique(self):
        ids = [t.id for t in self.todos]
        dupes = {i for i in ids if ids.count(i) > 1}
        if dupes:
            raise ValueError(f"duplicate todo ids: {sorted(dupes)}")
        known = set(ids)
        for t in self.todos:
            missing = [d for d in t.depends_on if d not in known]
            if missing:
                raise ValueError(f"{t.id}: depends_on unknown ids {missing}")
        return self

    def next_id(self) -> str:
        n = max((int(t.id[2:]) for t in self.todos), default=0)
        return f"t-{n + 1:03d}"


def load(path: Path = TODOS_FILE) -> TodoList:
    return TodoList(todos=yaml.safe_load(path.read_text()) or [])


TOPIC_ORDER = [t.value for t in Topic]


def render_agenda(tl: TodoList, app: str | None = None, date: str | None = None) -> str:
    """Open partner-meeting items, grouped by topic. Decisions first within a topic."""
    items = [t for t in tl.todos if t.status == "open" and t.venue == "partner-meeting"
             and (app is None or app in t.apps)]
    items.sort(key=lambda t: (TOPIC_ORDER.index(t.topic), t.kind != "decision", t.priority, t.id))
    title = f"Partner meeting agenda{f': {app}' if app else ''}{f' ({date})' if date else ''}"
    out = [f"# {title}", "",
           "_Generated from `todos.yaml` by `adapt-rfp todo agenda`. Edit the YAML, not this file._", ""]
    for topic in TOPIC_ORDER:
        group = [t for t in items if t.topic == topic]
        if not group:
            continue
        out += [f"## {topic.replace('-', ' ').capitalize()}", ""]
        for t in group:
            out.append(f"### {t.id} · {t.title}")
            out.append(f"*{t.kind}, priority {t.priority}; affects {', '.join(t.affects) or '—'}*")
            out += ["", t.context.strip()]
            if t.options:
                out += ["", "Options:"] + [f"- {o}" for o in t.options]
            if t.proposal:
                out += ["", f"Proposal: {t.proposal.strip()}"]
            if t.depends_on:
                out += ["", f"Depends on: {', '.join(t.depends_on)}"]
            out.append("")
    pre = [t for t in tl.todos if t.status == "open" and t.venue == "ask" and t.priority == 1
           and (app is None or app in t.apps)]
    if pre:
        out += ["## Before the meeting (async asks)", ""]
        out += [f"- {t.id} · {t.title} (ask: {', '.join(t.ask)})" for t in pre]
        out.append("")
    return "\n".join(out)


TK_RE = re.compile(r"\{>>TK\s+(\w+):(.*?)<<\}", re.S)
TODO_REF_RE = re.compile(r"\bt-\d{3}\b")


def uncovered_tk(root: Path = ROUND_DIR) -> list[tuple[Path, str, str]]:
    """TK notes in answer drafts that don't cite a todo id (t-NNN)."""
    hits = []
    for p in sorted(root.glob("applications/*/answers/*.md")):
        draft = p.read_text().split("## Provenance", 1)[0]
        for m in TK_RE.finditer(draft):
            if not TODO_REF_RE.search(m.group(2)):
                hits.append((p, m.group(1), " ".join(m.group(2).split())[:100]))
    return hits
