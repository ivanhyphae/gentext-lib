---
title: Measuring AI "slop" (Shaib et al. 2025)
slug: s-slop-measurement
level: 3
parent: index.md
related: [ai-slop.md, span-feedback-schema.md, s-edit-based-rewards-lamp.md, m-genericness.md, m-readability-sophistication.md, ../llm-evaluation/adversarial-review-pass.md]
tags: [ai-slop, taxonomy, span-annotation, density, templatedness]
status: draft
updated: 2026-09-25
kind: technique
verdict: adopt
fit: [M4, M7]
license: paper arXiv (non-exclusive); diversity package Apache-2.0; cshaib/slop repo MIT (placeholder)
maturity: emerging
inspectability: high
sources:
  - title: Shaib, Chakrabarty, Garcia-Olano, Wallace. Measuring AI "Slop" in Text (arXiv 2509.19163, v2 2026-01-24)
    url: https://arxiv.org/html/2509.19163v2
    accessed: 2026-09-25
  - title: cshaib/slop repository (MIT; README says "Coming soon")
    url: https://github.com/cshaib/slop
    accessed: 2026-09-25
  - title: cshaib/diversity package (compression ratio, templates-per-token; Apache-2.0)
    url: https://github.com/cshaib/diversity
    accessed: 2026-09-25
---

# Measuring AI "slop" (Shaib et al. 2025)

> **TL;DR** **Adopt the taxonomy and the lesson, not a score.** Shaib et al. split "slop" into three themes and seven codes: *information utility* (density, relevance), *information quality* (factuality, bias/subjectivity) and *style quality* (structure, coherence, tone). Expert annotators agree on the *spans* more than on a binary "this is slop" label. Cheap metrics give only a modest signal (AUPRC about 0.52–0.55), and zero-shot LLMs, GPT-5 included, were close to useless at the binary call. The consequence for us is to report per-code, per-span findings and never a single slop verdict.

## What it is

The authors interviewed experts in NLP, writing and philosophy, then had three professional copy-editors annotate word-level spans in 150 news articles and 100 MS MARCO QA passages. They then tested which automatic measures track each code.

| Theme | Code | Automatic proxy they tested |
|---|---|---|
| Information utility | Density (little substance for the length) | token entropy (GPT-2), propositional idea density |
| | Relevance (off-task) | none reliable |
| Information quality | Factuality | human annotation needed |
| | Bias / subjectivity | subjectivity lexicon (Wiebe 2004) |
| Style quality | Structure: repetition, templatedness | lexical and POS compression ratio, templates-per-token |
| | Coherence | human annotation needed |
| | Tone: verbosity, word complexity, formality, fluency | word/sentence counts, Gunning-Fog, Flesch-Kincaid |

## Key numbers (from the v2 HTML, accessed 2026-09-25)

- Agreement on binary slop labels was poor (κ −0.15 to 0.29; AC1 0.12–0.42). Span-level precision between annotators was 0.65–0.80, and theme-level Krippendorff's α_MASI was 0.34–0.45.
- A linear model over the proxies reached AUPRC 0.52 (news) and 0.55 (QA). That is some signal above the prevalence baseline, but not much.
- Zero-shot LLM binary slop prediction had κ ≈ 0 (GPT-5, DeepSeek-V3, o3-mini), with recall 0.08–0.12. Zero-shot span extraction reached character-level precision of only 0.13–0.16. A fine-tuned Qwen-7B got span F1 0.26–0.30.
- The WQRM writing-quality reward model ([card](s-edit-based-rewards-lamp.md)) correlated weakly with slop labels (0.25 news, 0.15 QA).
- What counts as slop depends on the domain. News annotators weighted coherence, tone, density and relevance. QA annotators weighted factuality and structure.

## Why it matters for adapt-rfp

- It supplies the **top level of our category tree** in the [span-feedback schema](span-feedback-schema.md). "Density", "relevance" and "structure/templatedness" are exactly the maintainer's "generic" and "AI slop" complaints, split into parts Claude can act on.
- It is a warning against prompting Claude with "is this slop? yes/no". Frontier models fail that task. Findings have to be scoped to one code, anchored to a quote and checked by a validator, which is the *witness* pattern from [llm-evaluation](../llm-evaluation/index.md).
- Two proxies are cheap to compute and suit proposals: **templates-per-token / POS compression ratio** for sentence-shape monotony, from the `diversity` package, and **idea density** for filler. Both should be normed against the firm corpus ([norming](m-norming-presentation.md)), not read raw.

## How it would fit

- M4 computes the per-paragraph proxies (density, templatedness, verbosity) and emits `statistical` findings.
- The M7 LLM annotator gets one code at a time ("mark low-density spans") with a guideline and examples ([LLM span annotation](s-llm-span-annotation.md)).
- Relevance maps onto M5: is the span responsive to the question prompt? Factuality maps onto [claim verification](../llm-evaluation/claim-verification.md).

## Strengths

- An expert-derived, interpretable, multi-dimensional definition. It is the first careful one we found.
- It gives honest negative results on LLM detection. That is rare and useful.

## Weaknesses / risks

- The domains are news and QA, not grant narrative. Proposals *require* some things that look like slop elsewhere, such as funder vocabulary and restating the prompt.
- No released code or annotations yet. The `cshaib/slop` repo contained only a README on 2026-09-25. We did not run the `diversity` metrics in this pass *(not probed)*.
- The disagreement result cuts both ways. A human "slop" label on our drafts will also be noisy, so the calibration set needs two raters.

## Verdict rationale

Adopt as taxonomy and as a design constraint (per-code, span-first). The metrics themselves are trial-grade inputs, and nothing in the paper supports a composite "slop score".

Parent: [Prose signals](index.md) · Up: [AI slop](ai-slop.md)
