---
title: Sapling API
slug: a-sapling
level: 3
parent: index.md
related: [commercial-apis.md, a-languagetool-api.md, a-ai-detection-apis.md, ../nlp-quality/vale.md]
tags: [grammar, style-guide, tone, ai-detection, api, span-offsets]
status: draft
updated: 2026-09-25
kind: service
verdict: trial
fit: [M4, M7]
license: proprietary (cloud API; self-hosted on Enterprise)
maturity: mature
inspectability: medium
sources:
  - title: Sapling, API overview (endpoint list)
    url: https://sapling.ai/docs/api/
    accessed: 2026-09-25
  - title: Sapling, Edits overview (request parameters, response fields)
    url: https://sapling.ai/docs/api/edits-overview/
    accessed: 2026-09-25
  - title: Sapling, API pricing (edits, detector, tone, style guide compliance)
    url: https://sapling.ai/docs/api/pricing/
    accessed: 2026-09-25
  - title: Sapling, API access (trial 50,000 chars / 24 h; prepaid credits)
    url: https://sapling.ai/docs/api/api-access/
    accessed: 2026-09-25
  - title: Sapling, AI Detector API (doc/sentence/token scores; stated caveats)
    url: https://sapling.ai/docs/api/detector/
    accessed: 2026-09-25
  - title: Sapling, Self-hosting overview
    url: https://sapling.ai/docs/onprem/overview/
    accessed: 2026-09-25
  - title: Sapling, HIPAA page (no-data-retention option for enterprise; via search summary)
    url: https://nyc.sapling.ai/hipaa
    accessed: 2026-09-25
  - title: Sapling, Migrating from the Grammarly Text Editor SDK
    url: https://sapling.ai/docs/sdk/Integration%20Details/grammarly-migration/
    accessed: 2026-09-25
---

# Sapling API

> **TL;DR** **Trial.** Sapling is the most developer-friendly rented writing-feedback API in 2026. It is self-serve, pay per character, and has a free trial key. It returns **span-level** grammar/spelling edits with error categories, a **style-guide compliance** check (your rules in, violations with offsets and rewrites out), tone scoring, and an AI detector with document, sentence and token scores. It is the best candidate for the rented grammar layer and a cheap way to test "style-guide-as-a-service" against our Vale rules.

## What it returns

**Edits** (`POST /api/v1/edits`): up to 100k chars per request (it recommends chunks ≤4k). Each edit has:

```
id, sentence, sentence_start, start, end, replacement, error_type, general_error_type
```

`start`/`end` are **relative to the sentence**. The document offset is `sentence_start + start`. The options are useful: `auto_apply` (returns `applied_text`), `ignore_edit_types` (articles, hyphens, punctuation…), `variety` (us/gb), `neural_spellcheck`, and `include_error_categories=false` for speed. The `id` lets you send accept/reject feedback.

**Style Guide Compliance**: checks text against rules you supply and returns "grounded violations with offsets, notes and compliant rewrite suggestions". It is priced alongside Tone and Classify. We confirmed the endpoint from the pricing and docs summaries, but did not read or run the full reference *(schema unverified)*.

**Tone**, **Rephrase**, **Plain-language simplification**, **Scoring & Classification**, **Guardrails**: also available. Simplification is relevant to plain-language requirements.

**AI Detector** (`/api/v1/aidetect`): `score` 0–1, `sentence_scores`, `token_probs`, and an optional HTML heat map. Up to 200k chars, with ≥300 chars recommended. Sapling itself warns that light edits defeat it and that "human-written (but perhaps rote) text can be misclassified". That caveat applies squarely to boilerplate-heavy proposals. See [a-ai-detection-apis](a-ai-detection-apis.md).

## Pricing and terms (2026-09-25)

| Endpoint | 0–10M chars |
|---|---|
| Edits / Rephrase | $0.025 per 1k chars |
| Tone, Style Guide Compliance | $0.02 per 1k |
| AI Detector | $0.005 per 1k |

The trial key allows 50,000 chars per 24 h with no card. Prepaid credits are $1 each. **Data:** no-retention and on-prem are Enterprise options. The docs pages we read do not state the default cloud retention *(unverified, so ask before production)*.

## How it would fit

An M7 adapter, `sapling.edits`, that converts to absolute offsets and emits `L7.sapling.<general_error_type>`, severity warning. A second adapter, `sapling.style`, would receive our glossary and style rules as the supplied guide and run *beside* Vale. Where the two disagree we get test cases in both directions. Detector sentence scores could feed an advisory "reads-as-AI" band. Tool shape: `check_prose(text, checks=["sapling.edits"])` on the FastMCP server, with the key held in server config and not exposed to Claude.

## Strengths

- Spans and categories, so there is something concrete to correct. Self-serve with low cost. Sapling explicitly courts Grammarly-SDK refugees.
- One key covers grammar, style-guide checks, tone and detection.

## Weaknesses / risks

- The model versions change silently, so log them and cache per text hash.
- The style-guide endpoint is presumably LLM-backed, so it is less deterministic than Vale.
- Small vendor, and the default retention terms are unclear.

## Verdict rationale

Trial on synthetic and promoted library text. Keep it if it finds grammar issues that spaCy and Vale miss, at an acceptable false-positive rate, on about 20 real paragraphs.

Parent: [Prose signals](index.md) · Comparison: [commercial-apis](commercial-apis.md)
