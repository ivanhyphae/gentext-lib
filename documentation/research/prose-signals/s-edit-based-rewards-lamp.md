---
title: Edit-based writing rewards (LAMP corpus, WQRM)
slug: s-edit-based-rewards-lamp
level: 3
parent: index.md
related: [ai-slop.md, span-feedback-schema.md, s-slop-measurement.md, s-writing-critic-models.md, a-minor-and-discontinued.md, ../llm-evaluation/critic-reviser-loop.md]
tags: [ai-slop, reward-model, expert-edits, taxonomy, lamp, wqrm]
status: draft
updated: 2026-09-25
kind: technique
verdict: adopt
fit: [M4, M7]
license: LAMP data CC BY 4.0 (per paper); creativity_eval repo BSD-3-Clause (archived 2026-06-25); WQRM weights MIT
maturity: emerging
inspectability: medium
sources:
  - title: Chakrabarty, Laban, Wu. Can AI writing be salvaged? Mitigating Idiosyncrasies and Improving Human-AI Alignment in the Writing Process through Edits (CHI 2025; arXiv 2409.14509)
    url: https://arxiv.org/html/2409.14509v5
    accessed: 2026-09-25
  - title: Chakrabarty, Laban, Wu. AI-Slop to AI-Polish? Aligning Language Models through Edit-Based Writing Rewards and Test-time Computation (arXiv 2504.07532)
    url: https://arxiv.org/html/2504.07532v1
    accessed: 2026-09-25
  - title: salesforce/creativity_eval (Writing_Alignment, WritingRewards; archived)
    url: https://github.com/salesforce/creativity_eval
    accessed: 2026-09-25
  - title: Salesforce/WQRM and Salesforce/WQRM-PRE model cards (MIT, ModernBERT-large)
    url: https://huggingface.co/Salesforce/WQRM
    accessed: 2026-09-25
  - title: WQRM inference script
    url: https://github.com/salesforce/creativity_eval/blob/main/WritingRewards/WQRM_inference.py
    accessed: 2026-09-25
---

# Edit-based writing rewards (LAMP corpus, WQRM)

> **TL;DR** **Adopt the LAMP idiosyncrasy taxonomy and its edit format. Trial WQRM as an advisory paragraph score.** Professional writers edited LLM paragraphs, and each edit is a span with a category and a rewrite: cliché, unnecessary exposition, purple prose, poor sentence structure, lack of specificity, awkward word choice, tense inconsistency. That record is the shape Claude needs for revision. WQRM, an MIT ModernBERT scorer trained on those edits, ran locally on our pilot in seconds. It ranked a synthetic slop paragraph lowest, but it was trained on creative writing, so treat it as a trend line, not a judge.

## What it is

**LAMP** (Language model Authored, Manually Polished), from CHI 2025: 18 MFA-trained writers edited 1,057 LLM paragraphs from GPT-4o, Claude 3.5 Sonnet and Llama 3.1 70B, producing 8,035 span-level edits. Each edit is *(span, category, rewrite)*. The seven categories and their share of edits:

| Category | Share | Proposal-prose analogue |
|---|---|---|
| Awkward word choice and phrasing | 28% | nominalizations, vague pronouns, jargon strings |
| Poor sentence structure | 20% | stacked clauses, weak transitions |
| Unnecessary / redundant exposition | 18% | restating the prompt, "this project will…" wind-ups |
| Cliché | 17% | "at a pivotal crossroads", "a testament to" |
| Lack of specificity and detail | (rest) | the funder's "could apply to many communities" |
| Purple prose | (rest) | "vibrant tapestry of shade and belonging" |
| Tense inconsistency | (rest) | mixing "will plant" with "planted" |

Findings from that paper: no model family wrote better than the others. Few-shot LLM detection of problem spans reached 0.46 precision, against 0.57 agreement between experts, but only 0.20 when the category also had to match. Human preference ran writer-edited > LLM-edited > raw LLM output.

**WQRM** (arXiv 2504.07532). The *Writing Quality* benchmark pools 4,729 judgments. GPT-4o scored 40.9% on it (random is 50%), while the edit-trained ModernBERT-large **WQRM** reached 74.3%. The paper's pipeline is: *detect problem spans → rewrite → apply edits*, then generate 20 candidates and pick the best by WQRM. Experts agreed with WQRM's pick 66% of the time, rising to 72.2% when the reward gap was over 1 point.

## Hands-on probe (2026-09-25, local, RTX 5000, `Salesforce/WQRM-PRE`)

We scored 11 paragraphs (90–220 words) from the two pilot DOCX files, plus two synthetic paragraphs we wrote: a buzzword-dense "slop" version and a concrete rewrite. Scores are on a 0–10 scale.

| Text | WQRM | AI-vocab per 100 words |
|---|---|---|
| Pilot paragraphs (n=11) | mean 6.86, sd 0.97, range 5.32–8.49 | 0–2.8 |
| Synthetic slop | **4.32** | 18.7 |
| Synthetic concrete rewrite | 6.68 | 0 |

Pairwise mode also preferred the rewrite. The model loads in seconds and runs well under a second per paragraph on the GPU, and CPU should also work since it is about 400M parameters *(CPU speed not measured)*. The model card says to score paragraph by paragraph and average for longer text. n is tiny. This is a sanity check, not a validation.

## How it would fit

- **Taxonomy**: the LAMP categories become the `style.*` and `slop.*` leaves in the [span-feedback schema](span-feedback-schema.md). The edit triple *(span, category, rewrite)* is the schema's core.
- **WQRM**: an M4 `statistical` detector that emits one paragraph-level finding with `evidence.metric: wqrm`, normed as a percentile against the firm corpus. It can also act as a *tie-breaker* between candidate rewrites in a bounded [critic-reviser loop](../llm-evaluation/critic-reviser-loop.md), never as the stop criterion.
- **Gold data**: LAMP's CC BY data can seed few-shot examples for the LLM annotator's categories.

## Strengths

- The data is expert edits, not preferences, so it teaches *what to change*.
- The weights are small, open and MIT-licensed, run locally, and support both pairwise and scalar scoring.

## Weaknesses / risks

- The domain is literary and creative nonfiction. Proposal virtues such as funder terms, compliance restatement and numbers may be scored as flaws *(untested)*. Shaib et al. found WQRM correlates only weakly with slop labels in news and QA (0.15–0.25).
- Goodhart risk: optimizing to WQRM invites style drift. It never overrides facts or rubric fit.
- The repo is archived, so there will be no upstream fixes. The research-only disclaimer is on the card, but the license is MIT.

## Verdict rationale

The taxonomy and edit format are exactly what span-feedback needs, so adopt them. WQRM is a cheap, inspectable second signal. Trial it, report it as a percentile, keep it advisory.

Parent: [Prose signals](index.md) · Up: [AI slop](ai-slop.md)
