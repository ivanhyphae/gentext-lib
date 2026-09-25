---
title: Specificity and concreteness (concreteness norms, anchor density, specificity models)
slug: m-specificity-concreteness
level: 3
parent: index.md
related: [holistic-metrics.md, m-genericness.md, m-readability-sophistication.md, ../nlp-quality/spacy-rule-matching.md, ../nlp-quality/hedge-booster-lexicon.md]
tags: [specificity, concreteness, named-entities, genericness, span-level]
status: draft
updated: 2026-09-25
kind: technique
verdict: adopt
fit: [M4, M7]
license: Brysbaert norms CC BY 4.0 (via NORARE); spaCy MIT; Speciteller and Ko et al. repos no license stated
maturity: mature
inspectability: high
sources:
  - title: Brysbaert, Warriner & Kuperman (2014), Concreteness ratings for 40 thousand generally known English word lemmas (Behavior Research Methods)
    url: https://link.springer.com/article/10.3758/s13428-013-0403-5
    accessed: 2026-09-25
  - title: NORARE, Brysbaert 2014 Concreteness dataset (CC BY 4.0)
    url: https://norare.clld.org/contributions/Brysbaert-2014-Concreteness
    accessed: 2026-09-25
  - title: ArtsEngine/concreteness (plain-text copy of the ratings)
    url: https://github.com/ArtsEngine/concreteness
    accessed: 2026-09-25
  - title: Li & Nenkova (2015), Fast and Accurate Prediction of Sentence Specificity (AAAI); jjessyli/speciteller (Python 2.7)
    url: https://github.com/jjessyli/speciteller
    accessed: 2026-09-25
  - title: Ko, Durrett & Li (2019), Domain Agnostic Real-Valued Specificity Prediction (AAAI; arXiv 1811.05085)
    url: https://arxiv.org/abs/1811.05085
    accessed: 2026-09-25
  - title: wjko2/Domain-Agnostic-Sentence-Specificity-Prediction (PyTorch 1.0; train-your-own)
    url: https://github.com/wjko2/Domain-Agnostic-Sentence-Specificity-Prediction
    accessed: 2026-09-25
  - title: Ellinger et al. (2026), Granuscore, a reference-free measure of granularity (arXiv 2605.26620, EMNLP 2026)
    url: https://arxiv.org/abs/2605.26620
    accessed: 2026-09-25
---

# Specificity and concreteness

> **TL;DR** **Adopt** two cheap, span-level measures as the backbone of "this is generic". (1) **Mean concreteness** of content words, from the Brysbaert norms (40k lemmas, CC BY 4.0). (2) **Anchor density**: named places, organizations, people, numbers, dates, and money per sentence, from spaCy plus our M3 registries. A sentence with no anchor and low concreteness is a precise, quotable "generic" finding. Trained specificity predictors (Speciteller, Ko et al. 2019) are the research-grade version, but their code is stale. Hold them as validation references.

## What it is

- **Concreteness norms.** Each word is rated 1 (abstract) to 5 (concrete) by 4,000+ raters: *tree* ≈ 5, *resilience* ≈ 1.5. Averaging over content lemmas gives a paragraph score, and each low-scoring sentence is a span.
- **Anchor density.** The share of sentences that contain at least one checkable particular: a GPE/FAC/ORG/PERSON entity, a number or quantity, a date, or a registry term (project name, partner, site). It is computed from spaCy NER plus the [gazetteer rules](../nlp-quality/spacy-rule-matching.md) we already plan. It also operationalizes the reviewer's question "could this sentence appear in any proposal?"
- **Sentence-specificity models.** Speciteller (Li & Nenkova 2015) scores sentences 0–1 for news text. It is Python 2.7, and performance drops outside news. Ko et al. (2019) adapt to new domains without labels but ship no pretrained model (PyTorch 1.0). Granuscore (2026) measures granularity from hierarchical embeddings and reports signal beyond sentence length. Code availability is *unverified*.

## Probe on the pilot (2026-09-25, local)

| Sample | Mean concreteness | Entities /100 words | Numbers /100 words | Sentences without anchor |
|---|---|---|---|---|
| Firm project descriptions | 3.18 | 4.8 | 0.5 | 50% |
| Pilot narrative paragraphs | 3.07–3.23 | 3.8–5.9 | 0.9–5.2 | 0–33% |
| Firm boilerplate ("extensive experience…") | **2.71** | 6.9 | 0.0 | 33% |
| Synthetic "AI slop" | **2.70** | **0.0** | 1.6 | **71%** |
| Synthetic 4th-grade | 3.42 | 0.0 | 2.6 | 91% |

Findings: concreteness separates boilerplate and slop (≈2.7) from grounded project prose (≈3.1–3.2) by about 0.4 points, at paragraph level. Anchor density catches the slop sample (no entities at all). The firm boilerplate *does* name organizations, so anchors alone would pass it. It needs the concreteness and [genericness](m-genericness.md) checks. The 4th-grade sample is concrete but unanchored: simple, not generic. That is why the panel reads these axes together.

## Granularity and short-text reliability

Both measures work per sentence and are stable at paragraph level (≈10 sentences). A per-sentence concreteness mean over five content words is noisy. Flag a sentence only when it is both unanchored **and** below the reference corpus's 20th percentile for concreteness.

## How it would fit

- M4 stores per-sentence `concreteness`, `anchors[]`, and `anchored: bool`.
- M7 emits findings like `S4 unanchored, concreteness 2.3 (p8 vs firm corpus): name the site, the partner, or a number`. The fix hint points Claude at M3 facts for the target place, which also serves the no-invention rule (a missing fact becomes a `[[NEEDS SOURCE]]` placeholder).
- Numbers found here feed the fact-provenance check (every number resolves to M3).

## Weaknesses / risks

- The norms cover general vocabulary. Domain terms (*UTCI*, *bioswale*) may be missing or rated oddly. Add a small domain override list.
- Anchoring is not truth: a wrong place name is anchored. Context-leakage checks remain separate.
- Rewards name-dropping. Report anchors per sentence, not as a score to maximize.

## Verdict rationale

Deterministic, explainable, span-level, and permissively licensed. It directly addresses the most common reviewer complaint about grant prose. Adopt.

Parent: [Prose signals](index.md) · Up: [Holistic metrics](holistic-metrics.md)
