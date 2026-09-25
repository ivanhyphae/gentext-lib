---
title: Open-weight writing critics and reward models (WQRM, WritingBench critic, LitBench RMs, Prometheus 2)
slug: s-writing-critic-models
level: 3
parent: index.md
related: [ai-slop.md, s-edit-based-rewards-lamp.md, span-feedback-schema.md, m-aes-ellipse.md, ../llm-evaluation/index.md]
tags: [reward-model, critic, open-weight, writing-quality]
status: draft
updated: 2026-09-25
kind: library
verdict: trial
fit: [M4, M7]
license: WQRM MIT; WritingBench critic Apache-2.0; LitBench data MIT (models' license unverified); Prometheus 2 (see llm-evaluation)
maturity: experimental
inspectability: medium
sources:
  - title: Salesforce/WQRM model card
    url: https://huggingface.co/Salesforce/WQRM
    accessed: 2026-09-25
  - title: X-PLUG/WritingBench (critic model AQuarterMile/WritingBench-Critic-Model-Qwen-7B, Apache-2.0)
    url: https://github.com/X-PLUG/WritingBench
    accessed: 2026-09-25
  - title: WritingBench, A Comprehensive Benchmark for Generative Writing (arXiv 2503.05244; NeurIPS 2025 D&B)
    url: https://arxiv.org/abs/2503.05244
    accessed: 2026-09-25
  - title: LitBench, A Benchmark and Dataset for Reliable Evaluation of Creative Writing (arXiv 2507.00769)
    url: https://arxiv.org/abs/2507.00769
    accessed: 2026-09-25
---

# Open-weight writing critics and reward models

> **TL;DR** **Trial WQRM only; assess the rest.** The open writing critics are small, local and cheap, but all are trained on **creative or general writing**, and none emits spans. WQRM (MIT, about 400M parameters) is the only one we ran. It separated synthetic slop from a concrete rewrite on the pilot probe ([card](s-edit-based-rewards-lamp.md)). The WritingBench critic (Qwen-7B, Apache-2.0) scores per criterion with a justification. LitBench's reward models beat off-the-shelf judges on Reddit stories. Use one as a paragraph-level `statistical` signal and a tie-breaker between rewrites, never as the judge.

## Options

| Model | Size / base | Output | Trained on | Reported result | License |
|---|---|---|---|---|---|
| **WQRM / WQRM-PRE** | ModernBERT-large (~400M) | scalar 0–10 per paragraph; pairwise preference | LAMP expert edits | 74.3% on WQ benchmark (GPT-4o 40.9%) | MIT |
| **WritingBench critic** | Qwen-7B | 1–10 score + justification **per query-specific criterion** | WritingBench (6 domains, 100 subdomains, incl. business/academic) | 84% human alignment with dynamic criteria (paper) | Apache-2.0 |
| **LitBench RMs** | Bradley-Terry and generative RMs | pairwise preference | 43.8k Reddit story pairs | 78% vs Claude 3.7 Sonnet 73% as judge | data MIT; model license *unverified* |
| **Prometheus 2** | 7B / 8x7B | rubric score + feedback | general feedback data | see [llm-evaluation](../llm-evaluation/index.md) (hold) | *see that page* |

Notes: WritingBench switched its own evaluation to Claude Sonnet 4.5 in November 2025, a hint that the critic lags frontier judges (repo, accessed 2026-09-25). WritingBench includes business and official-document domains, the nearest to proposals, but we did not run the critic *(not probed; a 7B model fits our 16 GB GPU in fp16 only tightly, so it would need quantization)*.

## How it would fit

- M4: `detector.kind: model` findings at **paragraph scope**, normed as a percentile against the firm corpus ([norming](m-norming-presentation.md)), severity `info` unless below p10.
- M7 critic-reviser loop: score N candidate rewrites of a flagged paragraph and show the ranking to Claude as evidence. This is the AI-Polish test-time trick, bounded by fact checks.
- None produces spans, so pair them with the [LLM span annotator](s-llm-span-annotation.md) to say *where*.

## Weaknesses / risks

- Domain shift: literary taste is not proposal taste. The ELLIPSE-style scorers in this folder also hit a ceiling on professional text ([m-aes-ellipse](m-aes-ellipse.md)).
- Goodhart: optimizing a reward model yields reward hacking. Keep them advisory, with facts and rubric fit always taking priority.
- The Salesforce repo is archived, so no maintenance.

## Verdict rationale

Cheap, local and open, and a useful "did the rewrite help?" signal. Trial WQRM now. Revisit WritingBench's critic if a proposal-domain gold set shows WQRM misranks.

Parent: [Prose signals](index.md) · Up: [AI slop](ai-slop.md)
