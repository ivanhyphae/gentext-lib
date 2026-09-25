---
title: Stylometry and AI-text detection
slug: stylometry-ai-detection
level: 3
parent: index.md
related: [readability-descriptives.md, hedge-booster-lexicon.md, sentence-embeddings.md]
tags: [stylometry, authorship, ai-detection, voice]
status: draft
updated: 2026-09-25
kind: technique
verdict: hold
fit: [M1, M7]
license: faststylometry MIT; stylo (R) license unverified
maturity: emerging
inspectability: low
sources:
  - title: Liang et al. (2023), GPT detectors are biased against non-native English writers (Patterns), ScienceDaily summary
    url: https://www.sciencedaily.com/releases/2023/07/230710113921.htm
    accessed: 2026-09-25
  - title: OpenAI, New AI classifier for indicating AI-written text (withdrawn 2023-07-20 for low accuracy)
    url: https://openai.com/index/new-ai-classifier-for-indicating-ai-written-text/
    accessed: 2026-09-25
  - title: Survey, Towards Possibilities & Impossibilities of AI-generated Text Detection (arXiv 2310.15264)
    url: https://arxiv.org/abs/2310.15264
    accessed: 2026-09-25
  - title: Style as a Confound, False Positives in AI Detection of Non-Native Academic Writing (arXiv 2608.26710)
    url: https://arxiv.org/abs/2608.26710
    accessed: 2026-09-25
  - title: fastdatascience/faststylometry (MIT; PyPI 1.0.15, 2025-07)
    url: https://github.com/fastdatascience/faststylometry
    accessed: 2026-09-25
  - title: computationalstylistics/stylo (R package; repo active 2026-06)
    url: https://github.com/computationalstylistics/stylo
    accessed: 2026-09-25
---

# Stylometry and AI-text detection

> **TL;DR** **Hold** as a QA gate. Stylometry (Burrows' Delta over function-word frequencies) can *describe* voice differences between firm, partner, and agency text, which is mildly useful as an M1 hint. AI-text detectors are unreliable and biased: OpenAI withdrew its classifier over low accuracy, and perplexity detectors flag non-native writing at high rates. For "sounds like AI" concerns, use the explicit, inspectable pattern checks (hype lexicon, humanizer skill).

## What it is

- **Stylometry.** Authorship attribution from style markers: most-frequent-word profiles, character n-grams, sentence length, and function-word ratios. Burrows' Delta is the classic distance. Tools: `faststylometry` (Python, MIT, 2025-07) and `stylo` (R; the GitHub API shows no license, *CRAN license unverified*).
- **AI-text detection.** Perplexity/burstiness scoring (GPTZero-style), trained classifiers (e.g., Pangram's technical report, arXiv 2402.14873), and watermark detection (requires cooperation from the generator).

## Reliability evidence

- **OpenAI's classifier** was withdrawn on 2023-07-20 "due to its low rate of accuracy". It had flagged only 26% of AI text as "likely AI-written" and mislabeled 9% of human text.
- **Liang et al. 2023**: perplexity-based detectors misclassified non-native TOEFL essays at an average 61.3% false-positive rate, while being near-perfect on native college essays. Low lexical variety resembles "AI" text. A 2026 follow-up (arXiv 2608.26710) again frames style as a confound in academic writing.
- Surveys (arXiv 2310.15264) discuss theoretical limits: as model and human distributions converge, detection power drops, and paraphrasing evades detectors.

## Why it matters for gentext (and why hold)

- gentext *intends* to produce drafts with LLM help. Detecting "AI-ness" is not a correctness property. Unsupported claims, hype, and generic filler are, and the deterministic checks already target those.
- Funders may run detectors. Chasing a detector score is not a sound goal, and there's no reliable way to measure it anyway.
- Mixed voices (DR-0002 lesson 9) are better handled by **metadata** (`voice`, `owner`) set at ingest than inferred by stylometry. Short chunks (≤ 300 words) are also far below what stylometric attribution typically needs *(commonly cited as thousands of words; not re-verified)*.

## Acceptable limited uses

- An M1 *hint*: sentence-length, passive-ratio, and function-word profiles per segment may help a human spot where partner-authored text starts inside a working doc. Show them as features, never as a verdict.
- "AI-tell" checks as **named patterns** (stock phrases, rule-of-three padding, em-dash overuse), via the existing `humanizer` skill or a Vale style. Each hit is visible and arguable.

## Verdict rationale

Low inspectability, documented bias, and a mismatch with our actual quality goals. Hold.

Parent: [NLP quality checks](index.md)
