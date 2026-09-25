---
title: Anthropic Contextual Retrieval
slug: contextual-retrieval
level: 3
parent: index.md
related: [retrieval-design.md, hybrid-search-and-reranking.md]
tags: [retrieval, anthropic, embeddings, bm25, prompt-caching]
status: draft
updated: 2026-09-25
kind: technique
verdict: adopt
fit: [M4, M6]
license: n/a (technique)
maturity: mature
inspectability: high
sources:
  - title: Introducing Contextual Retrieval (Anthropic, 2024-09-19)
    url: https://www.anthropic.com/news/contextual-retrieval
    accessed: 2026-09-25
---

# Anthropic Contextual Retrieval

> **TL;DR** Anthropic's technique prepends 50–100 tokens of chunk-specific context before embedding and BM25 indexing. It cut retrieval failures by 35% with embeddings alone, 49% combined with BM25, and 67% with reranking. The same post advises skipping RAG entirely under ~200k tokens. Adopt both lessons: use our curated metadata as the context prefix (no extra LLM pass), and prefer stuffing a filtered slice into the prompt over retrieval where it fits.

## What it is
From Anthropic's 2024-09-19 post: Claude writes a short context for each chunk ("this chunk is from X's Q2 filing, discussing…"), and that context is prepended before both embedding and BM25 indexing. Reported top-20 retrieval failure rates were 5.7% → 3.7% (contextual embeddings), → 2.9% (+ contextual BM25), → 1.9% (+ reranking). For knowledge bases under about 200,000 tokens (about 500 pages), the post recommends including the whole knowledge base in the prompt, with prompt caching to cut latency (>2×) and cost (up to 90%) ([anthropic.com](https://www.anthropic.com/news/contextual-retrieval), accessed 2026-09-25).

## Why it matters for adapt-rfp
- Chunks cut from working documents lose context ("the park", "the District"). The fix is the same whether an LLM writes the context or a human curates it.
- Our chunks carry `type`, `summary`, `places`, `orgs` and `programs`. Rendering those as a header line gives most of the benefit deterministically and inspectably.
- The 200k-token rule of thumb tells us that retrieval infrastructure is optional for the pilot (15–25 chunks) and for most filtered queries later.

## How it would fit
- Index-time text: `"[method] UTCI microclimate modeling. Places: none (funder-neutral). Summary: …\n\n" + body`.
- Optional LLM-written `context` for chunks whose summary is thin. Store it in frontmatter as `retrieval_context`, reviewed like any other field, so it stays canonical and diffable.
- M6 compose: if `sum(tokens(filtered candidates)) < budget`, pass them all to Claude with prompt caching. Otherwise run the hybrid search funnel.

## Strengths
- Simple and first-party, with a measured effect.
- Works with any embedding model or reranker.

## Weaknesses / risks
- The numbers come from Anthropic's own benchmarks on other corpora. Our gains are unmeasured.
- LLM-generated context can itself leak or hallucinate, which is why we review it or use curated metadata.
- The 200k threshold predates newer long-context models. Treat it as a heuristic *(date-sensitive)*.

## Verdict rationale
Adopt the prefix idea (curated form) and the "fits in context → don't retrieve" rule.

Up: [knowledge representation](index.md)
