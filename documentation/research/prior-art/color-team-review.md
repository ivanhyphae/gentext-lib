---
title: Color-team review
slug: color-team-review
level: 3
parent: proposal-management-practice.md
related: [compliance-matrix.md, grant-writing-ai-assistants.md, funder-ai-policies.md]
tags: [shipley, review, red-team, llm-judge, qa]
status: draft
updated: 2026-09-25
kind: technique
verdict: adopt
fit: [M7, M8]
license: n/a (practice)
maturity: mature
inspectability: high
sources:
  - title: Shipley, Winning Color Team Reviews (course page)
    url: https://www.shipleywins.com/training/winning-color-team-reviews
    accessed: 2026-09-25
  - title: GovEagle, Pink, Red, and Gold Team Reviews playbook (Sept 2026)
    url: https://www.goveagle.com/blog/pink-red-gold-team-reviews-playbook
    accessed: 2026-09-25
  - title: VisibleThread, How to Run Shipley Color Team Reviews (search summary)
    url: https://www.visiblethread.com/blog/color-team-review-guide/
    accessed: 2026-09-25
  - title: Granted AI home page ("Granted Review Board")
    url: https://grantedai.com/
    accessed: 2026-09-25
---

# Color-team review

> **TL;DR** Shipley-style staged reviews check a proposal at set milestones. The **red team** is independent reviewers scoring the draft against the evaluation criteria as the funder would. **Adopt** the stages as M7 modes and model the adversarial LLM pass on the red team: fresh context, rubric only, evidence-cited scores.

## What it is

A sequence of reviews named by color (Blue, Pink, Red, Green, Gold, White). Shipley's public course page promises to "use formal color team reviews to ensure compliance, responsiveness, and customer focus" but doesn't define the stages publicly. The stage details below come from secondary practitioner guides. They are consistent with each other but not checked against Shipley's paid material *(partly unverified)*.

| Stage | Timing | Reviewers | Scores against |
|---|---|---|---|
| Pink | ~20–40% | Writers, capture lead, SMEs | Structure and themes vs requirements/criteria mapping |
| Red | ~80–90% | **External to the writing team**, acting as the evaluation panel | Evaluation factors (rubric) |
| Gold | 100%, 1–2 days before submission | Leadership, contracts, pricing | Compliance, pricing, final polish |

In practice, the compliance matrix ties comments to specific requirements at every stage.

## Why it matters for adapt-rfp

The planned "adversarial LLM pass" in M7 is a red team. The practice suggests design rules that general LLM-judge advice often skips:

1. **Independence.** Red-teamers did not write the proposal. For an LLM: a separate call or agent whose context holds only the solicitation model (M5) and the draft. No library, no drafting conversation, no author intent.
2. **Score with the funder's instrument.** Use the actual rubric bands (EHCRP High/Medium/Low descriptors and points), not a generic quality scale.
3. **Evidence-cited findings.** Every score cites the draft span that earns it, or states the missing evidence ("no community voice quoted").
4. **Several perspectives, then reconcile.** Granted AI's "Review Board" (independent review → deliberation → consensus) is a commercial version. Personas could include program officer, community reviewer, technical reviewer, and budget reviewer.
5. **Staging.** Cheap structural checks (pink) come before expensive judgment (red), and deterministic gates (gold) come last so late edits get re-checked.

## How it would fit

```
check-draft --stage pink  -> coverage: every matrix row has a planned location; word budgets per section
check-draft --stage red   -> N reviewer personas x rubric; JSON {row_id, band, score, evidence_spans[], missing[]}
check-draft --stage gold  -> limits, acronyms, entities, leakage, fact resolution, budget %, AI-use rule
```

Results update the compliance matrix `status` column ([compliance matrix](compliance-matrix.md)). An M8 skill wraps each stage. Humans still run a real red team for high-stakes bids. The LLM version is a rehearsal.

## Strengths

- Decades of practice; the vocabulary is familiar to agency partners.
- Gives the LLM judge a principled role and inputs instead of "make this better".

## Weaknesses / risks

- LLM reviewers share the drafter's blind spots and tend to be lenient. Calibrate them against past scored applications if any exist (DR-0002 open question on past proposals).
- Full color-team ceremony is heavy for a small team. Use lightweight, automatable versions.

## Verdict rationale

**Adopt**: this directly shapes M7's architecture and costs nothing but design discipline.

Up: [Proposal management practice](proposal-management-practice.md)
