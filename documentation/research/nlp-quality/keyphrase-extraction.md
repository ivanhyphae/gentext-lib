---
title: Keyphrase extraction (YAKE, KeyBERT)
slug: keyphrase-extraction
level: 3
parent: index.md
related: [sentence-embeddings.md, embeddings-and-similarity.md]
tags: [keyphrases, yake, keybert, metadata]
status: draft
updated: 2026-09-25
kind: library
verdict: assess
fit: [M1, M4, M7]
license: YAKE AGPL-3.0 per repo LICENSE (PyPI metadata says LGPLv3/GPLv3, inconsistent); KeyBERT MIT
maturity: mature
inspectability: medium
sources:
  - title: INESCTEC/yake GitHub repository and LICENSE (AGPL-3.0 + commercial option; v0.7.3, 2026-02-09)
    url: https://github.com/INESCTEC/yake
    accessed: 2026-09-25
  - title: yake on PyPI (0.7.3; license field LGPLv3, classifier GPLv3)
    url: https://pypi.org/project/yake/
    accessed: 2026-09-25
  - title: MaartenGr/KeyBERT GitHub repository (MIT; v0.9.0, 2025-02-07; last push 2026-08-25)
    url: https://github.com/MaartenGr/KeyBERT
    accessed: 2026-09-25
  - title: Campos et al. (2020), YAKE! Keyword extraction from single documents using multiple local features, Information Sciences 509
    url: https://doi.org/10.1016/j.ins.2019.09.013
    accessed: 2026-09-25
---

# Keyphrase extraction (YAKE, KeyBERT)

> **TL;DR** **Assess.** Keyphrases help propose chunk `topics[]` metadata (M1) and give a cheap "does the answer address the prompt's key terms?" signal (T4). **KeyBERT** (MIT) reuses our embedding model and is the easy choice. **YAKE** is statistical, model-free, and explainable, but its **license is inconsistent** (repo LICENSE says AGPL-3.0 with a commercial option; PyPI metadata says LGPL/GPL). Clear that with a human before depending on it.

## What it is

- **YAKE!** (INESC TEC; v0.7.3, 2026-02). Unsupervised, single-document, and needs no corpus or model. It scores candidate n-grams from local features: casing, position, frequency, context dispersion, and sentence spread (Campos et al. 2020). Deterministic, and each score comes from named features.
- **KeyBERT** (MIT; v0.9.0 2025-02, repo active 2026-08). Embeds the document and candidate n-grams with any sentence-transformers model (or others) and ranks candidates by cosine to the document. It supports MMR or Max-Sum diversification and seeded keywords. Deterministic given the model, but the reason for a ranking is "embedding similarity", which is less inspectable.
- Alternatives *(not evaluated)*: spaCy noun chunks + TF-IDF against the library, `pke`, TextRank variants.

## Why it matters for adapt-rfp

- **Metadata proposals.** M1 must propose `topics[]` so humans only confirm (DR-0003). Keyphrases mapped onto the controlled glossary topics give suggestions that are grounded in the text.
- **Prompt coverage (T4).** Extract keyphrases from the M5 question prompt and rubric High band. Report which ones have no lexical or semantic counterpart in the draft. It is a coarse signal, and cheaper than an LLM pass.
- **Library search facets.** Keyphrase indexes improve lexical retrieval alongside embeddings.

## How it would fit

- M4: `keyphrases(chunk, method="keybert", model=<pinned>)` cached as derived data.
- Prefer mapping raw keyphrases onto glossary terms (rapidfuzz/embedding match) over storing free-text keyphrases as canonical metadata.

## Strengths

- Both are light. KeyBERT adds no new model if we already embed.
- YAKE works with no model at all and explains its scores.

## Weaknesses / risks

- Keyphrases are noisy for short (≤ 250-word) texts.
- YAKE's license ambiguity (AGPL in the repo) matters if adapt-rfp is ever offered as a network service. Treat it as AGPL until clarified.
- Neither measures quality. They only describe content.

## Verdict rationale

Useful but not central. None of the DR-0002 defects needs it. Assess KeyBERT during M1 metadata work.

Parent: [NLP quality checks](index.md)
