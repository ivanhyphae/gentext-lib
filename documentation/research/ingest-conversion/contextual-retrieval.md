---
title: Contextual retrieval and late chunking
slug: contextual-retrieval
level: 3
parent: index.md
related: [heading-chunking.md, claude-pdf-files-api.md]
tags: [retrieval, embeddings, chunking, context]
status: draft
updated: 2026-09-25
kind: technique
verdict: trial
fit: [M4, M6]
license: n/a
maturity: emerging
inspectability: medium
sources:
  - title: Anthropic, Introducing Contextual Retrieval (2024-09-19)
    url: https://www.anthropic.com/news/contextual-retrieval
    accessed: 2026-09-25
  - title: "Günther et al., Late Chunking: Contextual Chunk Embeddings Using Long-Context Embedding Models (arXiv:2409.04701)"
    url: https://arxiv.org/abs/2409.04701
    accessed: 2026-09-25
---

# Contextual retrieval and late chunking

> **TL;DR** **Trial** contextual retrieval: before embedding and BM25 indexing, prepend a short, LLM-written description that places each chunk within its source. Anthropic reports 35% fewer retrieval failures with contextual embeddings, 49% with contextual BM25 added, and 67% with reranking. For adapt-rfp, the heading path already supplies much of that context deterministically. Try that first, then add LLM context where it helps. **Assess** late chunking.

## What they are
- **Contextual retrieval (Anthropic, 2024-09-19):** for each chunk, a model is given the whole document plus the chunk and asked for 50–100 tokens of situating context. The context is prepended before embedding and BM25. The reported top-20 failure rate fell from 5.7% to 3.7%, then 2.9%, then 1.9% with reranking. Prompt caching made the one-off cost about $1.02 per million document tokens (Claude 3 Haiku pricing at the time; re-price for current models).
- **Late chunking (Jina, arXiv 2409.04701):** embed the whole document with a long-context embedding model, then pool token embeddings per chunk, so each chunk vector carries document context without extra LLM calls. It requires a long-context embedder with token-level output.

## Why it matters for adapt-rfp
Chunks like "our team has done this in three counties" are ambiguous on their own. Context such as "Hyphae firm-experience boilerplate, Bay Point EHCRP working doc, tab Pre-application" improves retrieval in M6 and similarity in M4. It also helps catch **context leakage** (the "Fresno County" case), because the situating text names the source place.

## How it would fit
- Level 1 (deterministic): `contextualize = tab › heading path + doc title + funder/place from the manifest`. This is Docling's `contextualize()` idea.
- Level 2 (LLM): Claude-generated context, stored as a derived field with the prompt version and the model id, so it can be audited and rebuilt.

## Weaknesses / risks
- LLM-generated context can introduce claims. Keep it out of canonical chunk text.
- Late chunking ties us to one embedder's API and is harder to inspect.

Up: [index.md](index.md)
