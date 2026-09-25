---
title: Ingest and conversion
slug: index
level: 1
parent: ../index.md
related: [converter-comparison.md, google-docs-tabs.md]
tags: [ingest, conversion, segmentation, chunking, docx, pdf, google-docs]
status: draft
updated: 2026-09-25
---

# Ingest and conversion

> **TL;DR** For DOCX, use **pandoc** (`-f docx+styles --track-changes=all`) as the deterministic M0 converter, and add a small Lua filter plus our own heading-based segmenter for M1. Run **Docling** as a trial second opinion; its DoclingDocument JSON and HybridChunker are the best off-the-shelf structural model we tested. For PDF solicitations, use `pdftotext -layout` + regex for rubric text, **pdfplumber** or **pymupdf4llm** for the few real tables, and Claude's PDF support for LLM-assisted M5 extraction that humans verify. For Google Docs, read the **Docs API with `includeTabsContent=true`**. Per-tab styles *are* exposed there, and Drive `files.export` cannot choose a tab.

## The question

M0 has to turn messy working documents into **structure-preserving Markdown + a manifest**: many-tab Google Docs exported to DOCX, solicitation PDFs, and forms with checkboxes. M1 then splits that Markdown by heading and paragraph, classifies chunks, and finds near-duplicates across forked documents (DR-0002, DR-0003). The lens is *powerful, elegant, inspectable*. The output should be diffable text, and every step should be re-runnable without an LLM.

## What we found (hands-on, pilot files, 2026-09-25)

Details are in [converter-comparison.md](converter-comparison.md).

- **Heading styles survive.** The Ambrose DOCX uses real `Heading1–5` styles. pandoc, MarkItDown and Docling all recover about 120 headings. The Urban Greening form has **no paragraph styles at all**, so its segmentation has to rely on heuristics (bold text, numbering, question patterns).
- **The export marks tab-like boundaries with `Title` paragraphs** ("Overview", "Notes", "Template Letter", "Pre-application"…). pandoc's default output flattens these to plain paragraphs. `docx+styles` keeps them as `custom-style="Title"` divs, and Docling promotes them to `#`. *(That these paragraphs mark Google Docs tab boundaries is our inference and has not been verified.)*
- **Tables:** pandoc emits HTML `<table>` for complex cells (safe, lossless), and MarkItDown forces pipe tables. The guidelines PDF's Appendix F rubric turns out to be **bulleted text, not tables**, so it is easier to parse than expected. Only the score-overview table is a real grid, and pymupdf4llm and Docling both rebuilt it correctly.
- **Comments and suggestions:** only pandoc (`--track-changes=all`) kept the 7 comments and 1 deletion in the pilot DOCX.
- **Checkboxes** in the form are Unicode glyphs (☐/☒), which every converter preserves.
- **Noise to strip:** a Google-generated TOC, empty headings, headings split across two paragraphs, and direct bold/underline formatting inside headings.

## Recommendation

| Need | Adopt | Trial | Hold |
|---|---|---|---|
| DOCX → Markdown (M0) | [pandoc](pandoc.md) | [Docling](docling.md) | [MarkItDown](markitdown.md) (lossy), [mammoth](mammoth.md) (HTML-only now) |
| Google Docs | [Docs API tabs](google-docs-tabs.md), [Apps Script exporter](apps-script-tab-export.md) as a fallback | Drive DOCX export (all tabs, via UI) | Drive `files.export` markdown for tabbed docs |
| PDF solicitations | `pdftotext -layout` + [pdfplumber](pdfplumber.md) | [pymupdf4llm](pymupdf4llm.md) (AGPL), Docling PDF | [Unstructured](unstructured.md) (heavier, overlaps Docling), Marker (model-weight licence) |
| LLM reading of PDFs (M5) | [Claude PDF + Files API](claude-pdf-files-api.md) | | |
| Segmentation (M1) | [Heading-path chunking](heading-chunking.md) | Docling HybridChunker | fixed-size splitters |
| Retrieval context (M6) | | [Contextual retrieval](contextual-retrieval.md) | late chunking (needs a long-context embedder) |

Why pandoc and not Docling as the default: pandoc is a single static binary (about 500 MB for our whole test venv, versus 1.6 GB for Docling with CPU torch). Its AST (`-t json`) is fully inspectable, it is fast (0.7 s on a 15k-word doc), and it keeps comments. Docling's advantage is its *model*. It gives typed items, a heading breadcrumb on every chunk, and one representation for DOCX and PDF. That makes it worth a trial as the segmenter's data model.

## Pages in this topic

Level 2:
- [converter-comparison.md](converter-comparison.md): side-by-side results on the pilot files.
- [google-docs-tabs.md](google-docs-tabs.md): what the Docs API, Drive export and Apps Script can and can't do with tabs.

Level 3 cards:
- [pandoc.md](pandoc.md) · [docling.md](docling.md) · [markitdown.md](markitdown.md) · [mammoth.md](mammoth.md) · [unstructured.md](unstructured.md)
- [pdfplumber.md](pdfplumber.md) · [pymupdf4llm.md](pymupdf4llm.md) · [claude-pdf-files-api.md](claude-pdf-files-api.md)
- [apps-script-tab-export.md](apps-script-tab-export.md)
- [heading-chunking.md](heading-chunking.md) · [contextual-retrieval.md](contextual-retrieval.md)

## Open questions

- Confirm that each `Title` paragraph in the DOCX export corresponds to one Google Docs tab. Test: compare it against `tabs[].tabProperties.title` from the Docs API for the same document.
- Should the canonical derived text be the pandoc JSON AST, with Markdown rendered from it, or Markdown only?
- Near-duplicate detection (MinHash via `datasketch` 2.0.0, MIT) belongs to M1, but its design lives with the similarity/embeddings topic.

Up: [../index.md](../index.md)
