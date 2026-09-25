---
title: Perplexity and surprisal with a small local LM
slug: m-perplexity
level: 3
parent: index.md
related: [holistic-metrics.md, m-genericness.md, a-ai-detection-apis.md, ../nlp-quality/stylometry-ai-detection.md]
tags: [perplexity, surprisal, burstiness, language-model, ai-detection]
status: draft
updated: 2026-09-25
kind: technique
verdict: assess
fit: [M4, M7]
license: GPT-2 MIT (modified); Qwen2.5-0.5B Apache-2.0; Binoculars code (license unverified)
maturity: mature
inspectability: medium
sources:
  - title: Qwen/Qwen2.5-0.5B model card (Apache-2.0, 0.49B params)
    url: https://huggingface.co/Qwen/Qwen2.5-0.5B
    accessed: 2026-09-25
  - title: Hans et al. (2024), Spotting LLMs with Binoculars (ICML; arXiv 2401.12070)
    url: https://arxiv.org/abs/2401.12070
    accessed: 2026-09-25
  - title: ahans30/Binoculars (reference implementation, Falcon-7B pair)
    url: https://github.com/ahans30/Binoculars
    accessed: 2026-09-25
  - title: Shaib et al. (2025), Measuring AI "Slop" in Text (arXiv 2509.19163)
    url: https://arxiv.org/abs/2509.19163
    accessed: 2026-09-25
  - title: Holtzman et al. (2020), The Curious Case of Neural Text Degeneration (arXiv 1904.09751)
    url: https://arxiv.org/abs/1904.09751
    accessed: 2026-09-25
  - title: Liang et al. (2023), GPT detectors are biased against non-native English writers (arXiv 2304.02819; Patterns)
    url: https://arxiv.org/abs/2304.02819
    accessed: 2026-09-25
---

# Perplexity and surprisal

> **TL;DR** **Assess.** A small local LM (Qwen2.5-0.5B, Apache-2.0, CPU) gives per-token **surprisal**. Summarized, it says how *predictable* a text is. Very low perplexity with low surprisal variance ("flat" text) is a real hint of stock phrasing and templated prose. It is also the signature of simple, 4th-grade text, and of non-native writing that detectors mis-flag. Very high perplexity marks broken or telegraphic text (notes, fragments, heavy errors). It is useful as a **span locator** (the most predictable run of sentences). It is not a quality score and not an AI detector.

## What it is

Perplexity = exp(mean negative log-likelihood per token) under a reference LM. **Burstiness** is the spread of surprisal across tokens or sentences. Human prose mixes predictable and surprising stretches, while stock prose stays flat. **Binoculars** (Hans et al. 2024) normalizes one model's perplexity by the cross-perplexity between two related models, and is the strongest zero-shot detector of this family. It needs a 7B model pair, and the "AI or not" framing doesn't match our goals ([hold rationale](../nlp-quality/stylometry-ai-detection.md)).

## Probe on the pilot (2026-09-25, CPU, <5 s per paragraph)

| Sample | PPL GPT-2 | PPL Qwen2.5-0.5B | Surprisal SD (Qwen) |
|---|---|---|---|
| Pilot narratives (4 paragraphs) | 38–57 | 19–29 | 2.83–3.09 |
| Firm project descriptions | 69 | 50 | 3.18 |
| Firm boilerplate | 43 | 25 | 3.03 |
| Meeting summary (notes register) | 109 | 67 | 3.34 |
| Synthetic "AI slop" | **25** | **12.5** | **2.42** |
| Synthetic 4th-grade | **19** | **11.0** | **2.18** |
| Synthetic ungrammatical | **147** | 66 | 2.83 |

Readings: slop and simple text are both the most predictable, so perplexity alone cannot tell "generic" from "plain". The concreteness and grade signals disambiguate them (slop: grade 16, concreteness 2.7; 4th-grade: grade 0, concreteness 3.4). Specific project prose, dense with names and numbers, has the *highest* perplexity among fluent texts. Surprise there is information, not error. The two models rank the samples identically, so the cheaper one is enough for ranking.

## Granularity and reliability

Token-level values are available, so compute sentence means and flag the **lowest-surprisal runs** as "stock phrasing candidates". At 250 words (about 330 tokens) the document mean is stable enough to rank paragraphs within one draft. Comparisons **across genres or models** are meaningless, so norm against the firm corpus scored with the same model. Holtzman et al. show that maximum-likelihood text is repetitive and bland, which supports reading low perplexity as a caution, not a virtue.

## How it would fit

M4 caches per-sentence surprisal with a pinned model id. M7 reports `paragraph 2: predictability p95 vs firm corpus; flattest sentences S3–S5` next to concreteness. The combination drives the finding. Perplexity never appears alone.

## Weaknesses / risks

- Confounded by simplicity, list structure, repeated proper nouns, and the writer's language background (Liang et al. 2023). Using it to attribute authorship would be both unfair and wrong.
- Shaib et al. (2025) found automatic slop proxies, surprisal included, weak predictors of human slop judgments: linear models reached AUPRC ≈ 0.52–0.55.
- Model-specific: changing the model changes every norm.

## Verdict rationale

Cheap and locally runnable, and it gives a genuinely orthogonal "predictability" axis with span localization. The evidence says it is a weak proxy, so assess it inside the panel, not as a gate.

Parent: [Prose signals](index.md) · Up: [Holistic metrics](holistic-metrics.md)
