# 0004. Source corpus in the private repo; sensitivity tagging

- Status: Accepted (2026-09-25)
- Date: 2026-09-25
- Deciders: Ivan Heitmann; Claude (drafting)

## Context
The pilot sources (`projects/EHCRP Round 2/`) include staff emails and phone numbers, internal meeting notes with action items, candid assessments of partner capacity and eligibility, outreach templates addressed to named individuals, and pre-decisional strategy. The maintainer decided that the repo will be **private** and will keep sample data in it. The README also targets cloud deployment for Claude web, which widens exposure later.

## Decision
1. `projects/` (raw sources) **is committed** to the private repo. The M0 manifest still records each source's path and sha256, so derived chunks can cite exact source versions.
2. Every library chunk, fact, and entity carries a `sensitivity` tag:
   - `public`: already published or cleared for any proposal/marketing use.
   - `internal`: reusable in proposals, not published verbatim elsewhere.
   - `partner`: owned by or about a partner. Reuse follows the partner relationship (see DR-0008 on authorship).
   - `restricted`: personal data or candid assessments. Never promoted to the library.
3. M1 treats contact blocks, meeting notes, and action items as context-only by default.
4. Anything leaving the repo (Claude Docs, published artifacts, third-party APIs such as embedding services) is limited by the tag. Raw `projects/` text goes out only when a human asks.

## Consequences
- Collaborators and agents get the full corpus with no separate store to manage.
- Making the repo public or widely shared later would require removing `projects/` from history, which is costly. Treat "private" as a hard constraint. Revisit before any deployment that syncs the repo to a hosted service.
- Choosing an embedding or search provider now has to check what text leaves the machine.

## Alternatives considered
- Sources out of git (the original proposal): safer, but it adds a second store for a small private team. Rejected by the maintainer.

## Open questions
- Who can clear a chunk as `public`?

## Revisions
- 2026-09-25: Replaced the proposed "keep sources out of git" decision with "commit in private repo", per the maintainer.
