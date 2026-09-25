---
title: AI-detection APIs (Pangram, GPTZero, Originality.ai, Sapling, Grammarly)
slug: a-ai-detection-apis
level: 3
parent: index.md
related: [commercial-apis.md, a-sapling.md, a-grammarly.md, ../nlp-quality/stylometry-ai-detection.md, ../provenance/index.md, ../prior-art/funder-ai-policies.md]
tags: [ai-detection, slop, provenance, false-positives]
status: draft
updated: 2026-09-25
kind: service
verdict: assess
fit: [M4, M7]
license: proprietary
maturity: emerging
inspectability: low
sources:
  - title: Pangram, AI Detection API reference (async task; fraction_ai; windows)
    url: https://docs.pangram.com/api-reference/ai-detection
    accessed: 2026-09-25
  - title: Pangram, AI Detection API product page ($0.05 per 100 words; zero-retention on enterprise)
    url: https://www.pangram.com/solutions/api
    accessed: 2026-09-25
  - title: Pangram documentation (Read the Docs), Inference API (window start_index/end_index, ai_assistance_score)
    url: https://pangram.readthedocs.io/en/latest/api/rest.html
    accessed: 2026-09-25
  - title: GPTZero, Developers / API page (predict/text; document_classification; "we do not store")
    url: https://gptzero.me/developers
    accessed: 2026-09-25
  - title: Originality.ai API v3 docs
    url: https://docs.originality.ai/
    accessed: 2026-09-25
  - title: Sapling, AI Detector API
    url: https://sapling.ai/docs/api/detector/
    accessed: 2026-09-25
  - title: Karr et al., Why AI Detection Fails for Academic Integrity (arXiv 2608.11256)
    url: https://arxiv.org/abs/2608.11256
    accessed: 2026-09-25
  - title: SiliconANGLE, Superhuman buys GPTZero (2026-06-24)
    url: https://siliconangle.com/2026/06/24/grammarly-parent-superhuman-buys-ai-detector-gptzero/
    accessed: 2026-09-25
  - title: GPTZero, GPTZero vs Pangram (vendor comparison; treated as marketing)
    url: https://gptzero.me/news/gptzero-vs-pangram/
    accessed: 2026-09-25
---

# AI-detection APIs (Pangram, GPTZero, Originality.ai, Sapling, Grammarly)

> **TL;DR** **Assess, advisory only.** The detectors now return **spans** (windows or sentences), so they can mark "this paragraph reads as machine-written", which is a usable proxy for the maintainer's "AI slop" complaint. They measure *style*, not quality and not authorship. Independent 2026 results show high false positives on legitimately polished human text. Our own provenance record answers "who wrote it". If we want the heat map, Pangram has the richest window output. Sapling's detector is the cheapest because it shares a key with grammar.

## What each returns (2026-09-25)

| Vendor | Output | Granularity | Price | Data |
|---|---|---|---|---|
| **Pangram** | `fraction_ai`, `fraction_ai_assisted`, fraction human. `windows[]`: `label` (e.g. "AI-Assisted"), `ai_assistance_score`, `confidence`, `start_index`, `end_index` | Window, char offsets | $0.05 per 100 words realtime, −20% bulk; prepaid $5–$2,000 | Zero-retention "options" on enterprise |
| **GPTZero** (Superhuman since 2026-06) | `document_classification` HUMAN_ONLY / MIXED / AI_ONLY with probabilities and `confidence_category`. `highlight_sentence_for_ai` | Sentence text (no offsets seen) | API tiers exist, figures not visible *(unverified)* | "We do not store or collect the documents passed into any calls to our API"; SOC 2 |
| **Originality.ai** | AI %, sentence-level scores; plagiarism, readability, grammar and fact-check scans on the same credits | Sentence *(schema unverified)* | API from Enterprise plan $179/mo per third-party reviews *(unverified)* | Not checked |
| **Sapling** | `score`, `sentence_scores`, `token_probs` | Sentence and token | $0.005 per 1k chars | See [a-sapling](a-sapling.md) |
| **Grammarly** (beta) | `average_confidence`, `ai_generated_percentage` | Document | Enterprise only | See [a-grammarly](a-grammarly.md) |

## Accuracy: be skeptical

- Vendors publish mutually contradictory benchmarks. Pangram claims about 1 false positive in 10k–24k documents. GPTZero claims 99.3% recall and a 0.05% FPR after a January 2026 "correction", and publishes comparisons where it beats Pangram. Superhuman says its own detector "ranks first … on RAID". None of these is independent.
- **Independent:** Karr et al. (arXiv 2608.11256, 2026) found commercial detectors flagged 9–15% of *unmodified* contemporary human abstracts, and 38–80% of abstracts with minor, guideline-compliant AI polishing. Humaniser tools cut detection to under 4%. Detectors key on vocabulary density and length, not authorship. Earlier work on non-native-writer bias is covered in [stylometry-ai-detection](../nlp-quality/stylometry-ai-detection.md).
- Proposal boilerplate is exactly the "rote human text" Sapling warns gets misclassified.

## Why it still might matter

Funders and reviewers may run these tools ([funder-ai-policies](../prior-art/funder-ai-policies.md)), and a PNAS 2026 study found AI-assisted proposals read as less distinctive. A **pre-submission** "how would a detector see this?" heat map is defensive intelligence. It tells Claude which paragraphs need a voice pass. It must never be written into provenance.

## How it would fit

An optional M7 check, `detector.<vendor>`. Pangram windows map straight to `{start, end, confidence}`. GPTZero sentences are re-anchored by text-quote. The report groups them as an **advisory band** (low/med/high), with the vendor model version and the date. Excluded from any pass/fail. Cost for a 10k-word pilot draft: about $5 (Pangram) or about $0.30 (Sapling).

## Strengths

- Span output, cheap, and it mirrors what some reviewers will actually run.

## Weaknesses / risks

- Unreliable and gameable, and models change without notice (Pangram announced 2–10× API price increases with v4 *(unverified, third-party report)*).
- Consolidation: GPTZero is now inside Superhuman, so the API's future is unannounced.
- Risk of Claude "optimising for the detector" instead of for readers. Pair it with the rubric pass, never use it alone.

## Verdict rationale

Assess. Run one detector on 10 known-human and 10 known-AI Hyphae paragraphs after the pilot. Adopt it as advisory only if human false positives stay low on *our* boilerplate.

Parent: [Prose signals](index.md) · Comparison: [commercial-apis](commercial-apis.md)
