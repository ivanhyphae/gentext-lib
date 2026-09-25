---
title: Reviewer-panel simulation
slug: panel-simulation
level: 3
parent: index.md
related: [rubric-judging.md, adversarial-review-pass.md, judge-reliability.md, multi-agent-debate.md]
tags: [llm-as-judge, personas, review-panel, grant-review]
status: draft
updated: 2026-09-25
kind: technique
verdict: trial
fit: [M5, M7]
license: n/a (technique)
maturity: emerging
inspectability: high
sources:
  - title: "Evaluating LLM-Based Grant Proposal Review via Structured Perturbations (Thorne et al., 2026)"
    url: https://arxiv.org/abs/2603.08281
    accessed: 2026-09-25
  - title: "Evaluating large language models as grant reviewers (Frontiers in Education, 2026)"
    url: https://www.frontiersin.org/journals/education/articles/10.3389/feduc.2026.1856134/full
    accessed: 2026-09-25
  - title: "How Closely Do LLM Reviews Align with Human Peer Review? (2026)"
    url: https://arxiv.org/abs/2608.03659
    accessed: 2026-09-25
---

# Reviewer-panel simulation

> **TL;DR** Two or three reviewer personas each score a narrative answer against the funder's actual rubric, with quotes, in separate contexts. Disagreement between them is the signal. **Trial** it with a small panel, run per question and per checklist item. A 2026 study found a "Council of Personas" ensemble *worse* than plain section-by-section review. The personas widen what gets noticed, not how accurate the score is.

## What it is

Role-conditioned LLM judges stand in for an expert review panel. EHCRP applications go to an "Interagency Panel Review" scored with Appendix F, and top applicants get an interview that assesses alignment with the program's four values (Guidelines §8.5, local copy). A simulated panel previews how different reviewer priorities read the same 250 words.

## Proposed EHCRP panel (fictional roles, no real people)

| Persona | Weighs | Typical catch |
|---|---|---|
| **Program-compliance reviewer** | Does the answer address every part of the prompt and every High item? | "Prompt asks *how you know*; no source of lived experience given" |
| **Community / equity reviewer** | Harm Reduction and Belonging; presence and authenticity of community voice | "Data present, voices absent; reads as outsider description" |
| **Infrastructure-delivery reviewer** | Feasibility, sequencing within 30 months, partner capacity | "Pathway from shade structure to reduced exposure is asserted, not explained" |

Every persona gets the **same** checklist items ([rubric-judging](rubric-judging.md)). The persona only changes emphasis and the notes it writes, never the rubric. Scores roll up as the median band. Items where personas disagree by a full band go into a "contested" list for humans.

## Why it matters for gentext

Writers ask "how will the panel read this?" A panel output grouped by rubric item shows unanimous gaps first (e.g. "Voices: absent, 3/3") and contested items second. That report is more actionable than one score and more honest about uncertainty.

## How it would fit

- M7 stage 2 of the [adversarial pass](adversarial-review-pass.md). Persona prompts are versioned files in `skills/check-draft/references/personas/`, a planned path.
- Each persona's output uses the same JSON schema, validated deterministically (quote exists, item id exists).
- The run record stores persona prompt hashes, so a change in panel behaviour can be traced to a prompt edit.

## Strengths

- Surfaces different blind spots at low cost: three calls with a shared cached prefix.
- Its disagreement estimates judge uncertainty better than one sampled score.
- Mirrors the funder's actual process, so the output is legible to writers.

## Weaknesses / risks

- **Personas don't add accuracy.** On EPSRC proposals, section-by-section analysis beat a "Council of Personas". Feedback skewed toward compliance checking, and clarity problems were largely missed ([arXiv 2603.08281](https://arxiv.org/abs/2603.08281)).
- **Score compression and optimism.** Zero-shot LLM reviewers inflated scores and narrowed the spread, and funding recommendations were at or below chance ([Frontiers 2026](https://www.frontiersin.org/journals/education/articles/10.3389/feduc.2026.1856134/full)). Report bands and gaps, never a "predicted award score".
- Coarse alignment can coexist with fine misalignment: models separated accept from reject but not finer tiers ([arXiv 2608.03659](https://arxiv.org/abs/2608.03659)).
- Persona caricature. An "equity reviewer" prompt can drift into stereotyped demands. Keep personas anchored to rubric text.

## Verdict rationale

**Trial.** The value is in structured, quoted, per-item feedback with a disagreement signal. Keep the panel small, run it per question, and never present its numbers as a forecast.

Parent: [LLM evaluation](index.md)
