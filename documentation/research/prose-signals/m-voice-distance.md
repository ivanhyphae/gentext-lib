---
title: Voice distance to the firm's best writing (Burrows' Delta, feature profiles, embedding centroids)
slug: m-voice-distance
level: 3
parent: index.md
related: [holistic-metrics.md, m-genericness.md, m-norming-presentation.md, ../nlp-quality/stylometry-ai-detection.md, ../nlp-quality/sentence-embeddings.md]
tags: [voice, stylometry, burrows-delta, register, embeddings, reference-corpus]
status: draft
updated: 2026-09-25
kind: technique
verdict: trial
fit: [M4, M7]
license: own implementation (numpy); faststylometry MIT; sentence-transformers Apache-2.0
maturity: emerging
inspectability: high
sources:
  - title: Eder (2015), Does size matter? Authorship attribution, small samples, big problem (Digital Scholarship in the Humanities)
    url: https://www.researchgate.net/publication/274151528_Does_size_matter_Authorship_attribution_small_samples_big_problem
    accessed: 2026-09-25
  - title: Evert et al. (2015), Towards a better understanding of Burrows's Delta in literary authorship attribution (CLfL workshop)
    url: https://aclanthology.org/W15-0709.pdf
    accessed: 2026-09-25
  - title: fastdatascience/faststylometry (Burrows' Delta in Python; MIT)
    url: https://github.com/fastdatascience/faststylometry
    accessed: 2026-09-25
---

# Voice distance to the firm's best writing

> **TL;DR** **Trial**, framed as *register/voice conformity*, not authorship. Build a **reference corpus** of paragraphs the team marks as its best writing. Score a draft paragraph with (a) **Burrows' Delta over function-word and style-feature profiles** and (b) the paragraph's **percentile position** on each panel metric within that corpus. Embedding-centroid cosine mostly measures *topic*, so use it only as a secondary signal. At 150–250 words, Delta cannot attribute authors (that needs about 2,000+ words), but in our probe it cleanly separated firm-register prose from notes, slop, childlike, and ungrammatical text.

## What it is

- **Burrows' Delta.** z-score the relative frequencies of the most frequent words (mostly function words) against a corpus, then take the mean absolute z-difference from the reference profile. Evert et al. (2015) analyse why it works and which variants are better (e.g., cosine Delta).
- **Style-feature profile.** The same idea over interpretable features we already compute: sentence-length mean/SD, passive ratio, nominalization rate, concreteness, hedges/boosters, first-person plural rate. Each feature is a named, explainable deviation.
- **Embedding centroid.** Cosine between the paragraph embedding and the mean embedding of reference paragraphs.

## Probe on the pilot (2026-09-25)

Reference = 10 firm project-description paragraphs (44–124 words). Delta uses 36 function words, with the SD floored at 0.01. Leave-one-out gives the reference's own spread.

| Sample | Delta (lower = closer) | Embedding cosine to centroid |
|---|---|---|
| Reference paragraphs, leave-one-out | median 0.48 (0.35–0.61) | median 0.70 (min 0.50) |
| Pilot narratives (4) | 0.36–0.45 | 0.52–0.67 |
| Firm boilerplate | 0.42 | 0.70 |
| Meeting summary | 0.55 | 0.56 |
| Synthetic "AI slop" | **0.68** | 0.58 |
| Synthetic ungrammatical | **0.84** | 0.59 |
| Synthetic 4th-grade | **1.16** | **0.48** |

Findings: Delta put every real firm paragraph inside the reference band and every off-register sample outside it. That includes the slop, which the embedding cosine could not separate from the pilot narratives (0.58 vs 0.52–0.67). Embedding cosine tracked subject matter: the heat-modelling paragraph scored lowest among the pilot texts (0.52), even though it is on-register.

## Granularity and short-text reliability

Delta and feature profiles are paragraph-level. Below about 100 words, function-word frequencies get sparse, so pool adjacent paragraphs or rely on the feature profile. Localize spans by pointing at the sentences that drive the largest feature deviations ("S2–S4 average 48 words vs firm p50 of 24"). Eder (2015) finds attribution needs roughly 2,000 words or more, so **never** use these scores to infer who wrote a passage. Authorship comes from provenance metadata (DR-0008).

## How it would fit

- M2 marks exemplar chunks (`exemplar: true`, by voice: firm, partner, agency). M4 derives the reference profiles and norms and rebuilds them when exemplars change.
- M7 reports `voice: Delta 0.71 (outside firm band p95 0.61); drivers: sentence-length SD high, "we" rate 0, nominalizations p97`. Claude gets drivers it can act on, not a mystery number.
- M6 can rank candidate variants by voice fit before composing.

## Weaknesses / risks

- Only as good as the exemplar set. Ten paragraphs is a toy; aim for 50–100 curated ones per voice.
- Conformity is not quality: it can penalize a deliberate register change, such as community voice or quotes. Show it as information.
- Some funders value distinctiveness (PNAS 2026, see [genericness](m-genericness.md)). Voice conformity should mean the *firm's* voice, not the average proposal's.

## Verdict rationale

Deterministic, explainable, and in this small probe surprisingly discriminative at paragraph scale. Trial it as a register check with named drivers. Stylometric attribution stays on hold per the existing card.

Parent: [Prose signals](index.md) · Up: [Holistic metrics](holistic-metrics.md)
