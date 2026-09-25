---
title: "Proposal management practice: compliance matrices, color teams, themes"
slug: proposal-management-practice
level: 2
parent: index.md
related: [compliance-matrix.md, color-team-review.md, visiblethread.md, rfp-evaluation-matrix.md, plain-language-guidelines.md, funder-ai-policies.md]
tags: [shipley, apmp, compliance-matrix, color-team, review, qa]
status: draft
updated: 2026-09-25
---

# Proposal management practice: compliance matrices, color teams, themes

> **TL;DR** Federal proposal practice (Shipley, APMP) already has the workflow gentext is rebuilding: **shred** the solicitation into one row per requirement (M5), write to **theme statements** backed by proof (M2/M3/M6), and review in **staged color teams** where an independent **red team** scores the draft the way an evaluator would. That red team is our adversarial LLM pass (M7). The method is free to borrow. Add proposal QA checks (acronyms, readability, plain language) and current funder AI policies.

## 1. Compliance matrix (M5)

The APMP Body of Knowledge guidance, as presented at the APMP Western chapter, says: build the matrix early, before writing; shred line by line so every "shall/must/should/will" is its own row; follow the customer's numbering; keep it current through amendments; look for **hidden requirements** in narrative and evaluation text; and treat the matrix as the writers' plan and the reviewers' checklist ([Conniff, APMP Western 2023](https://apmp-western.org/wp-content/uploads/2023/10/WRC2023-Conniff-Shred-For-Success.pdf), accessed 2026-09-25).

For EHCRP this means the Appendix F rubric "High" descriptors are requirements too. "Community voices… quotes or stories" is a hidden requirement, and the pilot drafts miss it (DR-0002 §7). Details: [compliance matrix card](compliance-matrix.md). For a deterministic gate that proves each row really came from the source, see [rfp-evaluation-matrix](rfp-evaluation-matrix.md).

## 2. Color-team reviews (M7)

Shipley's staged reviews are named by color. Shipley's own public pages describe the course but not the stages ([Shipley](https://www.shipleywins.com/training/winning-color-team-reviews), accessed 2026-09-25). The table below follows a secondary playbook ([GovEagle](https://www.goveagle.com/blog/pink-red-gold-team-reviews-playbook), accessed 2026-09-25; practitioner blog, consistent with other guides):

| Team | When | Who | Scores against | gentext analogue |
|---|---|---|---|---|
| Blue | Before writing | Capture lead | Win strategy | `model-solicitation` + outline |
| Pink | ~20–40% draft | Writers, SMEs | Structure vs requirements/criteria | `check-draft --stage pink`: coverage map of rubric items to outline |
| Red | ~80–90% draft | **Independent** reviewers acting as evaluators | Evaluation criteria (rubric bands) | Adversarial LLM judge in a *fresh context* with only the solicitation and the draft |
| Gold | Final, 1–2 days out | Leadership, contracts | Compliance, pricing, polish | Deterministic gate: limits, budget %, names, leakage |

The key idea for us is **independence**. Red-team reviewers did not write the proposal, and they score it with the evaluator's own criteria. An LLM that has just drafted the answer, with the library in context, is a poor red team. Card: [color-team review](color-team-review.md).

## 3. Theme statements and proof (M2, M3, M6)

Shipley: "Theme statements in proposals link a customer benefit to the discriminating features of your offer." State the benefit first, quantify it, keep it to about one sentence, and use it consistently ([Shipley blog](https://www.shipleywins.com/blogs/effective-theme-statements), accessed 2026-09-25). Practitioner guides add that every benefit needs **proof** (past performance, data). That maps straight onto gentext:

- A `theme` chunk type (or a `themes[]` field on a solicitation response plan) with `benefit`, `discriminator`, `proof: [fact ids]`.
- M7 check: every theme used in a draft has at least one resolvable fact. That makes the check for "unhedged boosters" ("cutting-edge", DR-0002 §6) *constructive*: replace the booster with a proof point.

## 4. Proposal QA standards (M4, M7)

- **Acronyms**: VisibleThread checks four failure types: undefined, conflicting definitions, used before defined, defined more than once ([VisibleThread](https://www.visiblethread.com/acronym-checks/), accessed 2026-09-25). "Conflicting definitions" is exactly the pilot's UTCI defect. Card: [VisibleThread](visiblethread.md).
- **Plain language**: federal plain-language principles (audience, active voice, topic sentences, lists, tables) and "must, not shall". The canonical plainlanguage.gov text now sits in an archived public-domain GitHub repo. Card: [plain language](plain-language-guidelines.md).

## 5. The funder side: AI policy and reviewer signals (M5, M7)

- NIH (NOT-OD-25-132, 2025-07-17): applications "substantially developed by AI" are not considered original; NIH says it uses AI-detection technology.
- NSF (2023-12-14): proposers are *encouraged* to disclose AI use and are responsible for accuracy.
- A 2026 PNAS study: NIH proposals with stronger LLM-writing signals were funded more often but were **less semantically distinctive**.
- Candid 2025: only 1% of foundations use generative AI to screen applications.

Card with sources: [funder AI policies](funder-ai-policies.md). In practice: record each solicitation's AI rule in M5, keep provenance so a disclosure can be generated truthfully, and add a distinctiveness check to M7.

## Proposed M7 stage design (synthesis)

```
check-draft --stage pink   # outline vs M5 matrix: every requirement has a home; word budgets
check-draft --stage red    # independent LLM evaluator(s): score each rubric band, cite evidence
                           #   spans, list "what a Low reviewer would say"; no library in context
check-draft --stage gold   # deterministic: limits, acronyms, entity names, leakage, facts resolve,
                           #   budget %s, funder AI-use rule satisfied
```

Each stage writes to the same machine-readable report. The compliance matrix's `status` column is updated from the report, so the matrix, as in Shipley practice, is the single thread through all reviews.

Up: [Prior art](index.md)
