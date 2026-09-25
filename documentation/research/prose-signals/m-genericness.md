---
title: Genericness (portability, boilerplate similarity, place-swap, "hivemind" baseline)
slug: m-genericness
level: 3
parent: index.md
related: [holistic-metrics.md, m-specificity-concreteness.md, m-perplexity.md, m-voice-distance.md, ../nlp-quality/sentence-embeddings.md, ../nlp-quality/minhash-lsh.md, ../nlp-quality/nli-claim-support.md]
tags: [genericness, boilerplate, embeddings, slop, homogenization, span-level]
status: draft
updated: 2026-09-25
kind: technique
verdict: trial
fit: [M4, M7]
license: sentence-transformers Apache-2.0; all-MiniLM-L6-v2 Apache-2.0; slop-score MIT (wordfreq.js Apache-2.0/CC BY-SA)
maturity: emerging
inspectability: medium
sources:
  - title: Shaib et al. (2025), Measuring AI "Slop" in Text (taxonomy; span annotation; arXiv 2509.19163)
    url: https://arxiv.org/html/2509.19163v2
    accessed: 2026-09-25
  - title: Jiang et al. (2025), Artificial Hivemind, the open-ended homogeneity of language models (NeurIPS 2025; arXiv 2510.22954)
    url: https://arxiv.org/abs/2510.22954
    accessed: 2026-09-25
  - title: Homogenizing effect of LLMs on creative diversity, human vs ChatGPT admissions essays (2025)
    url: https://www.sciencedirect.com/science/article/pii/S294988212500091X
    accessed: 2026-09-25
  - title: sam-paech/slop-score (over-represented LLM words, trigrams, "not X but Y" patterns; MIT)
    url: https://github.com/sam-paech/slop-score
    accessed: 2026-09-25
  - title: Kobak et al. (2025), Delving into LLM-assisted writing in biomedical publications through excess vocabulary (Science Advances)
    url: https://www.science.org/doi/10.1126/sciadv.adt3813
    accessed: 2026-09-25
  - title: Phys.org summary of the 2026 PNAS study on AI-assisted grant proposals and distinctiveness
    url: https://phys.org/news/2026-08-ai-grant-narrowing-ideas.html
    accessed: 2026-09-25
---

# Genericness

> **TL;DR** **Trial.** "This is generic" can be measured in four complementary ways, all per sentence. (1) **Anchor/concreteness** absence ([card](m-specificity-concreteness.md)). (2) **Portability**: high embedding similarity to sentences from *other* projects in the firm corpus, meaning the sentence could be pasted anywhere. (3) **Place-swap invariance**: swapping the place or partner leaves the sentence equally true. (4) **Hivemind distance**: similarity to what an LLM writes for the same question *without* our facts. (2) and (3) are cheap and deterministic. (4) costs a few LLM calls and is the most direct test of "AI slop". A stock-phrase lexicon (slop-score lists, the humanizer skill) supplies named, quotable hits.

## Why these operationalizations

Shaib et al. (2025) interviewed experts and found "slop" decomposes into information utility (density, relevance), information quality, and style quality (repetition, templatedness, verbosity, tone). Binary slop labels had poor agreement (κ ≤ 0.29), while span-level codes were more reliable. So we measure *components* on spans rather than a single "slop score". Homogenization studies (Artificial Hivemind 2025; admissions essays 2025; PNAS 2026 on grant proposals) show that LLM text converges on the same ideas and phrasings. Distance from that convergence point is therefore a meaningful axis.

## The four measures

| Measure | Computation | Granularity | Cost |
|---|---|---|---|
| Anchor absence | no entity, number, or registry term; concreteness < p20 | sentence | ms |
| Portability | max cosine to sentences from other-project chunks (sentence-transformers); also MinHash hits on boilerplate | sentence | ms |
| Place-swap | replace target place/partner with a foil from the registry; NLI or Claude asks "is this still equally true/relevant?" Invariant = generic | sentence | NLI ≈ 50 ms; Claude batch |
| Hivemind distance | generate N=5 answers to the same question with no firm facts (Claude and one other family); cosine of each draft sentence to that pool | sentence | 5 LLM calls per question, cacheable |

Supporting signals: gzip compression ratio and templates-per-token (Shaib's repetition/templatedness proxies), and excess-vocabulary lexicons (Kobak et al.'s marker words; slop-score's lists).

## Probe on the pilot (2026-09-25, local, all-MiniLM-L6-v2)

Reference = 10 firm project-description paragraphs. Share of sentences with cosine > 0.60 to a reference sentence ("portable"):

- Pilot narrative ¶ on heat modelling: **60%** portable (mean max cosine 0.64). Its method sentences sit closest (0.68–0.74) to the firm's LA Depave Plan and Green Heart descriptions, so it is method language carried over from other projects.
- Pilot narrative ¶ on community engagement: **0%** (0.45). Place-specific content.
- Firm boilerplate paragraphs: **56%**. Synthetic slop: **0%**.

The last result matters. Portability detects *our own* boilerplate, not generic AI prose, because slop is off-distribution from the firm corpus. The anchor check caught the slop instead (71% unanchored). That is why hivemind distance is the complementary test for slop. It was not run in this probe *(proposal; needs LLM calls)*.

## How it would fit

- M4 caches sentence embeddings and a per-sentence `portability` value. M6 can *prefer* portable sentences when reusing firm credentials (reuse is fine there) and flag them in place-specific answers.
- M7 emits: `S1 portable (0.74 to the LA Depave Plan chunk) + unanchored: generic for this question`. It suggests which M3 facts could anchor it.
- The hivemind pool is cached per solicitation question, which makes it a reusable "what everyone else will say" baseline for the whole pilot.

## Weaknesses / risks

- Portability is not a defect by itself: firm-experience sections *should* reuse approved text. Weight it by question type (M5).
- Embedding cosine is topic-dominated. Thresholds need calibration on a labelled sample, and 0.60 here is illustrative.
- Place-swap via NLI is untested on this domain *(unverified)*. Claude may do it better, as a quoted-span finding.

## Verdict rationale

Several independent, inspectable, span-level proxies for the complaint reviewers make most. Trial on Harm Reduction Q1/Q2 with a human-labelled set of ≈50 sentences.

Parent: [Prose signals](index.md) · Up: [Holistic metrics](holistic-metrics.md)
