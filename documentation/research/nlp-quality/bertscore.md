---
title: BERTScore
slug: bertscore
level: 3
parent: index.md
related: [embeddings-and-similarity.md, nli-claim-support.md, sentence-embeddings.md]
tags: [similarity, reference-based-metric, evaluation]
status: draft
updated: 2026-09-25
kind: algorithm
verdict: hold
fit: [M4]
license: MIT
maturity: legacy
inspectability: medium
sources:
  - title: Zhang et al. (2020), BERTScore, Evaluating Text Generation with BERT, ICLR
    url: https://arxiv.org/abs/1904.09675
    accessed: 2026-09-25
  - title: Tiiiger/bert_score GitHub repository (MIT; last push 2024-07)
    url: https://github.com/Tiiiger/bert_score
    accessed: 2026-09-25
  - title: bert-score on PyPI (0.3.13, 2023-02-20)
    url: https://pypi.org/project/bert-score/
    accessed: 2026-09-25
---

# BERTScore

> **TL;DR** **Hold.** BERTScore compares a candidate text to a *reference* by greedily matching contextual token embeddings, and reports precision, recall, and F1. gentext rarely has a gold reference, and plain sentence embeddings or MinHash answer our similarity questions more simply. The package has had no release since 2023.

## What it is

A reference-based generation metric (Zhang et al., ICLR 2020). Each candidate token is matched to its most similar reference token (cosine over BERT-family contextual embeddings), with optional IDF weighting and baseline rescaling. Output: P (candidate supported by reference), R (reference covered by candidate), and F1. MIT-licensed. PyPI 0.3.13 was released 2023-02, and the last repo push was 2024-07.

## Why it might matter for gentext

The one plausible use is **variant fidelity**: when a "SHORTENED" variant is made from a long chunk, BERTScore *precision* (short vs long as reference) estimates whether the short version adds content that isn't in the source. Recall estimates how much it drops. Token-level alignments can be visualized, which is somewhat inspectable.

## Why hold

- **Better tools exist for each question.** Literal reuse → [MinHash containment](minhash-lsh.md). Semantic closeness → [sentence embeddings](sentence-embeddings.md). "Is the short version still faithful?" → [NLI/MiniCheck](nli-claim-support.md), which targets support directly.
- Scores need rescaling to be interpretable, and they differ across backbone models.
- Maintenance is quiet, and its model defaults (roberta-large layer choices) are dated.

## Revisit if

We build a regression eval where human-edited "gold" answers exist (M9 harvest gives us edited versions), and want an automatic "how far did the draft move from the final" metric. Even then, embedding cosine plus a diff is probably enough.

Parent: [NLP quality checks](index.md)
