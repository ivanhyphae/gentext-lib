---
title: pymupdf4llm
slug: pymupdf4llm
level: 3
parent: index.md
related: [pdfplumber.md, docling.md, converter-comparison.md]
tags: [pdf, markdown, layout, tables, ocr]
status: draft
updated: 2026-09-25
kind: library
verdict: trial
fit: [M0, M5]
license: AGPL-3.0 (or commercial from Artifex)
maturity: mature
inspectability: medium
sources:
  - title: pymupdf4llm on PyPI (1.28.2, 2026-08-06)
    url: https://pypi.org/project/pymupdf4llm/
    accessed: 2026-09-25
  - title: Marker (datalab-to/marker) README, for comparison
    url: https://github.com/datalab-to/marker
    accessed: 2026-09-25
---

# pymupdf4llm

> **TL;DR** **Trial** for PDF → Markdown with headings and tables. On the guidelines PDF it produced 76 multi-level headings and a correct score table in 11.6 s on CPU, without torch. The catch is the **AGPL-3.0** licence. It is fine for internal tooling, but it needs a decision before it becomes part of any service offered to others.

## What it is
A MuPDF-based wrapper that emits Markdown, JSON or text. It now uses `pymupdf-layout` for layout analysis (multi-column reading order, header detection) and runs OCR automatically on pages that need it (it invoked Tesseract on 4 pages of the pilot). Office formats require the paid PyMuPDF Pro (PyPI, accessed 2026-09-25).

## Pilot results
- Headings come from font-size/bold heuristics. The section tree (`## 1. Background`, `#### **1.1 …**`) matches the document. Bold and underline markup leaks into heading text.
- The score-overview table became a correct 2-column pipe table. Rubric bands came out as bullets with bold labels.

## Alternatives noted
- **Marker** (datalab) gives higher-quality PDF→Markdown/JSON/chunks, with an optional `--use_llm` mode that supports Claude. Its code is Apache-2.0, but the **model weights are licensed only for research, personal use, or organizations under $5M revenue/funding** (README, accessed 2026-09-25). Hold, because of the weight licence and GPU appetite.

## Weaknesses / risks
- AGPL network clause: if gentext is ever deployed as a hosted service built on this library, obligations follow.
- Heuristic heading levels. OCR adds a Tesseract dependency and nondeterminism.

## Verdict rationale
It gives the best structure per second of anything we tried on PDFs. Use it for previews or to cross-check the pdftotext parse. Keep pdfplumber on the canonical path until the licence question is settled.

Up: [index.md](index.md)
