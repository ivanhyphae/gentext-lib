---
title: Web Annotation selectors and brat standoff
slug: web-annotation-selectors
level: 3
parent: index.md
related: [span-anchoring.md, fuzzy-anchoring.md, inline-markup.md]
tags: [standoff, annotation, w3c, selectors]
status: draft
updated: 2026-09-25
kind: standard
verdict: adopt
fit: [M2, M6, M7, M9]
license: W3C Document License (spec); brat MIT (unverified)
maturity: mature
inspectability: high
sources:
  - title: Web Annotation Data Model (W3C Recommendation, 23 Feb 2017)
    url: https://www.w3.org/TR/annotation-model/
    accessed: 2026-09-25
  - title: brat standoff format
    url: https://brat.nlplab.org/standoff.html
    accessed: 2026-09-25
---

# Web Annotation selectors and brat standoff

> **TL;DR** Standoff annotation keeps the text pristine and puts pointers in a separate file. The W3C **TextQuoteSelector** (`exact`, `prefix`, `suffix`) is the robust pointer. The **TextPositionSelector** (`start`, `end`) is fast but brittle. **Adopt** quote+position as the sidecar anchor format. Borrow brat's one-line simplicity as a mental model, not its offset-only format.

## What it is

The W3C Web Annotation Data Model (Recommendation, 23 Feb 2017) defines selectors for pointing into a resource:

- **TextQuoteSelector:** `exact` is a copy of the selected text after normalization. `prefix` and `suffix` hold the text immediately before and after it, for disambiguation.
- **TextPositionSelector:** `start` (inclusive) and `end` (exclusive), counted in Unicode code points over normalized text. The spec warns it is "very brittle with regards to changes to the resource".
- Selectors can be combined or chained with `refinedBy`. A `State` can pin the version the selector was made against, which for us is a git commit.

<a id="brat-standoff"></a>**brat standoff** pairs a `.txt` file with a `.ann` file. Each line holds an ID, then a tab, then an annotation, e.g. `T1 Organization 0 4 Sony`, with an exclusive end offset. It also supports relations (`R`), attributes (`A`), normalizations to external ids (`N`), and notes (`#`). It is widely used in NLP corpora.

## Why it matters for adapt-rfp

Funder-facing prose must stay clean and paste-ready. Standoff lets us attach "I-ReLab wrote this" or "asserts fact X" without touching the text, and it survives any renderer.

## How it would fit

The `<chunk>.prov.yaml` sidecar ([schema](schema.md)) uses `exact`/`prefix`/`suffix` plus a `start` hint. `anchored_at: <commit>` plays the role of W3C `State`. We write YAML, not JSON-LD. A JSON-LD export is trivial if ever needed.

## Strengths
- Text stays untouched, so git diffs of prose stay readable.
- A quote selector is self-verifying: if `exact` isn't found, you know the anchor is stale.
- Many annotation tools and viewers already understand the W3C model.

## Weaknesses / risks
- Sidecars drift silently unless a tool re-checks them ([fuzzy anchoring](fuzzy-anchoring.md)).
- Duplicated text in a chunk makes quotes ambiguous without context.
- brat offsets break on any upstream edit. That is fine for frozen corpora, bad for living copy.

## Verdict rationale

Adopt. It is the best fit for "inspectable": a human can read a sidecar entry and find the sentence with Ctrl-F.

Up: [provenance index](index.md)
