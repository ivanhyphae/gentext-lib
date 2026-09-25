# 0004. Source corpus in the private repo; sensitivity tagging

- Status: Accepted (2026-09-25)
- Date: 2026-09-25
- Deciders: Ivan Heitmann; Claude (drafting)

## Context
The pilot sources (`projects/EHCRP Round 2/`) include staff emails and phone numbers, internal meeting notes with action items, candid assessments of partner capacity and eligibility, outreach templates addressed to named individuals, and pre-decisional strategy. The maintainer decided that the repo will be **private** and will keep sample data in it. The README also targets cloud deployment for Claude web, which widens exposure later.

## Decision
1. `projects/` (raw sources) **is committed** to the private repo. The M0 manifest still records each source's path and sha256, so derived chunks can cite exact source versions.
2. Every library chunk, fact, and entity carries a light `sensitivity` tag. The default is `internal`:
   - `public`: already published (submitted proposals, website, reports).
   - `internal` (default): normal proposal prose. Fine for Claude Docs, embedding APIs, writing-feedback APIs, and LLMs.
   - `restricted`: personal contact details or candid assessments of people/partners. Never promoted to the library, and kept out of published artifacts and API payloads.
3. M1 treats contact blocks, meeting notes, and action items as context-only by default.
4. Third-party APIs are allowed for `public` and `internal` text. Only `restricted` material has an outbound limit.

## Consequences
- Collaborators and agents get the full corpus with no separate store to manage.
- Making the repo public or widely shared later would require removing `projects/` from history, which is costly. Treat "private" as a hard constraint. Revisit before any deployment that syncs the repo to a hosted service.
- Embedding and writing-feedback APIs are open choices. They are chosen for quality and cost, not for data residency.

## Alternatives considered
- Sources out of git (the original proposal): safer, but it adds a second store for a small private team. Rejected by the maintainer.

## Revisions
- 2026-09-25: Replaced the proposed "keep sources out of git" decision with "commit in private repo", per the maintainer.
- 2026-09-25: Relaxed per the maintainer. Most prose ends up public or semi-public, and embedding via APIs is fine. Dropped the `partner` tag, because authorship is tracked for accountability, not rights (DR-0008). Only `restricted` personal/candid material has limits.
