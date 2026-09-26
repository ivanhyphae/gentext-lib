# 0014. Open items list and partner-meeting agenda

- Status: Proposed
- Date: 2026-09-26
- Deciders: Ivan Heitmann; Claude (drafting)

## Context
Drafting the Center Park answers surfaced many things a person has to supply or decide. Some are choices only the partners can make together: the co-applicant, the Planning Document type, the demonstration scope, the split with the IRWM project, and Belonging. Others are single asks, such as the submitted pre-app text or survey permissions. So far they lived in chat replies, draft footers, `TK` notes and `status.md`, and nothing gathered them. The maintainer asked for one tracked list, and a protocol for adding to it, until a meeting with Brent and the co-applicants.

## Decision
1. **One YAML list per solicitation round:** `solicitations/<funder>/<program>/<round>/todos.yaml`, validated by `adapt_rfp.todos` (pydantic). Items span that round's applications (`apps`).
2. **Item shape:**
   - `kind`: decision | question | task
   - `venue`: partner-meeting | ask | internal. This decides whether an item takes meeting time.
   - `topic` and `priority`, which order the agenda.
   - Shareable `context`, `options` and `proposal`.
   - `ask` (who answers), `owner` (who drives it to closure), `affects` (question ids), `sources`, `depends_on`, `due`.
   - `status`: open → answered → done, or dropped. A `resolution` (date, who decided, text) is required for any status other than `open`.
3. **Draft linkage:** every `TK` note in an answer draft cites an item id. `adapt-rfp todo tk` reports TK notes that don't, and a test enforces it.
4. **The agenda is generated** (`adapt-rfp todo agenda`) from open partner-meeting items, grouped by topic with decisions first, plus priority-1 async asks as "before the meeting". The YAML is the source. A rendered agenda is a dated snapshot, reviewed by the maintainer before it goes to anyone.
5. The protocol lives in AGENTS.md ("Open items and the partner meeting").

## Consequences
- Anything that needs a person has exactly one home, visible to every session and collaborator.
- Meeting time goes to decisions, because single-person asks are routed to `ask`.
- Item text may be shown to partners, so it must stay neutral. That is a writing constraint on Claude.
- There is one more file to keep current. The TK-linkage test keeps drafts and the list from drifting apart.

## Alternatives considered
- **Claude's in-session task list:** it doesn't persist across sessions and isn't visible to collaborators.
- **ClickUp or another tracker:** it keeps items away from the drafts and sources they refer to. It can be revisited if partners need to edit the list directly.
- **A Markdown checklist:** it can't be validated, filtered or rendered into an agenda, and it drifts from the TK notes.

## Open questions
- Should partners see and edit the list directly (e.g. a shared doc rendered from the YAML), or only the agenda?
- Should resolved decisions also be promoted into the application YAML automatically?

## Revisions
