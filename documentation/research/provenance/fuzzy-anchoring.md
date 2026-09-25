---
title: "Fuzzy re-anchoring: Hypothes.is and diff-match-patch"
slug: fuzzy-anchoring
level: 3
parent: index.md
related: [span-anchoring.md, web-annotation-selectors.md, git-blame-and-hashing.md]
tags: [anchoring, fuzzy-matching, diff, algorithm]
status: draft
updated: 2026-09-25
kind: algorithm
verdict: adopt
fit: [M2, M7, M9]
license: Apache-2.0 (diff-match-patch)
maturity: mature
inspectability: high
sources:
  - title: Fuzzy Anchoring (Hypothesis blog)
    url: https://web.hypothes.is/blog/fuzzy-anchoring/
    accessed: 2026-09-25
  - title: dom-anchor-text-quote (uses diff-match-patch for approximate matches)
    url: https://github.com/tilgovi/dom-anchor-text-quote
    accessed: 2026-09-25
  - title: anchor-quote (successor experiment, quantifiable fuzziness)
    url: https://github.com/robertknight/anchor-quote
    accessed: 2026-09-25
  - title: diff-match-patch on PyPI (tracks maintained fork)
    url: https://pypi.org/project/diff-match-patch/
    accessed: 2026-09-25
  - title: google/diff-match-patch (archived Aug 2024)
    url: https://github.com/google/diff-match-patch
    accessed: 2026-09-25
---

# Fuzzy re-anchoring: Hypothes.is and diff-match-patch

> **TL;DR** Hypothes.is keeps millions of annotations attached to web pages that change under them. It does this with quote selectors, a position hint, and approximate string matching (Bitap via diff-match-patch, later Myers bit-parallel via `approx-string-match`). **Adopt** the same approach in a ~200-line Python tool, using the `diff-match-patch` PyPI package, with stdlib `difflib` as a fallback.

## What it is

The Hypothesis anchoring strategy, from their blog and libraries:
1. Try the stored position. Check that the text there equals `exact`.
2. Otherwise search for the quote. Use fuzzy search around the expected start to find the prefix and around the expected end to find the suffix, which handles both content and structure changes.
3. `dom-anchor-text-quote` uses diff-match-patch for approximate matches. `anchor-quote` (Robert Knight) is a successor experiment with a *quantifiable* fuzziness threshold, built on Myers' bit-parallel approximate matching.

**diff-match-patch** (originally Google, 2006) provides `diff_main` (Myers diff plus cleanups), `match_main` (Bitap fuzzy match near an expected location), and `patch_*`. Google's repo was archived on 5 Aug 2024. The PyPI package now tracks a maintained fork, Apache-2.0.

## Why it matters for adapt-rfp

Chunks get edited, shortened, and round-tripped. Without re-anchoring, span sidecars rot after the first edit. With it, small edits (typo fixes, "the"→"a", punctuation) keep provenance attached automatically. Larger rewrites surface as orphans for a human.

## How it would fit

`adapt-rfp prov check` (M2/M7) runs on commit and on harvest (M9):
- `match_main(text, exact, loc=start_hint)` gives a candidate. Score the candidate plus its prefix and suffix with a normalized edit ratio.
- Tune `Match_Threshold` (0.0 = exact, 1.0 = anything) and `Match_Distance`. Expose them in config so decisions are inspectable.
- At harvest, `diff_main(pushed, returned)` gives sentence-level change classes: unchanged, edited, new, deleted.

## Strengths
- Proven at scale in Hypothes.is. Deterministic, fast, no LLM needed (DR-0003 principle).
- Scores are explainable: "anchored with 0.91 similarity".

## Weaknesses / risks
- Bitap in diff-match-patch has a pattern-length limit (32 characters in several ports, because of bit-width) *(unverified for the Python port; test it)*. Long sentences may need chunked matching or `difflib.SequenceMatcher`.
- Thresholds are a judgment call. Set too loose, a span jumps to a similar boilerplate sentence.
- The archived upstream means relying on a fork.

## Verdict rationale

Adopt. It is the smallest mechanism that makes standoff provenance survive real editing.

Up: [provenance index](index.md)
