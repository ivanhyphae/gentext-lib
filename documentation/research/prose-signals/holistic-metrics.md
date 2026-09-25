---
title: Holistic prose-quality metrics (paragraph and document level)
slug: holistic-metrics
level: 2
parent: index.md
related: [m-readability-sophistication.md, m-aes-ellipse.md, m-grammar-error-density.md, m-specificity-concreteness.md, m-genericness.md, m-perplexity.md, m-voice-distance.md, m-norming-presentation.md, commercial-apis.md, ../nlp-quality/index.md, ../nlp-quality/check-catalog.md, ../llm-evaluation/rubric-judging.md]
tags: [metrics, readability, aes, grammar, specificity, genericness, perplexity, voice, M4, M7]
status: draft
updated: 2026-09-25
---

# Holistic prose-quality metrics

> **TL;DR** No single NLP metric measures "good proposal prose", but a **panel of seven cheap, local signals** can tell Claude *where* the problem is and *what kind* it is: generic, childlike, broken grammar, over-dense, off-voice, or stock phrasing. Report each as a **percentile against the firm's own exemplar corpus**, with the worst spans quoted, and combine them into **named symptoms** instead of a composite score. Adopt: concreteness plus anchor density, and the norming contract. Trial: grammar density (LanguageTool + CoLA), the readability/sophistication panel, genericness (portability, hivemind distance), and voice distance (Burrows' Delta). Assess: perplexity and ELLIPSE-style essay scorers, which are real signals only at the extremes.

This page builds on the copy-editing research in [NLP quality](../nlp-quality/index.md) (Vale, spaCy rules, textstat, hedge lexicon, embeddings), which covers *specific defects*. This page covers *holistic* complaints about larger chunks. For hosted services, see [commercial APIs](commercial-apis.md).

## The maintainer's complaints → measurable symptoms

| Complaint | Primary signals | Span unit | Card |
|---|---|---|---|
| "This is generic" | no anchors (entities/numbers/registry terms); low concreteness; high portability to other-project text; closeness to an LLM "hivemind" answer | sentence | [specificity](m-specificity-concreteness.md), [genericness](m-genericness.md) |
| "This is AI slop" | generic symptoms + low, flat surprisal + stock-phrase lexicon hits + high MTLD with low concreteness | sentence run | [genericness](m-genericness.md), [perplexity](m-perplexity.md) |
| "A 4th grader wrote this" | grade ensemble < band; low MTLD; high mean word frequency; short, uniform sentences; ELLIPSE traits low | paragraph | [readability](m-readability-sophistication.md), [AES](m-aes-ellipse.md) |
| "Big grammar problems here" | LanguageTool grammar rate; CoLA acceptability below threshold; GEC edit rate (guarded) | sentence / char | [grammar density](m-grammar-error-density.md) |
| "Wall of words" | sentence length > p95; dependency distance; nominalization rate; formula spread | sentence | [readability](m-readability-sophistication.md) |
| "Doesn't sound like us" | Burrows' Delta and feature-profile drivers vs the exemplar corpus | paragraph | [voice distance](m-voice-distance.md) |

## Landscape

- **Readability and sophistication** (textstat formulas, MTLD/HD-D/MATTR, Zipf frequency, TAALES/TAACO/TAASSC, Coh-Metrix, LFTK/lingfeat, CEFR estimators). Mature and interpretable. The research suites are **non-commercial licensed**, so re-implement the individual indices from permissive parts.
- **Automated essay scoring.** ELLIPSE (six analytic traits) and PERSUADE (argument-element spans) from the Kaggle Feedback Prize. Models exist, but they are trained on grade 8–12 learner essays and **saturate on professional prose**.
- **Grammatical error detection/correction.** LanguageTool (rules), CoLA classifiers (acceptability), GECToR (tag edits), Flan-T5 correctors (rewrites, hallucination-prone).
- **Specificity.** Brysbaert concreteness norms (CC BY), NER/number density, Speciteller/Ko et al. specificity models (stale code), Granuscore (2026).
- **Genericness/homogenization.** Embedding portability, boilerplate MinHash, place-swap tests, LLM-consensus distance (Artificial Hivemind 2025), slop-lexicon lists (slop-score, Kobak excess vocabulary). Shaib et al. (2025) show that slop splits into components (density, relevance, repetition, templatedness, verbosity, tone) and that automatic proxies for them are weak on their own.
- **LM predictability.** Perplexity/burstiness with a 0.5B model, and Binoculars. Informative but confounded, with documented bias.
- **Stylometry.** Burrows' Delta and feature profiles. They cannot attribute authorship at 250 words, but they discriminate *register* well.

## Probe summary (pilot excerpts + three synthetic controls, CPU, 2026-09-25)

Seven pilot paragraphs (150–250 words: firm project descriptions, boilerplate, four narrative answers, a meeting summary) and three synthetic controls we wrote (AI-slop, 4th-grade, ungrammatical). Details are on each card.

- **Every floor case was caught by at least two signals.** Ungrammatical: LT 9.4 hits/100 w, CoLA 0.11, ELLIPSE grammar 2.25. Childlike: FK −0.3, MTLD 25, Delta 1.16. Slop: 0 entities, concreteness 2.70, lowest perplexity among fluent texts, Delta 0.68.
- **Signals that invert or saturate:** MTLD was *highest* for slop (178) and boilerplate (172). The ELLIPSE scorer rated slop as highly as the best pilot text. CoLA rated slop the *most* acceptable. Fluency metrics reward slop.
- **Real pilot findings:** CoLA's worst sentence in one answer was the known "one of the primary recreational facility" defect, which LanguageTool missed. Firm boilerplate had concreteness 2.71, near the slop sample. One narrative paragraph averaged 51 words per sentence (FK 28.8), and 60% of its sentences were near-duplicates of method language from other projects.
- **Hazard:** the Flan-T5 grammar corrector changed dates ("2023–2026" → "2012-2015") and names ("Hyphae has" → "He has"). Rewrite-based models must never auto-apply.

## Recommended panel

| # | Signal | Tool (license) | Granularity | ≈ runtime per 250 w (CPU) | Verdict |
|---|---|---|---|---|---|
| 1 | Anchor density + concreteness | spaCy + Brysbaert norms + M3 registries (MIT / CC BY) | sentence | < 50 ms | adopt |
| 2 | Grammar density | LanguageTool server (LGPL) + `roberta-base-CoLA` | sentence/char | ≈ 1 s | trial |
| 3 | Readability band + sentence-length outliers | textstat, spaCy (MIT) | sentence/paragraph | < 50 ms | trial |
| 4 | Lexical diversity (low-side only) + word frequency | lexicalrichness MATTR/MTLD, wordfreq (MIT/Apache) | paragraph (≥ 50 tokens) | < 50 ms | trial |
| 5 | Portability / hivemind distance | sentence-transformers MiniLM or bge (Apache) + cached LLM pool | sentence | ≈ 0.2 s (+ LLM once per question) | trial |
| 6 | Voice distance | own Delta + feature profile vs exemplars | paragraph | < 50 ms | trial |
| 7 | Predictability | Qwen2.5-0.5B surprisal (Apache) | sentence run | ≈ 2–5 s | assess |
| — | ELLIPSE trait scorer | KevSun RoBERTa (NC data) | paragraph | ≈ 1 s | assess (floor only) |

All of these run locally, and none needs an API or a GPU. That fits the DR-0004 confidentiality posture even for non-public drafts.

## Interpretation guidance for Claude

1. Read **symptoms**, not metrics. A symptom fires only when two or more signals agree (e.g., *generic* = unanchored AND concreteness < p20, OR portable > 0.6 in a place-specific question).
2. Treat every percentile as relative to `firm-exemplar` (see [norming](m-norming-presentation.md)). Out-of-domain models are advisory.
3. Fix **content first**. The remedy for generic text is a fact from M3 (or a `{>>TK …<<}` placeholder), not synonyms. Don't rewrite to move a number.
4. Metrics never fail a draft. They supply quotable evidence for the [rubric pass](../llm-evaluation/rubric-judging.md) and the [adversarial reviewer](../llm-evaluation/adversarial-review-pass.md).

## Open questions / next steps

- Build `firm-exemplar` (the team marks about 50 paragraphs) and a 50-sentence human-labelled set (generic / grammar / fine) from the Harm Reduction answers. Calibrate thresholds on it.
- Test hivemind distance and NLI place-swap. Both are unprobed.
- Resolve the licensing of the CoLA checkpoint and the ELLIPSE-derived models before any commercial use.

## Children

- [Readability, sophistication, diversity](m-readability-sophistication.md): trial
- [Automated essay scoring (ELLIPSE, PERSUADE)](m-aes-ellipse.md): assess
- [Grammatical error density](m-grammar-error-density.md): trial
- [Specificity and concreteness](m-specificity-concreteness.md): adopt
- [Genericness](m-genericness.md): trial
- [Perplexity and surprisal](m-perplexity.md): assess
- [Voice distance](m-voice-distance.md): trial
- [Norming and presentation](m-norming-presentation.md): adopt

Parent: [Prose signals](index.md)
