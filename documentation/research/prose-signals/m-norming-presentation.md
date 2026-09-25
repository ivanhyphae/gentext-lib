---
title: Norming and presenting metrics to Claude (reference corpora, percentiles, span findings)
slug: m-norming-presentation
level: 3
parent: index.md
related: [holistic-metrics.md, m-voice-distance.md, ../nlp-quality/check-catalog.md, ../llm-evaluation/rubric-judging.md, ../llm-evaluation/judge-reliability.md]
tags: [norms, percentiles, reference-corpus, report-schema, llm-interface]
status: draft
updated: 2026-09-25
kind: technique
verdict: adopt
fit: [M4, M7]
license: n/a (design pattern)
maturity: emerging
inspectability: high
sources:
  - title: Zenker & Kyle (2021), minimum text lengths for lexical diversity indices (stability thresholds)
    url: https://www.researchgate.net/publication/346623372_Investigating_minimum_text_lengths_for_lexical_diversity_indices
    accessed: 2026-09-25
  - title: Shaib et al. (2025), Measuring AI "Slop" in Text (span-level components more reliable than binary labels)
    url: https://arxiv.org/html/2509.19163v2
    accessed: 2026-09-25
---

# Norming and presenting metrics to Claude

> **TL;DR** **Adopt.** Raw numbers ("MTLD 139", "perplexity 29") are useless or misleading to Claude and to humans. Every metric is reported as a **percentile against a named reference corpus**, with a **direction label** (what "bad" looks like for this metric), a **reliability flag** (the text is too short, or out of domain), and the **worst spans** with quotes. Claude reads the findings as evidence for its rubric pass. It never treats them as a verdict.

## Reference corpora (derived, rebuildable, per DR-0005)

| Corpus | Contents | Used for |
|---|---|---|
| `firm-exemplar` | chunks marked `exemplar: true` (≈50–100 paragraphs, firm voice) | voice distance, target bands |
| `firm-all` | all canonical library chunks | portability/boilerplate, general norms |
| `funded-public` *(optional)* | public winning proposals or funder examples, where licence allows | "what reviewers saw" bands |
| `hivemind:<question>` | cached LLM answers written without firm facts | genericness distance |
| `floor` | small synthetic/known-bad set (ungrammatical, childlike, slop) | sanity checks, calibration |

Norms are recomputed when the corpus changes, and each report records the corpus hash. Paragraph-level norms are computed on paragraph-sized units (100–300 words), so percentiles compare like with like.

## Finding shape (extends the [check catalog report](../nlp-quality/check-catalog.md))

```yaml
- metric: concreteness_mean
  scope: paragraph P2            # or sentence S4, or char span
  value: 2.71
  percentile: 4                  # vs firm-exemplar, n=64, corpus sha 3f2c…
  direction: low_is_bad
  reliability: ok                # ok | short_text | out_of_domain
  spans:
    - quote: "Hyphae Design Lab has extensive experience delivering innovative…"
      why: "no anchor; concreteness 2.3"
  hint: "Name the site, partner, or a number from M3 facts for Bay Point."
  severity: info                 # metrics are info/warning, never error
```

## Presentation rules

1. **Percentiles, not raw values.** Show the raw value in brackets for auditing.
2. **Two-sided where needed.** Grade level and sentence length have a good *band*. Lexical diversity is bad only when low: our probe found slop has the *highest* MTLD. Perplexity is ambiguous, so it is shown only next to concreteness.
3. **Spans before scores.** Each metric names its worst 1–3 spans. Claude fixes spans. Nobody can fix a score.
4. **Combine into named symptoms**, not a composite quality score. For example, *generic* = unanchored + low concreteness + portable or near-hivemind; *childlike* = grade < 8 + low MTLD + high Zipf; *broken grammar* = CoLA < p5 + LT grammar hits; *dense* = sentence length > p95 + nominalization > p90. Each symptom lists the metrics that fired.
5. **Reliability gates.** Under 50 tokens, suppress diversity metrics (Zenker & Kyle). Out-of-domain models (AES, CoLA) are always tagged as advisory.
6. **No gating on metrics.** Structural and factual checks can fail a draft. Prose-signal metrics only produce `info`/`warning`, consistent with the "scores are not decisions" finding ([judge-reliability](../llm-evaluation/judge-reliability.md)).

## How Claude uses it

The M8 skill `check-draft` returns the symptom list. Claude's rubric pass must **cite** a symptom or quote when it claims "generic" or "grammar problems". Findings it disagrees with it marks `disputed` with a reason, and those records become calibration data after the pilot.

## Weaknesses / risks

- Small exemplar sets make percentiles jumpy. Show `n`, and fall back to `firm-all` when n < 30.
- Fixing text to move percentiles can itself homogenize it. The hint text should point at *content* (facts, names), not at metric targets.

## Verdict rationale

Without norms and spans, the metrics in this folder are noise to an LLM. With them, they become quotable evidence. Adopt as the interface contract for M4 to M7.

Parent: [Prose signals](index.md) · Up: [Holistic metrics](holistic-metrics.md)
