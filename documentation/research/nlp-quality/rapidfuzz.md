---
title: RapidFuzz
slug: rapidfuzz
level: 3
parent: index.md
related: [spacy-rule-matching.md, abbreviation-detection.md, minhash-lsh.md]
tags: [fuzzy-matching, entity-resolution, names]
status: draft
updated: 2026-09-25
kind: library
verdict: adopt
fit: [M1, M3, M7]
license: MIT
maturity: mature
inspectability: high
sources:
  - title: rapidfuzz/RapidFuzz GitHub repository (MIT; v3.14.6, 2026-08-30)
    url: https://github.com/rapidfuzz/RapidFuzz
    accessed: 2026-09-25
  - title: RapidFuzz documentation
    url: https://rapidfuzz.github.io/RapidFuzz/
    accessed: 2026-09-25
---

# RapidFuzz

> **TL;DR** **Adopt.** RapidFuzz is a fast, MIT-licensed C++/Python string-similarity library (Levenshtein, Indel, Jaro-Winkler, token-sort/set ratios). Use it to catch **near-miss org names** ("Hispanic Counsel", "Resources Conservation District") that exact matching skips, and to normalize aliases while building the entity registry.

## What it is

The maintained successor to fuzzywuzzy, with a compatible `fuzz` / `process` API. v3.14.6 was released 2026-08-30. It provides `fuzz.ratio`, `partial_ratio`, `token_sort_ratio`, `token_set_ratio`, `WRatio`, and `distance.*` metrics, and `process.extract/extractOne/cdist` for vectorized matching against a list of choices.

## Local probe (2026-09-25)

| Query | Best canonical match | token_sort_ratio |
|---|---|---|
| "Contra Costa Resources Conservation District" | Contra Costa Resource Conservation District | 98.9 |
| "Caribbean South America Hispanic Counsel" | Caribbean South America Hispanic Council | 95.0 |

Both pilot misspellings score far above any plausible threshold while *not* being exact matches. That combination is the signal: "almost the canonical name, but not quite".

## How it would fit

- **M7 check L4.** For each candidate name span (spaCy NER `ORG`, noun chunks with capitalized tokens, or n-gram windows) that the PhraseMatcher did not match exactly, run `process.extractOne(span, registry_names_and_aliases, scorer=fuzz.token_sort_ratio, score_cutoff=90)`. A hit that is not an exact match gives an error with the suggestion "did you mean <canonical>?" and `because: registry:org/<id>`.
- **Short names.** Short strings give high ratios by chance ("CCRCD" vs "CCHS"). Require a minimum length, or use `distance.Levenshtein` ≤ 1 for acronyms, checked against the glossary.
- **M3 curation.** Cluster raw name mentions from all sources with `process.cdist` to propose alias groups for human confirmation.
- **M1.** Match headings across forked docs.

## Strengths

- Deterministic, with a numeric score and a named scorer, so it is fully explainable.
- Very fast (C++). `cdist` handles registry-sized matrices easily.
- No model, no data download.

## Weaknesses / risks

- Purely character-level. It won't link "Ambrose Recreation and Park District" to "ARPD". That needs the alias list and glossary.
- Thresholds need a small fixture set. Common words inflate `token_set_ratio`, so prefer `token_sort_ratio` or `WRatio` for names.
- Homophone errors that change *meaning* ("Counsel" is a real word) are exactly why an exact-match dictionary check alone is not enough, and why this check exists.

## Verdict rationale

Tiny dependency, direct hit on a pilot defect, and useful for registry building too.

Parent: [NLP quality checks](index.md)
