---
title: Prior art for proposal content and AI grant writing
slug: index
level: 1
parent: ../index.md
related: [../provenance/index.md, ../knowledge-representation/index.md]
tags: [prior-art, rfp-software, grant-ai, proposal-management, build-vs-buy]
status: draft
updated: 2026-09-25
---

# Prior art for proposal content and AI grant writing

> **TL;DR** Nothing on the market fits a small partner firm that needs an inspectable, git-native library plus funder-specific requirement models. **Build** gentext, **don't buy** an RFP platform or grant-AI tool as the core, and **borrow** a lot: content governance from RFP libraries (owners, review cadences, freshness, moderation), compliance matrices and color-team reviews from federal proposal practice, acronym and plain-language checks from proposal QA tools, and citation gates from a small open-source project.

## The question

Who has already solved "reusable proposal prose + requirement tracking + drafting + QA", and what should gentext take from them?

## Landscape (September 2026)

| Segment | Examples | What they do well | Why not for us |
|---|---|---|---|
| Enterprise RFP content libraries | Loopio, Responsive (ex-RFPIO), Upland Qvidian, Ombud | Mature governance: SME owners, scheduled review cycles, moderation, freshness and usage stats, archive-not-delete | Built for sales security questionnaires; closed stores; seat pricing; weak on narrative grants, rubrics, and length variants |
| AI-native RFP tools | Inventive AI, AutoRFP.ai, many startups | Sentence-level citations, "information unavailable" flags, conflict/staleness detection | Same closed-store problem; marketing claims hard to verify |
| Grant-specific AI assistants | Instrumentl Apply, Grantable, Grantboost, Granted AI, OpenGrants, Fundwriter, Candid | Funder discovery (990 data), RFP-to-outline, "org memory" of past proposals, mock review | Opaque retrieval, generic prose risk, no fact registry, no provenance you can audit |
| Federal proposal practice | Shipley, APMP Body of Knowledge | Compliance matrix ("shred" every requirement), color-team reviews, theme statements | A method, not software. Free to borrow |
| Proposal QA tools | VisibleThread | Acronym checks (undefined, conflicting, used before defined), readability, watchwords | Enterprise product; we can reproduce the checks we need in M7 |
| Open source | `rfp-evaluation-matrix` (Claude + stdlib citation checker), `ai-for-grant-writing` (prompt list), ~19 small `rfp-automation` repos | Patterns, not products | Nothing mature enough to adopt |
| Funder policy | NIH NOT-OD-25-132, NSF 2023 notice, Candid survey, PNAS 2026 study | Sets the rules for AI-assisted text | Constraints we must model, not tools |

## Recommendation: build, borrow, buy nothing (for now)

- **Build** the library, fact registry, solicitation models, and checks as planned in DR-0003. The commercial tools confirm the design (owners, citations, "unavailable" flags) but hide it behind a closed store. That fails our inspectability test.
- **Borrow** governance fields, review workflows, and QA checks (list below).
- **Buy** nothing now. Revisit only for *funder discovery* (Instrumentl, Candid), which is outside gentext's scope.

## Ideas to borrow, mapped to modules

1. **Owner + review cadence per chunk type**: add `owner`, `review_every`, and `next_review` alongside `last_reviewed`. Fact-heavy chunks get a short cycle; evergreen methods a long one. (M2, M3) See [governance](content-library-governance.md).
2. **Freshness and usage stats**: log which chunk variant went into which submission, and the outcome. Build a `library-health` report from it. (M2, M10, M8)
3. **Moderation gate**: text harvested from Claude Docs lands as a `draft` variant until a named moderator promotes it. (M9 → M2)
4. **ROT audit** (redundant, outdated, trivial): near-duplicates (M1), expired facts (M3), client-specific leftovers (M7 leakage check) as one periodic job.
5. **Few broad tags, controlled vocabulary**: fewer, clearer topics beat hundreds of tags. (M2, M3)
6. **Sentence-level citations + "information unavailable"**: the market's best anti-hallucination feature is our provenance map and `[[NEEDS SOURCE]]`. Keep it. (M6)
7. **Shred to one requirement per row**, including "hidden" requirements in narrative and scoring text, in the funder's numbering. (M5) See [compliance matrix](compliance-matrix.md).
8. **Citation gate on extraction**: every extracted requirement must quote the solicitation verbatim with page/line, checked by code. (M5, M7) See [rfp-evaluation-matrix](rfp-evaluation-matrix.md).
9. **Color-team stages as QA modes**: pink (structure vs rubric), red (independent scoring as the evaluator, our adversarial LLM pass), gold (final compliance). (M7, M8) See [color teams](color-team-review.md).
10. **Theme statements**: benefit + discriminator + proof, with the proof pointing at M3 facts. (M2, M3, M6)
11. **Acronym checks**: undefined, conflicting, used before defined, redefined. This catches the pilot's UTCI defect. (M7) See [VisibleThread](visiblethread.md).
12. **Plain-language rules and watchwords** as deterministic style checks. (M4, M7) See [plain language](plain-language-guidelines.md).
13. **Funder AI-use rules in the solicitation model**, plus a provenance-derived disclosure note. (M5, M6) See [funder AI policies](funder-ai-policies.md).
14. **Distinctiveness check**: flag drafts that echo the funder's own wording or generic funded-proposal language. (M4, M7)
15. **Multi-perspective mock review** (several reviewer personas, then reconciliation) for the red-team pass. (M7)

## Pages in this topic

Level 2
- [Content library governance](content-library-governance.md): how RFP and grant tools keep reusable answers accurate.
- [Proposal management practice](proposal-management-practice.md): compliance matrices, color teams, themes, QA standards, funder policy.

Level 3
- [Loopio](loopio.md)
- [Responsive (formerly RFPIO)](responsive.md)
- [AI-native RFP tools](ai-native-rfp-tools.md)
- [Grant-writing AI assistants](grant-writing-ai-assistants.md)
- [Compliance matrix](compliance-matrix.md)
- [Color-team review](color-team-review.md)
- [VisibleThread](visiblethread.md)
- [rfp-evaluation-matrix (open source)](rfp-evaluation-matrix.md)
- [Plain language guidelines](plain-language-guidelines.md)
- [Funder AI policies and reviewer signals](funder-ai-policies.md)

Up: [Research index](../index.md)
