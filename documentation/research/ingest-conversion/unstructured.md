---
title: Unstructured
slug: unstructured
level: 3
parent: index.md
related: [docling.md, heading-chunking.md]
tags: [partitioning, elements, chunking, pdf, docx]
status: draft
updated: 2026-09-25
kind: library
verdict: hold
fit: [M0, M1]
license: Apache-2.0
maturity: mature
inspectability: medium
sources:
  - title: Unstructured document elements and metadata
    url: https://docs.unstructured.io/open-source/concepts/document-elements
    accessed: 2026-09-25
  - title: unstructured on PyPI (0.27.8, 2026-09-22)
    url: https://pypi.org/project/unstructured/
    accessed: 2026-09-25
---

# Unstructured

> **TL;DR** **Hold.** It *partitions* files into a flat list of typed elements (`Title`, `NarrativeText`, `ListItem`, `Table`, …) with `parent_id`/`category_depth` hierarchy metadata, and it has title-based chunking. It overlaps Docling almost completely. Its element taxonomy is a useful reference for M1 chunk classification. Not tested hands-on.

## What it is
An open-source Python library (Apache-2.0) with a commercial platform/API on top. `partition_*` functions return elements. The docs list `Title`, `NarrativeText`, `ListItem`, `Table` (with `metadata.text_as_html`), `Header`, `Footer`, `PageBreak`, `Image`, `FigureCaption`, `Formula`, `Address`, `EmailAddress`, `UncategorizedText`, and `CompositeElement` for chunks. Metadata includes `page_number`, `parent_id`, `category_depth` and coordinates.

## Why it matters for adapt-rfp
- The element types line up with M1's *context-only* detection. `EmailAddress`/`Address` flag contact blocks, and `NarrativeText` vs `ListItem` separates prose from action items.
- Its `by_title` chunking (section-bounded chunks) is the same idea as our heading chunker *(chunking-strategy details not re-verified today)*.

## Weaknesses / risks
- The best PDF quality depends on its "hi_res" extras (detectron/OCR dependencies) or the paid API *(unverified detail)*.
- The flat element list with parent ids is less convenient than a tree.
- Its capabilities duplicate Docling's, and we would only want one heavyweight dependency.

## Verdict rationale
Borrow the taxonomy, not the dependency. Revisit only if Docling fails the trial.

Up: [index.md](index.md)
