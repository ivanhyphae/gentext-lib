---
title: Slop lexicons and pattern lists (slop-forensics, Slop Score, excess vocabulary, Signs of AI writing)
slug: s-slop-lexicons
level: 3
parent: index.md
related: [ai-slop.md, span-feedback-schema.md, ../nlp-quality/hedge-booster-lexicon.md, ../nlp-quality/vale.md, ../nlp-quality/spacy-rule-matching.md, m-genericness.md]
tags: [ai-slop, lexicon, patterns, negative-parallelism, em-dash, humanizer]
status: draft
updated: 2026-09-25
kind: technique
verdict: adopt
fit: [M4, M7]
license: slop-forensics MIT; slop-score MIT (+ wordfreq Apache-2.0/CC-BY-SA); antislop MIT; Wikipedia CC BY-SA 4.0; llm-excess-vocab code (license unverified), paper CC BY 4.0
maturity: emerging
inspectability: high
sources:
  - title: sam-paech/slop-forensics (MIT)
    url: https://github.com/sam-paech/slop-forensics
    accessed: 2026-09-25
  - title: sam-paech/slop-score and EQ-Bench Slop Score page
    url: https://eqbench.com/slop-score.html
    accessed: 2026-09-25
  - title: Paech et al. Antislop, A Comprehensive Framework for Identifying and Eliminating Repetitive Patterns in Language Models (arXiv 2510.15061)
    url: https://arxiv.org/abs/2510.15061
    accessed: 2026-09-25
  - title: Kobak et al. Delving into LLM-assisted writing in biomedical publications through excess vocabulary (Science Advances 2025)
    url: https://www.science.org/doi/10.1126/sciadv.adt3813
    accessed: 2026-09-25
  - title: Wikipedia, Signs of AI writing
    url: https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing
    accessed: 2026-09-25
  - title: Wikipedia, Negative parallelism
    url: https://en.wikipedia.org/wiki/Negative_parallelism
    accessed: 2026-09-25
  - title: The em-dash em-beds in Congress (arXiv 2608.05889)
    url: https://arxiv.org/pdf/2608.05889
    accessed: 2026-09-25
---

# Slop lexicons and pattern lists

> **TL;DR** **Adopt as deterministic detectors, but only with a curated, domain-tuned list.** The public lists are good raw material: slop-forensics and Slop Score (MIT), excess-vocabulary studies, and Wikipedia's *Signs of AI writing*, which the user's `humanizer` skill already encodes as 35 patterns. Our pilot probe showed why curation matters. Slop Score's word list is **fiction-biased**, and on the firm's own prose it mostly flagged funder and domain terms (*resilience*, *stewardship*, *interventions*). A short, reviewed list plus pattern regexes (negative parallelism, tricolon, em-dash density), normed against the firm corpus, gives span-level hits that are explainable and cheap to argue with.

## What exists

| Source | What it gives | Notes |
|---|---|---|
| **slop-forensics** (Paech) | `slop_list.json`, bigrams, trigrams, phrases: words over-represented in LLM output against human text, pooled across models | MIT; the pipeline can profile *any* model, including Claude on our prompts |
| **Slop Score** (EQ-Bench) | composite: 60% slop words, 25% "not-x-but-y" contrast patterns, 15% slop trigrams; plus MATTR, FK grade, n-gram repetition | MIT JS; runs in the browser; the contrast regexes in `js/regexes-stage1.js` are careful and portable |
| **Antislop** (arXiv 2510.15061) | sampler and FTPO fine-tuning to *suppress* slop; some patterns are more than 1,000× more frequent in LLM text than in human text | generation side; relevant only if we ever self-host a drafter |
| **Excess vocabulary** (Kobak et al. 2025) | style words whose frequency jumped in 15M+ PubMed abstracts after 2022 (*delves, underscores, showcasing…*); at least 13.5% of 2024 abstracts LLM-processed | the method is reusable: diff our firm corpus before and after 2023 |
| **Wikipedia: Signs of AI writing** | content, language, style, and chatbot-artifact signs; vocabulary (*delve, tapestry, pivotal, underscore, testament, foster, showcase, vibrant*…) | explicitly "potential signs of a problem, not the problem itself" |
| **`humanizer` skill** (user's) | 35 named patterns with rewrite guidance and a "what not to flag" section | already the rewrite side; our detectors should share its pattern ids |

Pattern evidence: negative parallelism is reported at about 3× human frequency (Wikipedia, *secondary*). Em-dash density in U.S. congressional press releases more than doubled in 2025, a within-author rise (arXiv 2608.05889).

## Hands-on probe (2026-09-25, local, pilot DOCX via zipfile)

| Metric | Ambrose EHCRP doc (15.3k words) | Urban Greening concept (2.1k) | Synthetic slop paragraph |
|---|---|---|---|
| Curated AI-vocab list (48 word forms) per 100 words | 0.27 | 0.24 | 18.7 |
| Slop Score `slop_list.json` hits per 100 words | 1.62 | 0.75 | n/a |
| Negative parallelism (simplified port of regex 1 + "not only…but") | 4 (1 false positive) | 0 | 2 |
| Em-dash per 100 words | 0.58 | 0.05 | 0 |

The top `slop_list` hits in the pilot were *resilience* (37), *stewardship* (21), *prioritize*, *interventions*, *relational* and *strategies*, all legitimate program vocabulary. The list is built from creative-writing prompts, and it also contains fantasy character names. The curated list's hits (*transformative, enhance, comprehensive, cutting-edge, leverage, robust*) are real candidates for plainer wording. Per-100-word density of about 0.25 is low. The signal is the **cluster**: the synthetic slop paragraph hit 14 distinct terms in 75 words.

## How it would fit

- An M4/M7 deterministic detector family `lex.*`: `lex.ai-vocab`, `lex.contrast`, `lex.tricolon`, `lex.emdash-density`, `lex.stock-phrase`. Each hit is a span finding with `evidence.lexicon_entry` and a humanizer pattern id ([schema](span-feedback-schema.md)).
- Implement as a Vale style (YAML, versioned next to the glossary; [Vale](../nlp-quality/vale.md)) or spaCy PhraseMatcher. Port Slop Score's contrast regexes to Python.
- **Allowlist from M5**: funder vocabulary (EHCRP's *Belonging*, *Lasting Community Benefits*) and glossary terms are exempt, like quoted community voices.
- **Density findings are paragraph-scoped** and normed ([norming](m-norming-presentation.md)). Single words are `info`, and clusters (three or more distinct hits per sentence) are `minor`.
- Optional: run slop-forensics on Claude drafts versus the firm's human paragraphs to build *our* over-representation list. That is the method, applied to our domain.

## Strengths

- Fully inspectable, fast and reproducible. Every hit is arguable, and they overlap with the hype/booster lexicon ([card](../nlp-quality/hedge-booster-lexicon.md)).
- Claude can act directly on a hit: delete, replace, or make concrete.

## Weaknesses / risks

- Genre mismatch (above) and false positives on humans. Wikipedia itself warns these are signs, not proof.
- Whack-a-mole: banning *delve* just moves the model to the next synonym. Lexicons catch surface features, and genericness needs [m-genericness](m-genericness.md).
- Lists go stale as models change. Date and version every list.

## Verdict rationale

Adopt, with three conditions: a curated list, an M5 allowlist, and severity by cluster rather than single hits.

Parent: [Prose signals](index.md) · Up: [AI slop](ai-slop.md)
