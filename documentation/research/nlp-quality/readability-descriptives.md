---
title: Readability and text descriptives (textstat, TextDescriptives)
slug: readability-descriptives
level: 3
parent: index.md
related: [spacy-rule-matching.md, minhash-lsh.md, check-catalog.md]
tags: [readability, descriptives, metrics, spacy]
status: draft
updated: 2026-09-25
kind: library
verdict: trial
fit: [M4, M7]
license: MIT (textstat); Apache-2.0 (TextDescriptives)
maturity: mature
inspectability: high
sources:
  - title: textstat GitHub repository (MIT; 0.7.13, 2026-02-18)
    url: https://github.com/textstat/textstat
    accessed: 2026-09-25
  - title: TextDescriptives documentation
    url: https://hlasse.github.io/TextDescriptives/
    accessed: 2026-09-25
  - title: TextDescriptives quality component
    url: https://hlasse.github.io/TextDescriptives/quality.html
    accessed: 2026-09-25
  - title: HLasse/TextDescriptives GitHub repository (Apache-2.0; v2.8.4, 2024-12-16; last push 2026-05-05)
    url: https://github.com/HLasse/TextDescriptives
    accessed: 2026-09-25
  - title: PassivePy (mitramir55/PassivePy, MIT; PyPI 0.2.23, 2023-07)
    url: https://github.com/mitramir55/PassivePy
    accessed: 2026-09-25
---

# Readability and text descriptives

> **TL;DR** **Trial.** Use **textstat** (MIT) for quick readability formulas and **TextDescriptives** (Apache-2.0, a set of spaCy components) for richer per-document metrics: sentence-length distribution, dependency distance, POS ratios, coherence, and Gopher-style repetition/quality flags. They are good for **targets, trends, and variant selection**. They are poor pass/fail gates, because readability formulas are crude for technical grant prose.

## What it is

- **textstat** 0.7.13 (2026-02): Flesch Reading Ease, Flesch-Kincaid grade, Gunning Fog, SMOG, Coleman-Liau, Dale-Chall, syllable and word counts, and more. Pure Python and fast.
- **TextDescriptives** v2.8.4 (2024-12; repo commits to 2026-05). spaCy v3 components for descriptive stats, readability, dependency distance, POS proportions, coherence, information theory, and **quality**. The quality component implements heuristics from Gopher (Rae et al. 2021) and T5 (Raffel et al. 2020): duplicate line, paragraph, and n-gram fractions, symbol-to-word ratio, and more. It exposes a `QualityThresholds` class and a `passed_quality_check` flag. Release cadence is slow, so check spaCy 3.8 compatibility.
- **Passive voice.** Either compute it from spaCy dependencies (`nsubjpass`/`auxpass`, see [spaCy rules](spacy-rule-matching.md)) or use PassivePy (MIT). PassivePy has not been released since 2023, so we prefer the handful of lines ourselves.

## Why it matters for adapt-rfp

- **Variant selection (M6).** Given a 250-word limit and three variants of a method chunk, prefer the one inside the funder's readability band.
- **Drift detection.** Sentence-length spread and passive ratio per author/voice help M1 attribute mixed-voice sections (firm vs partner) *(heuristic; see [stylometry](stylometry-ai-detection.md) caveats)*.
- **Repetition.** The duplicate n-gram fraction catches paragraphs pasted twice, a known risk with forked working docs.
- Local probe: "This cutting-edge tool offers unprecedented precision for heat modeling." scored Flesch Reading Ease 19.1 ("very difficult"). This shows how short, jargon-dense sentences skew the formulas.

## How it would fit

- M4 computes metrics per chunk and variant and caches them as derived data.
- M7 reports metrics with the funder's target band (M5 can carry `readability_target`, when the funder states one or the team chooses one), always as *info/warning*.

## Strengths

- Deterministic, cheap, well known. Formulas are documented.
- TextDescriptives gives many metrics through one `nlp.add_pipe` call.

## Weaknesses / risks

- Readability formulas measure syllables and sentence length, not clarity. Domain terms (Universal Thermal Climate Index) inflate grade levels.
- Metrics can invite gaming, such as splitting sentences to hit a score.
- TextDescriptives' slow release cadence is a maintenance risk. textstat alone covers the essentials.

## Verdict rationale

Useful context for humans and for variant choice, but not a gate. Trial it in M4 and keep it only if the team actually reads the numbers.

Parent: [NLP quality checks](index.md)
