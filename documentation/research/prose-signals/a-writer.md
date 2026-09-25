---
title: Writer (WRITER, Palmyra)
slug: a-writer
level: 3
parent: index.md
related: [commercial-apis.md, a-sapling.md, ../nlp-quality/vale.md, ../prior-art/content-library-governance.md]
tags: [style-guide, brand-voice, terminology, llm, enterprise]
status: draft
updated: 2026-09-25
kind: platform
verdict: hold
fit: [M7]
license: proprietary
maturity: mature
inspectability: low
sources:
  - title: Writer AI Studio, pricing (Palmyra X4/X5/X6; tools; X4/X5 deprecation 2026-12-14)
    url: https://dev.writer.com/home/pricing
    accessed: 2026-09-25
  - title: Writer AI Studio, changelog (SDK 3.0.0 on 2026-06-02 removes AI detection, Medical Comprehend, context-aware splitting)
    url: https://dev.writer.com/home/changelog
    accessed: 2026-09-25
  - title: WRITER blog, New at WRITER, brand systems (May 2026)
    url: https://writer.com/blog/new-roundup-may-2026/
    accessed: 2026-09-25
  - title: Writer Help Center, Adding terms
    url: https://support.writer.com/article/69-adding-terms
    accessed: 2026-09-25
---

# Writer (WRITER, Palmyra)

> **TL;DR** **Hold.** Writer's style-guide, terminology and voice enforcement is the product closest to "brand QA", but it lives in the **Writer app and agents**, not in a checking API. The developer platform (AI Studio) sells Palmyra LLM tokens and tools. It **removed AI detection** from its SDKs in June 2026. For us it would be just another LLM plus a style guide we would have to re-author in their format.

## What it is (2026-09-25)

- **App features:** *Voice profiles*, *Terms lists* (approved and banned terms, misspelled company names, a shareable glossary), and *Style Guides* (casing, punctuation, inclusivity). Since May 2026 these combine into "brand systems" that are applied automatically to WRITER Agent and custom-agent output. The emphasis is on steering generation, not on reporting violations in arbitrary text.
- **AI Studio API:** Palmyra X6 at $2/$8 per M tokens, X5 at $0.60/$6, X4 at $2.50/$10. X4 and X5 are deprecated on **2026-12-14**. Tools listed: PDF parser, Knowledge Graph, OCR, web access. The catalogue also resells third-party models, Claude and Gemini among them.
- **Removed:** SDK 3.0.0 (2026-06-02) dropped AI detection, Medical Comprehend and Context-Aware Text Splitting.
- We found **no documented endpoint** that takes text plus a style guide and returns span-level violations *(absence not proven: enterprise docs may differ)*.

## Why it matters for adapt-rfp

Writer shows where commercial "writing QA" has gone: its terms and style guide steer the model *before* drafting instead of flagging problems afterwards. That matches our M3 glossary plus M6 prompt-time constraints, and it supports keeping the **glossary and style rules as our own plain-text data** that feed both generation and a post-hoc linter (Vale).

## How it would fit

Only as an alternative LLM or judge, which Gemini covers better given Hyphae's GCP account ([a-google-cloud-nl-vertex](a-google-cloud-nl-vertex.md)). Its style enforcement cannot be called from our MCP server as a checker.

## Strengths

- Mature terminology and brand-governance UX, well suited to large marketing teams.

## Weaknesses / risks

- Enterprise sales motion. The rules sit in a proprietary format inside their app, so they are not inspectable or diffable in git.
- Frequent API churn: tools removed, model deprecations in 2026.

## Verdict rationale

Hold. Borrow the idea (terms, voice and style as one "brand system" that drives both drafting and checking) and implement it on our own glossary and Vale styles. For a rented style-guide *checker* with offsets, trial [Sapling](a-sapling.md) instead.

Parent: [Prose signals](index.md) · Comparison: [commercial-apis](commercial-apis.md)
