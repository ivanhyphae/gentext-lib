---
title: Docling
slug: docling
level: 3
parent: index.md
related: [converter-comparison.md, pandoc.md, heading-chunking.md, unstructured.md]
tags: [docx, pdf, layout, tables, chunking, json]
status: draft
updated: 2026-09-25
kind: library
verdict: trial
fit: [M0, M1, M5]
license: MIT
maturity: emerging
inspectability: medium
sources:
  - title: Docling GitHub repository
    url: https://github.com/docling-project/docling
    accessed: 2026-09-25
  - title: Docling chunking concepts
    url: https://docling-project.github.io/docling/concepts/chunking/
    accessed: 2026-09-25
  - title: docling on PyPI (2.130.0, 2026-09-22)
    url: https://pypi.org/project/docling/
    accessed: 2026-09-25
---

# Docling

> **TL;DR** **Trial.** IBM-originated (now LF AI & Data) converter with one typed document model, `DoclingDocument`, for DOCX and PDF, plus structure-aware chunkers. On the pilot it produced the cleanest heading hierarchy and useful heading breadcrumbs per chunk. It is heavy (1.6 GB venv with CPU torch), and its PDF path is slow on CPU.

## What it is
A Python library and CLI. It parses PDF (layout model, reading order, TableFormer tables, optional OCR/VLM), DOCX, PPTX, XLSX, HTML and more into `DoclingDocument`. That model can be exported to Markdown, HTML, JSON or DocTags. MIT licence, LF AI & Data hosted (repo, accessed 2026-09-25).

## Why it matters for adapt-rfp
- **Typed items:** `TitleItem`, `SectionHeaderItem`, `TextItem`, `ListItem`, `TableItem`, `PictureItem`, each with provenance (page/bbox for PDF). On the Ambrose DOCX it found 7 titles, 123 section headers, 524 list items and 4 tables, and it mapped the tab-like `Title` paragraphs to `#`.
- **Chunkers:** `HierarchicalChunker` gives one chunk per element (list items merged). `HybridChunker` splits oversized chunks and merges undersized peers with the same headings, using a tokenizer you choose (align it with the embedding model). `contextualize()` prepends heading and caption metadata for embedding (docs). On the pilot it made 170 chunks, median 81 words, each with a heading path such as `[doc title, Introduction, subsection]`.
- **One model for DOCX and solicitation PDFs**, which simplifies M1.

## How it would fit
M0 alternate converter and M1 structural backbone: store `export_to_dict()` JSON as derived data, and derive chunk candidates from `HybridChunker` with heading paths. Compare them against pandoc-based segmentation on the pilot.

## Strengths
- The richest structural model we tested, and actively released (2.130.0 on 2026-09-22).
- On PDF pages 40–50 it rebuilt the score table correctly.

## Weaknesses / risks
- **Weight:** torch plus model downloads (layout and RapidOCR weights fetched on first run). That is not viable inside Claude web. Run it locally or in CI.
- **Speed:** 122 s for 11 PDF pages on CPU on the first run. DOCX took 4.9 s.
- The PDF heading levels came out flat (every heading `##`).
- Comments were not seen in the output. The JSON is large, so it is inspectable but not pleasant to diff.
- Fast release cadence means API churn. Pin the version.

## Verdict rationale
It is powerful, and its chunk model is close to what M1 needs. It has to earn its weight against pandoc plus our own heading chunker.

Up: [index.md](index.md)
