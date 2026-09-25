# Decision Records

Numbered, append-mostly records of how and why `gentext-lib` is shaped the way it is.

## Process

1. Copy the template below into `NNNN-kebab-title.md` (next free number, zero-padded to 4).
2. Set status **Proposed**. Discuss it with a human collaborator.
3. On agreement, set **Accepted** and add the date. On rejection, set **Rejected** and keep the file, because the reasoning is still useful.
4. To change an accepted decision, write a new record with `Supersedes: NNNN` and mark the old one `Superseded by: MMMM`.
5. For small clarifications, append to the record's **Revisions** section with the date.
6. Update the index below.

## Index

| # | Title | Status |
|---|---|---|
| [0001](0001-record-architecture-decisions.md) | Record architecture decisions | Accepted |
| [0002](0002-pilot-case-ehcrp-round-2.md) | Pilot case: EHCRP Round 2 (Bay Point) | Accepted |
| [0003](0003-module-decomposition.md) | Module decomposition | Proposed |
| [0004](0004-source-corpus-confidentiality.md) | Source corpus in the private repo; light sensitivity tagging | Accepted |
| [0005](0005-canonical-store-plain-text.md) | Canonical library is plain-text Markdown in git; indexes are derived | Proposed |
| [0006](0006-language-and-tooling.md) | Python + uv with a repo-local .venv; no system Python packages | Accepted |
| [0007](0007-collaboration-workflow-shadow-pilot.md) | Collaboration: Claude Docs iteration, manual paste to Google Docs | Accepted |
| [0008](0008-authorship-provenance.md) | Authorship as first-class provenance (chunk + optional span), for accountability/QC | Proposed |
| [0009](0009-deployment-path.md) | Deployment: Claude Code clone MVP → FastMCP on Google Cloud Run | Accepted |
| [0010](0010-asset-discovery-and-inventory.md) | Asset discovery and inventory (M11): YAML manifest, sweep log, discovery skill | Accepted |
| [0011](0011-content-triage-funnel.md) | Content triage funnel: profile → Haiku card → extract → promote; dispositions hold/reference/ignore/drop | Proposed |
| [0012](0012-solicitation-and-application-model.md) | Solicitation model with explicit applications (permutations of site/partners) | Proposed |

## Template

```markdown
# NNNN. Title

- Status: Proposed | Accepted | Rejected | Superseded by MMMM
- Date: YYYY-MM-DD
- Deciders: <names/roles>
- Supersedes: <NNNN, optional>

## Context
What forces are at play? What did we observe? (Cite pilot evidence where possible.)

## Decision
What we will do, stated plainly.

## Consequences
What becomes easier, what becomes harder, what we must now do.

## Alternatives considered
Briefly, and why not.

## Open questions
Things this record deliberately leaves unresolved.

## Revisions
- YYYY-MM-DD: <clarification>
```
