---
title: AI-text detectors as a signal (Binoculars, EditLens, commercial detectors)
slug: s-ai-detectors
level: 3
parent: index.md
related: [ai-slop.md, a-ai-detection-apis.md, m-perplexity.md, ../nlp-quality/stylometry-ai-detection.md, ../provenance/index.md]
tags: [ai-detection, binoculars, editlens, pangram, gptzero, originality, false-positives]
status: draft
updated: 2026-09-25
kind: technique
verdict: hold
fit: [M7]
license: Binoculars BSD-3-Clause; EditLens weights CC BY-NC-SA 4.0; Pangram/GPTZero/Originality proprietary
maturity: mature
inspectability: low
sources:
  - title: Hans et al. Spotting LLMs With Binoculars (ICML 2024; arXiv 2401.12070)
    url: https://arxiv.org/abs/2401.12070
    accessed: 2026-09-25
  - title: ahans30/Binoculars repository (BSD-3-Clause; Falcon-7B observer/performer)
    url: https://github.com/ahans30/Binoculars
    accessed: 2026-09-25
  - title: Thai, Emi, Masrour, Iyyer. EditLens, Quantifying the Extent of AI Editing in Text (arXiv 2510.03154; ICLR 2026)
    url: https://arxiv.org/abs/2510.03154
    accessed: 2026-09-25
  - title: pangramlabs/EditLens (weights CC BY-NC-SA 4.0)
    url: https://github.com/pangramlabs/EditLens
    accessed: 2026-09-25
  - title: Jabarian and Imas. Artificial Writing and Automated Detection (NBER w34223, 2025-09)
    url: https://www.nber.org/papers/w34223
    accessed: 2026-09-25
  - title: Liang et al. GPT detectors are biased against non-native English writers (arXiv 2304.02819)
    url: https://arxiv.org/abs/2304.02819
    accessed: 2026-09-25
  - title: Style as a Confound, False Positives in AI Detection of Non-Native Academic Writing (arXiv 2608.26710)
    url: https://arxiv.org/abs/2608.26710
    accessed: 2026-09-25
  - title: Different Time, Different Language, Revisiting the Bias Against Non-Native Speakers in GPT Detectors (arXiv 2602.05769)
    url: https://arxiv.org/abs/2602.05769
    accessed: 2026-09-25
  - title: RAID, A Shared Benchmark for Robust Evaluation of Machine-Generated Text Detectors (arXiv 2405.07940)
    url: https://arxiv.org/abs/2405.07940
    accessed: 2026-09-25
---

# AI-text detectors as a signal

> **TL;DR** **Hold as a quality signal for our own drafts.** Detectors answer "did a model produce this?", and for us the answer is already known and recorded in provenance. They do not answer "is this bad?". The best commercial detector (Pangram) now has very low false-positive rates in independent tests. But detector scores on *professionally edited* human text swing from 0% to 100% depending on the tool, and polish itself raises scores. That makes them the wrong target for a firm whose goal is polished prose. Our one legitimate use is an occasional **pre-submission risk check** ("would a funder's detector flag this?"). Vendor details are in [a-ai-detection-apis](a-ai-detection-apis.md).

## What exists

| Detector | Type | Output | Access |
|---|---|---|---|
| **Binoculars** | zero-shot; ratio of perplexity to cross-perplexity between two LMs (Falcon-7B / -Instruct) | document score + threshold | BSD-3; needs two 7B models (about 28 GB fp16, not run on our 16 GB GPU) |
| **EditLens** (Pangram / UMass) | regression on the *amount* of AI editing, not binary | document score 0–1 + bucket | weights CC BY-NC-SA, **non-commercial** |
| **Pangram** | trained classifier | windows/sentences, 4 tiers | paid API; per-word pricing ([sibling card](a-ai-detection-apis.md)) |
| **GPTZero** | classifier + perplexity features | document, paragraph, sentence probabilities; `highlight_sentence_for_ai` | paid API |
| **Originality.ai** | classifier | document + highlights *(details unverified)* | paid API |
| Perplexity alone | small local LM | per-token surprisal | see [m-perplexity](m-perplexity.md) |

## Accuracy and false positives (what the evidence says)

- **Binoculars** reports >90% detection of ChatGPT text at 0.01% FPR across domains (paper). The README warns against use "without human supervision" and calls it academic-only.
- **Jabarian & Imas (NBER, 2025-09)** tested Pangram, Originality, GPTZero and an open RoBERTa detector. Only Pangram met a strict FPR ≤ 0.005 while keeping FNR low, including on short passages and humanizer-processed text. GPTZero and Originality kept FPR ≤ 1% on medium and long passages and under 3% on short ones. The open RoBERTa detector was far worse.
- **RAID** (600k+ texts, 11 generators, 11 attacks): detectors that excel in-domain degrade under shifts in domain, generator and attack.
- **Non-native and formal writing**: Liang et al. 2023 found 61% of TOEFL essays flagged by seven early detectors. A 2026 Czech replication found no such bias in modern detectors. But arXiv 2608.26710 (13 detectors, 135k non-native / native-edited pairs) found FPRs from **0% to 100%** by tool, with score changes tracking the *amount of professional editing*, and the direction varied by detector. Proposal prose is formal, edited and templated, which is exactly the confound.
- **EditLens** reframes detection as "how much AI editing", and it tracks edit magnitude better than binary Pangram (r 0.606 vs 0.491 on APT-Eval). That is closer to our reality of mixed authorship, but it is still not a quality measure.

## Why hold for adapt-rfp

1. **Wrong question.** Provenance (DR-0008) records which model wrote which span. A detector's guess adds nothing to that, and the [Wikipedia guide](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing) itself cautions against relying on detectors.
2. **Wrong gradient.** Rewriting to lower a detector score rewards "humanizer" tricks (odd word choice, injected errors) over clarity and specificity. The [slop lexicons](s-slop-lexicons.md) and [LAMP categories](s-edit-based-rewards-lamp.md) point at *fixable* problems.
3. **Low inspectability.** An opaque classifier gives no category, no fix and no reason.
4. **Confidentiality.** This is relaxed for public-bound text, but the sibling card covers vendor data policies.

## Acceptable limited uses

- **Pre-submission risk check**, run by a human on final text: if a funder is known to screen with Pangram or GPTZero, look at the flagged windows, then fix them using the slop taxonomy, not the score. Record the result as a `detector.kind: model` finding at `info` severity.
- **Calibration research**: correlate detector windows with our LLM-annotated slop spans on the gold set. If they agree, the detector is a cheap *locator*. If not, we have learned that too.

## Verdict rationale

Hold as a gate or an optimization target. At most, assess one commercial detector as an occasional risk heat map, with findings that are advisory and non-blocking.

Parent: [Prose signals](index.md) · Up: [AI slop](ai-slop.md)
