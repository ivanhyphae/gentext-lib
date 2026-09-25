---
title: Heading-path structural chunking
slug: heading-chunking
level: 3
parent: index.md
related: [docling.md, pandoc.md, contextual-retrieval.md, unstructured.md]
tags: [segmentation, chunking, headings, m1]
status: draft
updated: 2026-09-25
kind: technique
verdict: adopt
fit: [M1, M2]
license: n/a
maturity: mature
inspectability: high
sources:
  - title: Docling chunking concepts (HierarchicalChunker, HybridChunker)
    url: https://docling-project.github.io/docling/concepts/chunking/
    accessed: 2026-09-25
  - title: LangChain MarkdownHeaderTextSplitter
    url: https://docs.langchain.com/oss/python/integrations/splitters/markdown_header_metadata_splitter
    accessed: 2026-09-25
  - title: langchain-text-splitters on PyPI (1.1.2)
    url: https://pypi.org/project/langchain-text-splitters/
    accessed: 2026-09-25
---

# Heading-path structural chunking

> **TL;DR** **Adopt** as the M1 splitter. Split the normalised Markdown at headings, carry the full **heading path** (tab → H1 → … → Hn) as metadata, then split oversized sections at paragraph boundaries and merge tiny siblings. Write it ourselves in about 100 lines over the pandoc AST. Docling's HybridChunker and LangChain's MarkdownHeaderTextSplitter are reference implementations, not dependencies.

## What it is
Structure-first segmentation. Section boundaries come from the author's headings, and a size limit (words, not tokens, since our limits are 250/300/350 words) only makes secondary cuts. Variants:
- **Docling HierarchicalChunker:** one chunk per element, with heading and caption metadata attached. **HybridChunker** adds token-aware split and merge (`merge_peers`) plus `contextualize()` for embedding text.
- **LangChain MarkdownHeaderTextSplitter:** `headers_to_split_on=[("#","h1"),…]`, `strip_headers`. Each chunk gets its header values as metadata. Run a size splitter afterwards with `split_documents`.
- **LlamaIndex** has comparable Markdown/hierarchical node parsers *(not re-verified today)*.

## Why it matters for adapt-rfp
- Proposal prose is authored by section ("Modeling", "Monitoring", "SHORTENED VERSION"), so headings are the natural chunk unit (DR-0003 open question 1: section-level chunks).
- The heading path becomes the **locator** in `sources[]` and a strong classification feature. A path containing "Notes", "Meeting" or "Template Letter" points to context-only or template chunks.
- Deterministic and diffable. A re-run on a new export produces the same ids when the content is unchanged (id = hash of path + normalised text).

## Pilot-driven rules
1. Tab boundary (`Title` custom-style) = level-0 heading.
2. Drop the TOC, empty headings and pure-formatting headings, and merge consecutive same-level heading paragraphs.
3. Detect `SHORTENED VERSION` and similar markers to link length variants (`shortened-from`).
4. For style-less forms (Urban Greening), synthesise headings from numbered question patterns.
5. Near-duplicate pass (MinHash on shingles) across sources after splitting, so forked docs collapse into variants.

## Weaknesses / risks
- It depends on authors using heading styles. The form document shows that fallback heuristics are needed.
- Long unstructured sections need a paragraph-level fallback.

Up: [index.md](index.md)
