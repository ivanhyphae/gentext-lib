---
title: Grammatical error density (LanguageTool rate, CoLA acceptability, GEC edit rate)
slug: m-grammar-error-density
level: 3
parent: index.md
related: [holistic-metrics.md, m-aes-ellipse.md, a-languagetool-api.md, ../nlp-quality/languagetool.md, ../nlp-quality/spacy-rule-matching.md]
tags: [grammar, gec, ged, acceptability, cola, languagetool, span-level]
status: draft
updated: 2026-09-25
kind: technique
verdict: trial
fit: [M4, M7]
license: LanguageTool LGPL-2.1 (server; language_tool_python client GPL, see nlp-quality card); textattack/roberta-base-CoLA license not stated; flan-t5-large-grammar-synthesis weights Apache-2.0 (dataset CC BY-NC-SA); gotutiyan/gector code MIT, weights non-commercial
maturity: mature
inspectability: medium
sources:
  - title: textattack/roberta-base-CoLA model card (GLUE CoLA; eval accuracy ≈ 0.85)
    url: https://huggingface.co/textattack/roberta-base-CoLA
    accessed: 2026-09-25
  - title: pszemraj/flan-t5-large-grammar-synthesis model card (0.8B; expanded JFLEG; work in progress)
    url: https://huggingface.co/pszemraj/flan-t5-large-grammar-synthesis
    accessed: 2026-09-25
  - title: gotutiyan/gector (unofficial PyTorch GECToR; tag-based edits; code MIT, HF weights non-commercial)
    url: https://github.com/gotutiyan/gector
    accessed: 2026-09-25
  - title: Omelianchuk et al. (2020), GECToR, Grammatical Error Correction, Tag, Not Rewrite (arXiv 2005.12592)
    url: https://arxiv.org/abs/2005.12592
    accessed: 2026-09-25
  - title: gotutiyan/gec-metrics (ACL 2025 demo; GEC evaluation library)
    url: https://github.com/gotutiyan/gec-metrics
    accessed: 2026-09-25
  - title: language_tool_python on PyPI (3.4.0; bundles LanguageTool 6.8 download)
    url: https://pypi.org/project/language-tool-python/
    accessed: 2026-09-25
---

# Grammatical error density

> **TL;DR** **Trial** a three-layer "big grammar problems here" signal. (1) **LanguageTool grammar matches per 100 words**, excluding spelling, which is mostly proper nouns. (2) A **CoLA acceptability classifier** per sentence (RoBERTa, CPU), the best cheap *span locator*. (3) A **GEC model's edit rate** as a confirmation and fix suggestion. Keep layer 3 behind a fact guard: in our probe the Flan-T5 corrector silently changed dates and names. Report density vs the firm corpus, and list the worst sentences.

## What it is

- **Rule-based density.** LanguageTool matches by category (GRAMMAR, CONFUSED_WORDS, PUNCTUATION, TYPOS) per 100 words. It is precise, but it has gaps: it missed "one of the primary recreational facility" in the earlier probe and again here.
- **Grammatical error detection (GED) as acceptability.** Classifiers trained on CoLA (sentence acceptability) output P(acceptable) per sentence. Cheap, and they give sentence spans directly.
- **GEC edit rate.** Run a corrector and count word-level edits per 100 words. **Tag-based** GECToR outputs explicit edit operations ($KEEP, $APPEND, $TRANSFORM), so its edits are auditable. **Seq2seq** correctors (T5/Flan) rewrite the sentence and can paraphrase or hallucinate.

## Probe on the pilot (2026-09-25, local CPU)

| Sample | LT grammar-type /100 w | CoLA mean / min | Flan-T5 edits /100 w |
|---|---|---|---|
| Pilot narratives (4 paragraphs) | 0.0–0.4 | 0.86–0.95 / 0.51–0.91 | 2.8–14.8 |
| Meeting summary (notes) | 0.4 | 0.72 / **0.47** | 11.6 |
| Synthetic "AI slop" | 0.0 | 0.97 / 0.94 | 5.6 |
| Synthetic 4th-grade | 0.0 | 0.94 / 0.52 | 31.6 (hallucinated) |
| Synthetic ungrammatical | **9.4** | **0.11 / 0.04** | **44.8** |

Findings:

1. All three separate the broken sample from professional prose by an order of magnitude. At document level, "big grammar problems" is easy.
2. **CoLA found the known pilot defect.** Its lowest-scoring sentence in that paragraph was exactly the "one of the primary recreational facility" sentence (0.51), which LanguageTool missed. Flan-T5 corrected it to "facilities".
3. **The seq2seq corrector is unsafe as a metric or auto-fix.** It changed "2023–2026" to "2012-2015", "Hyphae has" to "He has", and "ARPD" to "ARP". It turned "Trees make shade." into "Trees make me sad. I hate them." Paraphrase inflates its edit rate on clean text (up to 14.8 per 100 words).
4. Grammatical fluency says nothing about substance: the slop sample is the most "acceptable" text in the set.

## Granularity and short-text reliability

LanguageTool and GECToR give character spans. CoLA gives sentence spans. The Flan-T5 diff gives token spans. A 250-word answer has about 10 sentences, so report the **count of sentences below threshold** and the worst three, not a mean. CoLA was trained on short linguist-made sentences, so long compound sentences score lower. Norm against the firm corpus.

## How it would fit

- M7 `grammar_density` finding: `3 of 11 sentences below acceptability p5; worst: S4 [quote]; LT: 2 GRAMMAR matches`. It attaches a suggested correction only when a GEC diff **preserves all numbers, entities, and registry terms** (M3 check), and it presents the correction as a diff for Claude to apply or reject.
- Prefer GECToR-style tagged edits over rewrites once a commercially usable checkpoint exists. Its current HF weights are non-commercial.

## Weaknesses / risks

- The CoLA checkpoint has no stated license, and domain jargon lowers its scores.
- LanguageTool's Java server is heavy, and its Python client is GPL (see [LanguageTool](../nlp-quality/languagetool.md)).
- Seq2seq GEC hallucinates, as shown above. Never let it write into drafts unreviewed.

## Verdict rationale

The cheapest reliable "is the grammar broken here?" signal, with span localization and a proven catch on a real pilot defect. Trial the LT + CoLA combination; the GEC fixes need a guard.

Parent: [Prose signals](index.md) · Up: [Holistic metrics](holistic-metrics.md)
