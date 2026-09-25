---
title: pdfplumber (with pdftotext)
slug: pdfplumber
level: 3
parent: index.md
related: [pymupdf4llm.md, converter-comparison.md, claude-pdf-files-api.md]
tags: [pdf, tables, text-layer, solicitations]
status: draft
updated: 2026-09-25
kind: library
verdict: adopt
fit: [M0, M5]
license: MIT
maturity: mature
inspectability: high
sources:
  - title: pdfplumber on GitHub
    url: https://github.com/jsvine/pdfplumber
    accessed: 2026-09-25
  - title: pdfplumber on PyPI (0.11.10, 2026-06-15)
    url: https://pypi.org/project/pdfplumber/
    accessed: 2026-09-25
---

# pdfplumber (with pdftotext)

> **TL;DR** **Adopt** as the deterministic PDF pair. Use `pdftotext -layout` (already installed) for the text layer that the rubric regex reads, and pdfplumber for the few real tables and for character-level geometry when a regex needs it. Both are pure text-layer tools with no models, and their output is fully reproducible.

## What it is
pdfplumber is a Python library on pdfminer.six. It exposes characters, lines and rectangles with coordinates, has a configurable table finder (`extract_tables`, with line and text strategies), and offers visual debugging images. MIT. `pdftotext` comes from poppler.

## Pilot results (guidelines PDF)
- `pdftotext -layout` gives clean bullets for every Appendix F question and rubric band. Page breaks (`\f`) give page locators for the manifest.
- `pdfplumber.extract_tables()` over pp. 43–50 took 0.8 s. The score-overview table came out as a 17×6 grid, including spurious empty columns that need cleanup. Rubric pages came out as 1-column "tables", because bordered text boxes look like tables to the line strategy. **Treat table output as candidates, not truth.**

## How it would fit
M5 extractor: `pdftotext` → normalise wrapped lines → regex for `Question N`, `[Points available: X; Limit: Y words]`, `High|Medium|Low (a-b points):` → YAML draft → human review. Use pdfplumber only for grids (budget tables, score overview).

## Strengths
- Fast, deterministic and explainable. Every value has a page and bbox.
- No AGPL concerns (compare [pymupdf4llm](pymupdf4llm.md)).

## Weaknesses / risks
- No reading-order or heading inference. Scanned PDFs need OCR elsewhere.
- Table settings need tuning per document family.

Up: [index.md](index.md)
