---
title: Pairwise comparison judging
slug: pairwise-comparison
level: 3
parent: index.md
related: [rubric-judging.md, judge-reliability.md, promptfoo.md]
tags: [llm-as-judge, pairwise, position-bias, variant-selection]
status: draft
updated: 2026-09-25
kind: technique
verdict: trial
fit: [M6, M7]
license: n/a (technique)
maturity: mature
inspectability: medium
sources:
  - title: "Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena (Zheng et al., 2023)"
    url: https://arxiv.org/abs/2306.05685
    accessed: 2026-09-25
  - title: "Large Language Models are not Fair Evaluators (Wang et al., 2023)"
    url: https://arxiv.org/abs/2305.17926
    accessed: 2026-09-25
  - title: "Prometheus 2 (Kim et al., 2024)"
    url: https://arxiv.org/abs/2405.01535
    accessed: 2026-09-25
  - title: "promptfoo model-graded metrics (select-best)"
    url: https://www.promptfoo.dev/docs/configuration/expected-outputs/model-graded/
    accessed: 2026-09-25
---

# Pairwise comparison judging

> **TL;DR** Show the judge two drafts and ask which better satisfies a named rubric item. Relative judgements are usually easier and more stable than absolute ones, but they carry strong position bias. **Trial** it only for choosing between M6 variants, for example two assemblies of the HR Q1 answer. Always run both orders, and count disagreement between orders as a tie.

## What it is

Pairwise (A vs B) is the Chatbot Arena and MT-Bench format ([arXiv 2306.05685](https://arxiv.org/abs/2306.05685)). The alternative is pointwise: one output scored against a rubric ([rubric-judging](rubric-judging.md)). Prometheus 2 trains a single evaluator for both modes ([arXiv 2405.01535](https://arxiv.org/abs/2405.01535)). promptfoo's `select-best` assertion does this across prompt or provider outputs ([docs](https://www.promptfoo.dev/docs/configuration/expected-outputs/model-graded/)).

## Why it matters for gentext

M6 will often produce several candidates for one question: different chunk selections, the long variant versus the SHORTENED one, or different partner framings. Writers need to know *which is closer to High on item X*, not an absolute score. Pairwise answers that question directly.

## How it would fit

- `gentext compare draftA draftB --question EHCRP-R2/HR-Q1 --items voices,not-generic`
- For each item, run A|B, then B|A. Record `winner`, with the quote from each side supporting the decision.
- Aggregate: win if both orders agree, tie otherwise. This is Wang et al.'s *balanced position calibration* ([arXiv 2305.17926](https://arxiv.org/abs/2305.17926)).
- Only compare drafts **of equal length**. Word limits make this natural and neutralise verbosity bias.
- For more than two candidates, use a round-robin within a small set. We don't need Elo.

## Strengths

- More discriminating than pointwise when both drafts land in the same band.
- Easy for humans to verify ("I agree B is more specific about bus-stop exposure").
- Works well as a regression test after a prompt or model change: the old best versus the new output.

## Weaknesses / risks

- **Position bias** is well documented. GPT-4 favoured the first candidate, and others favour the second ([arXiv 2305.17926](https://arxiv.org/abs/2305.17926)). Swapping doubles the cost.
- Preferences aren't calibrated. "B beats A" says nothing about whether either is High.
- Non-transitive results appear with more than three candidates.
- **Self-preference** is sharper when one candidate was written by the judge's own model family ([judge-reliability](judge-reliability.md)).

## Verdict rationale

It's useful and cheap for variant selection, but pointwise checklist grading remains the reporting unit because it maps to the funder's bands. **Trial** it in the pilot once M6 emits two or more candidates.

Parent: [LLM evaluation](index.md)
