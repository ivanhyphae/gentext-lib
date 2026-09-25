---
title: Analytic rubric judging (G-Eval / Prometheus style)
slug: rubric-judging
level: 3
parent: index.md
related: [judge-reliability.md, panel-simulation.md, pairwise-comparison.md, deepeval.md, claude-structured-outputs.md]
tags: [llm-as-judge, rubric, pointwise, g-eval, prometheus]
status: draft
updated: 2026-09-25
kind: technique
verdict: adopt
fit: [M5, M7]
license: n/a (technique)
maturity: mature
inspectability: high
sources:
  - title: "G-Eval: NLG Evaluation using GPT-4 with Better Human Alignment (Liu et al., 2023)"
    url: https://arxiv.org/abs/2303.16634
    accessed: 2026-09-25
  - title: "Prometheus 2: An Open Source Language Model Specialized in Evaluating Other Language Models (Kim et al., 2024)"
    url: https://arxiv.org/abs/2405.01535
    accessed: 2026-09-25
  - title: UK AISI Autonomous Systems Evaluation Standard (Scoring)
    url: https://ukgovernmentbeis.github.io/as-evaluation-standard/
    accessed: 2026-09-25
  - title: "Claude docs: Define success criteria and build evaluations"
    url: https://platform.claude.com/docs/en/test-and-evaluate/develop-tests
    accessed: 2026-09-25
---

# Analytic rubric judging (G-Eval / Prometheus style)

> **TL;DR** Pointwise grading of one draft against an explicit rubric: the judge reasons over named criteria and fills a form. **Adopt**, with one change from G-Eval and Prometheus: split the funder's band descriptors into binary or ternary checklist items with stable ids, and require a quote for each item before any band or points.

## What it is

- **G-Eval**: the judge gets criteria, generates evaluation steps (chain of thought), then fills a form score. It reported Spearman 0.514 with humans on summarisation, a large gain over BLEU/ROUGE-era metrics ([arXiv 2303.16634](https://arxiv.org/abs/2303.16634)).
- **Prometheus / Prometheus 2**: open evaluator LMs trained to grade against a *user-supplied* score rubric, in both direct-assessment and pairwise formats ([arXiv 2405.01535](https://arxiv.org/abs/2405.01535)). The lasting idea is that the rubric is an input, not something baked into the judge.

## Why it matters for adapt-rfp

EHCRP Appendix F already *is* an analytic rubric. Each question has points, three bands with point ranges, and descriptors that name evidence types. HR Q1 High wants "community voices… quotes or stories", and Medium penalises "broad terms that could apply to many communities". M5 already plans to extract these "evidence expectations". Rubric judging is the step that turns them into a check.

## How it would fit

- **M5** stores `questions[].bands[].items[]`, each with `id`, `text` (copied or paraphrased from the descriptor), `kind` (`presence | quality | negative`), and `source_span` (the page/line in the solicitation). A human verifies them once.
- **M7** judge call. Input: question prompt, items, draft (sentence-numbered), relevant facts. Output (structured): per item `{status: met|partial|absent, quote, sentence_ids, note}`, then `band`, then `points_range`.
- Points come *from* the band, e.g. "Medium, 3–4". Don't ask for a free 1–100 number. AISI discourages numeric rating by models ([AISI](https://ukgovernmentbeis.github.io/as-evaluation-standard/)). Anthropic's eval guide likewise prefers constrained outputs (yes/no, fixed classes, short ordinal scales) with a detailed rubric ([Claude docs](https://platform.claude.com/docs/en/test-and-evaluate/develop-tests)).

## Strengths

- Direct traceability: finding → item id → descriptor → page in the solicitation.
- Fits the funder's own mental model, so reviewers and writers read the same language.
- Cheap: one call per question per persona, with the rubric in a cached prefix.
- Works without a reference answer, which we rarely have.

## Weaknesses / risks

- Holistic bands still invite halo effects. Checklist items mitigate this but don't remove it.
- Item extraction is itself an LLM-assisted step that can drift from the descriptor, so human verification in M5 is mandatory.
- Quality-type items ("compelling rationale") stay subjective. Calibrate them before showing them (see [judge-reliability](judge-reliability.md)).
- G-Eval's probability-weighted scoring uses token log-probabilities. We don't rely on that, and whether the current Claude API exposes logprobs is *(unverified)*. The form-filling part is what we take.

## Verdict rationale

This is the backbone of every LLM pass in M7: [panel](panel-simulation.md), [skeptic](adversarial-review-pass.md), and [pairwise](pairwise-comparison.md) all reuse the same item ids. It is high on inspectability because every judgement is a quote plus an item id. Prometheus as a model is **hold**: we'd have to self-host it, and Claude is our judge. Its rubric-as-input format is adopted.

Parent: [LLM evaluation](index.md)
