---
title: Content library governance
slug: content-library-governance
level: 2
parent: index.md
related: [loopio.md, responsive.md, ai-native-rfp-tools.md, grant-writing-ai-assistants.md]
tags: [governance, content-library, metadata, review-cycle, rfp-software]
status: draft
updated: 2026-09-25
---

# Content library governance

> **TL;DR** Every serious RFP content library has the same governance model: each answer has an SME **owner**, a **review cycle** matched to how fast its content goes stale, a **moderator** who approves edits, **freshness and usage** stats, and **archive rather than delete**. Vendors and reviewers agree that AI answer quality depends on this upkeep. adapt-rfp should adopt the model as frontmatter fields plus a health report, without the platforms.

## Why this matters

DR-0003's M2 frontmatter already has `owner`, `status`, and `last_reviewed`. The commercial tools show which extra fields make that governance work, and how it fails: a library nobody maintains produces bad AI answers.

## What the platforms keep

| Practice | Loopio | Responsive | Qvidian | Ombud | AI-native (Inventive etc.) |
|---|---|---|---|---|---|
| SME owner per entry | Yes, owner/reviewer breakdown report | Yes, the owner "should be the SME responsible for accuracy" | Yes (SME review routing) | SME answers stored as approved content | Library owners prompted |
| Scheduled review cycles | Per entry, subcategory, or category; multi-reviewer | Default cycle; Any/All/Sequential reviewers | Push notice after 6 or 12 months without update | *(unverified)* | Flags content untouched ~6 months |
| Moderation / approval | Multi-step review (plan-dependent) | Moderator approves every edit and new entry | Multi-step approvals, audit trail | "Approved" flag visible to writers | Governance agent flags conflicts |
| Freshness / usage stats | "Freshness Score" (times used + last reviewed); library health report | Last-used search; duplicate report; "similar content" | Usage tracking; expiration dates | Tracks reuse; team voting on content | Stale flags; live sync to source systems |
| Disposal | Weed duplicates; one customer deletes unused entries after a year | Archive ("warehouse"), don't delete | Expiration dates | n/a | Pulls from live sources instead of a library |

Sources for each cell are in the cards: [Loopio](loopio.md), [Responsive](responsive.md), [AI-native RFP tools](ai-native-rfp-tools.md). Qvidian and Ombud rows come from vendor pages seen as search summaries, not fetched directly: [Qvidian](https://uplandsoftware.com/qvidian/resources/blog/its-time-to-stop-losing-great-rfp-answers-and-proposal-content/), [Ombud](https://www.ombud.com/product/overview) (both accessed 2026-09-25, *(unverified detail)*).

## Review cadence: published examples

Two vendors publish cadences by content type:

- **Responsive**: corporate facts every 90 days; product content every 6–12 months or on release; evergreen answers every 12–24 months. ([Responsive blog](https://www.responsive.io/blog/rfp-answer-library-content-audit), accessed 2026-09-25)
- **Loopio**: legal/compliance annual; financials quarterly; product features bi-weekly; security bi-monthly. ([Loopio blog](https://loopio.com/blog/best-practices-to-maintaining-accurate-content/), accessed 2026-09-25)

A mapping for adapt-rfp chunk types (a proposal, not vendor advice):

| adapt-rfp chunk / record | Suggested cadence | Trigger events |
|---|---|---|
| M3 facts with numbers (tract data, CHAT scores, budgets, staff counts) | 90 days, or at the fact's `valid_until` | New census or CalEnviroScreen release |
| `org-profile`, `boilerplate` | 6 months | Staff or service change |
| `project-case` | 12 months | Project milestone, award, completion |
| `method`, `capability` | 12–24 months | New tool or method (e.g., modeling stack change) |
| `site-context`, `network` | Per pursuit | Partner changes |

## The ROT audit

Responsive's audit sorts content into **R**edundant, **O**utdated, **T**rivial. Each maps to a adapt-rfp check:

- *Redundant*: near-duplicate detection (M1). The pilot's forked Ambrose files are the obvious case.
- *Outdated*: "not used in the last year" plus expired facts (M3 validity windows).
- *Trivial*: Responsive finds these by searching client names, which is our **context-leakage** check (M7) run over the library rather than a draft.

## Failure mode: the library rots and the AI inherits it

Review aggregators and competitors repeat the same complaint about Loopio's "Magic": it works on simple questions and fails when "the Library is not sufficiently maintained" ([AutoRFP.ai summary of reviews](https://autorfp.ai/blog/loopio-reviews), accessed 2026-09-25; a competitor's page, so read it with care). AI-native vendors answer by syncing live from SharePoint or Confluence instead of a curated library ([Inventive](https://www.inventive.ai/features), accessed 2026-09-25). That trades curation for freshness and gives up length variants and lineage. For a small firm writing narrative grants, curation wins, but only if upkeep is cheap. So M1 and M8 should *propose* metadata and reviews, and humans should only confirm.

## Grant tools: "org memory" without governance

Grant assistants ([Grantable](https://grantable.co/), [Instrumentl Apply](https://www.instrumentl.com/capability/apply), both accessed 2026-09-25) advertise a library that "never forgets" and draws on past proposals. None of the public material describes owners, review dates, or fact validity. Past proposals go in as undifferentiated context. That is DR-0003's rejected "RAG over raw documents" option, and it will carry stale facts and context leakage forward. See [grant-writing AI assistants](grant-writing-ai-assistants.md).

## Recommendations for adapt-rfp

1. **M2 frontmatter additions**: `owner` (a person, not only `hyphae|partner`), `moderator`, `review_every` (duration), `next_review` (derived), `archived` (bool or date). Keep `last_reviewed`.
2. **Usage log** (M10, derived from compose runs): `chunk_id, variant_id, submission_id, date, outcome`. Freshness and "performance" come from this, as in Loopio's four health metrics (usage %, freshness, performance, automation %).
3. **`library-health` skill** (M8): lists overdue reviews by owner, unused chunks, near-duplicates, expired facts, and leakage hits. Its output is a to-do list. It never edits.
4. **Moderation via git**: harvested edits (M9) arrive as a branch or `status: draft` variant, and a moderator promotes them. Git history provides the audit trail the vendors sell.
5. **Archive, don't delete**: `status: archived` keeps the chunk retrievable for lineage.
6. **Keep tags few**: one Loopio customer cut 500+ tags to 75 ([Loopio blog](https://loopio.com/blog/proposal-content-management/), accessed 2026-09-25). Use M3's controlled vocabulary and don't allow free-form tags.

Up: [Prior art](index.md)
