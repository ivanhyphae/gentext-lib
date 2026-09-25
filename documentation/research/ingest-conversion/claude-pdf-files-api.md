---
title: Claude PDF support and Files API
slug: claude-pdf-files-api
level: 3
parent: index.md
related: [pdfplumber.md, pymupdf4llm.md, contextual-retrieval.md]
tags: [claude, pdf, files-api, citations, llm-extraction]
status: draft
updated: 2026-09-25
kind: service
verdict: adopt
fit: [M5, M0]
license: proprietary (Anthropic API)
maturity: mature
inspectability: medium
sources:
  - title: Claude docs, PDF support
    url: https://platform.claude.com/docs/en/build-with-claude/pdf-support
    accessed: 2026-09-25
  - title: Claude docs, Files API
    url: https://platform.claude.com/docs/en/build-with-claude/files
    accessed: 2026-09-25
---

# Claude PDF support and Files API

> **TL;DR** **Adopt** for *LLM-assisted* reading of solicitations (M5): Claude gets both the text and an image of every page and can cite passages. Do **not** use it as the M0 converter. Its output is not deterministic, and DOCX is not accepted as a document block anyway. Use the Files API to upload a solicitation once and reference it by `file_id` across extraction runs.

## What it is (from the docs, accessed 2026-09-25)
- A PDF sent as a `document` block (base64, URL, or Files API `file_id`) is processed page by page. Each page is **converted to an image and its text is extracted alongside**.
- Limits: 32 MB request, **600 pages** per request (100 when the context window is under 1M tokens). Cost is roughly **1,500–3,000 text tokens per page plus image tokens**, with no PDF surcharge.
- GA on the Claude API, Bedrock, Vertex and Foundry. The Files API is not available on Bedrock or Vertex, where only base64 works.
- Plain text (`.md`, `.txt`) can be uploaded as `text/plain` document blocks. `.docx`/`.xlsx` must be converted first.
- Citations can point answers back to document passages.

## Why it matters for adapt-rfp
- M5 extraction (questions, word limits, points, rubric bands, budget floors) benefits from seeing layout. Citations give each extracted field a locator for human verification.
- It is available in Claude web, which is the README's end-to-end target, so a skill can hand Claude the PDF directly.

## How it would fit
The `model-solicitation` skill uploads the PDF via the Files API, extracts to the YAML schema with citations, diffs the result against the deterministic `pdftotext` regex parse, and flags disagreements for a human.

## Weaknesses / risks
- Every run costs tokens, and the result differs between runs. The canonical YAML must stay human-reviewed.
- Sensitive sources: check retention and ZDR eligibility before uploading internal working docs. The docs list PDF support as ZDR-eligible with model exceptions.

Up: [index.md](index.md)
