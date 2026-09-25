# 0007. Collaboration workflow: Claude Docs for iteration, manual paste into Google Docs

- Status: Accepted (2026-09-25)
- Date: 2026-09-25
- Deciders: Ivan Heitmann; Claude (drafting)

## Context
- Google Docs is the team's baseline authoring surface. Proposal documents use **many tabs**.
- Per the maintainer, the Google Docs API is a poor fit for AI editing of tabbed documents: text styles aren't well exposed for tabbed docs. (Research on the current API is in `documentation/research/ingest-conversion/`.)
- This pilot is a **shadow contribution**. The lead grant writer (James) runs the customary process in Google Docs. This work runs in parallel and must not disrupt it.
- Claude Docs (claude.ai living documents) lets Claude create, edit, and answer comments directly.

## Decision
1. **Iterate in Claude Docs.** Drafts produced by M6 (with M7 QA notes) are pushed to a Claude Doc per application section. Humans comment there, and Claude revises there.
2. **Final hand-off is manual.** A human copies approved blocks into the team's Google Doc. Agents never write to the team's Google Docs.
3. **Harvest back into the repo.** Accepted text is saved to the library as a new chunk variant with lineage (`edited-in: claude-doc:<id>`, editors, date) so the round-trip keeps provenance (DR-0008).
4. Each block handed off is *paste-ready*: within the word limit, no unresolved `[[NEEDS SOURCE]]` placeholders unless flagged in bold, plain formatting that survives paste.

## Consequences
- No dependency on the Google Docs API for writing. Tab-aware *reading* of Google Docs, for ingest, is still worth solving (research topic).
- Divergence risk: the lead writer may edit pasted text further in Google Docs. Those edits reach the library only by re-ingesting the final submitted document after the deadline, which is planned as a post-submission M0 step.

## Alternatives considered
- Direct Google Docs API edits: blocked by the tab/style limitations, and too intrusive for a shadow process.
- Repo-only Markdown review: fine for agents, unfamiliar for the grant team.

## Revisions
