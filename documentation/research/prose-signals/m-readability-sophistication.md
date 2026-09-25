---
title: Readability, lexical sophistication and diversity (beyond Flesch)
slug: m-readability-sophistication
level: 3
parent: index.md
related: [holistic-metrics.md, m-aes-ellipse.md, m-specificity-concreteness.md, m-norming-presentation.md, ../nlp-quality/readability-descriptives.md]
tags: [readability, lexical-diversity, sophistication, cohesion, syntactic-complexity, cefr]
status: draft
updated: 2026-09-25
kind: technique
verdict: trial
fit: [M4, M7]
license: textstat MIT; lexicalrichness MIT; wordfreq Apache-2.0; LFTK CC BY-NC 4.0; lingfeat CC BY-SA 4.0; TAALES/TAACO/TAASSC/TAALED CC BY-NC-SA 4.0
maturity: mature
inspectability: high
sources:
  - title: McCarthy & Jarvis (2010), MTLD, vocd-D, and HD-D validation study (Behavior Research Methods)
    url: https://www.researchgate.net/publication/44608173_MTLD_vocd-D_and_HD-D_A_validation_study_of_sophisticated_approaches_to_lexical_diversity_assessment
    accessed: 2026-09-25
  - title: Zenker & Kyle (2021), Investigating minimum text lengths for lexical diversity indices (Assessing Writing 47)
    url: https://www.researchgate.net/publication/346623372_Investigating_minimum_text_lengths_for_lexical_diversity_indices
    accessed: 2026-09-25
  - title: NLP Tools for the Social Sciences (TAALES, TAACO, TAASSC, TAALED; licenses)
    url: https://www.linguisticanalysistools.org/taales.html
    accessed: 2026-09-25
  - title: kristopherkyle/TAASSC (spaCy-based, CC BY-NC-SA 4.0)
    url: https://github.com/kristopherkyle/TAASSC
    accessed: 2026-09-25
  - title: LCR-ADS-Lab/TAACO (Python 3 + spaCy, importable, CC BY-NC-SA 4.0)
    url: https://github.com/LCR-ADS-Lab/TAACO
    accessed: 2026-09-25
  - title: kristopherkyle/TAALED (lexical diversity; CC BY-NC-SA 4.0)
    url: https://github.com/kristopherkyle/TAALED
    accessed: 2026-09-25
  - title: Lee & Lee (2023), LFTK, Handcrafted Features in Computational Linguistics (BEA 2023)
    url: https://aclanthology.org/2023.bea-1.1/
    accessed: 2026-09-25
  - title: LFTK on PyPI (1.0.9, license CC BY-NC 4.0)
    url: https://pypi.org/project/lftk/
    accessed: 2026-09-25
  - title: brucewlee/lingfeat (EMNLP 2021; PyPI license cc-by-sa-4.0)
    url: https://github.com/brucewlee/lingfeat
    accessed: 2026-09-25
  - title: Coh-Metrix at ASU SoLET lab (desktop by request; web via T.E.R.A.)
    url: https://soletlab.asu.edu/coh-metrix/
    accessed: 2026-09-25
  - title: Arase et al. (2022), CEFR-Based Sentence Difficulty Annotation and Assessment (EMNLP)
    url: https://aclanthology.org/2022.emnlp-main.416/
    accessed: 2026-09-25
---

# Readability, lexical sophistication and diversity

> **TL;DR** **Trial**, built from permissive parts: a **grade-level ensemble** (textstat), **MTLD/MATTR** (lexicalrichness), **word-frequency sophistication** (wordfreq Zipf), and spaCy syntax counts. The research suites (TAALES, TAACO, TAASSC, LFTK, Coh-Metrix) are the right *feature catalog*, but most are **non-commercial licensed**. Treat them as a reference to re-implement from, not as dependencies. These metrics answer "a 4th grader wrote this" and "this is a wall of nominalized 45-word sentences". They do **not** answer "this is good".

## What it is

- **Grade-level ensemble.** Five formulas (FK, Fog, SMOG, Coleman-Liau, Dale-Chall) and textstat's `text_standard` consensus. The spread between formulas is itself a warning sign: very different grades mean the text is unusual (jargon, or long lists).
- **Lexical diversity.** MTLD, HD-D, MATTR. McCarthy & Jarvis (2010) found MTLD nearly independent of length (r = −.02) and recommended MTLD with HD-D or Maas. Zenker & Kyle (2021) found MATTR and MTLD the most stable indices and set a **50-token minimum**. A 250-word grant answer is fine.
- **Lexical sophistication.** Mean frequency of content words (Zipf, wordfreq) and the share of rare words. TAALES extends this to 400+ indices (range, n-gram frequency, age of acquisition, psycholinguistic norms).
- **Cohesion.** TAACO (150 indices): adjacent-sentence overlap, connectives, givenness, semantic similarity between sections. **Syntactic complexity:** TAASSC (clause types, phrase elaboration). **Coh-Metrix** is the older ancestor of both (desktop on request, web via T.E.R.A.; terms unverified).
- **Feature libraries.** LFTK (220+ features, spaCy-based, BEA 2023) and lingfeat (255 features, readability-oriented).
- **CEFR estimation.** The CEFR-SP sentence-level estimator (Arase et al. 2022, macro-F1 84.5) is built for learner-facing text. Hub CEFR classifiers exist, but the one we checked is NC-licensed with thin documentation.

## Probe on the pilot (2026-09-25, local)

| Sample (words) | FK grade | MTLD | Mean Zipf | Rare % | Mean sent. len |
|---|---|---|---|---|---|
| Firm project descriptions (188) | 18.9 | 139 | 4.35 | 20.5 | 23.5 |
| Pilot narrative, modelling ¶ (255) | 28.8 | 125 | 4.48 | 5.1 | **51.0** (SD 22.7) |
| Firm boilerplate (173) | 18.6 | 172 | 4.70 | 8.0 | 19.2 |
| Synthetic "AI slop" (128) | 15.7 | **178** | 4.44 | 11.1 | 18.3 |
| Synthetic 4th-grade text (76) | −0.3 | **25** | **5.42** | 2.5 | 5.4 |
| Synthetic ungrammatical text (96) | 6.8 | 96 | 5.02 | 0.0 | 16.0 |

Findings: (1) The grade ensemble and Zipf flag the 4th-grader case clearly. (2) **High lexical diversity is not quality.** The slop and boilerplate samples score *highest* on MTLD, because buzzwords rarely repeat. Report MTLD only as a low-side warning (repetitive, limited vocabulary). (3) The worst readability in the pilot comes from one 51-word-average paragraph. Sentence-length spread localizes that problem better than a grade does. (4) Readability says nothing about grammar: the ungrammatical sample reads at "grade 7".

## Granularity and short-text reliability

Grades and Zipf means are document-level; compute them per paragraph and flag outliers. Per-sentence length, dependency distance, and nominalization counts give **spans** Claude can split or rewrite. At 250 words, individual TAALES/TAACO indices are noisy. Use a handful of robust ones.

## How it would fit

M4 computes the panel per chunk and per draft paragraph and stores it as derived data. M7 converts values to **percentiles against the firm's reference corpus** (see [norming](m-norming-presentation.md)) and emits findings such as `sentence 3: 64 words, 99th percentile`.

## Weaknesses / risks

- **Licenses.** Hyphae is a commercial firm. TAALES/TAACO/TAASSC/TAALED (CC BY-NC-SA) and LFTK (CC BY-NC) are unsafe dependencies. Re-implementing individual published formulas is fine.
- Formulas penalize necessary technical terms ("Universal Thermal Climate Index"). Use funder-appropriate bands, never a single target.
- Metrics invite gaming. See [readability-descriptives](../nlp-quality/readability-descriptives.md) for the existing caveats.

## Verdict rationale

Cheap, deterministic, and span-capable. Useful for the "too simple / too dense" axis. Keep the NC research suites as a catalog only.

Parent: [Prose signals](index.md) · Up: [Holistic metrics](holistic-metrics.md)
