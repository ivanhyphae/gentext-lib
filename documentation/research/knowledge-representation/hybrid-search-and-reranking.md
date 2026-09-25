---
title: Hybrid search and reranking (FTS5, sqlite-vec, Voyage, Cohere)
slug: hybrid-search-and-reranking
level: 3
parent: index.md
related: [retrieval-design.md, contextual-retrieval.md]
tags: [retrieval, bm25, embeddings, rerank, sqlite]
status: draft
updated: 2026-09-25
kind: technique
verdict: trial
fit: [M4, M6, M7, M10]
license: SQLite public domain; sqlite-vec Apache-2.0 OR MIT; Voyage/Cohere commercial APIs
maturity: mature
inspectability: medium
sources:
  - title: SQLite FTS5 (bm25 function)
    url: https://www.sqlite.org/fts5.html
    accessed: 2026-09-25
  - title: asg017/sqlite-vec (GitHub)
    url: https://github.com/asg017/sqlite-vec
    accessed: 2026-09-25
  - title: Embeddings (Claude platform docs)
    url: https://platform.claude.com/docs/en/build-with-claude/embeddings
    accessed: 2026-09-25
  - title: Voyage AI pricing
    url: https://docs.voyageai.com/docs/pricing
    accessed: 2026-09-25
  - title: "rerank-2.5 and rerank-2.5-lite (Voyage blog, 2025-08-11)"
    url: https://blog.voyageai.com/2025/08/11/rerank-2-5/
    accessed: 2026-09-25
  - title: Introducing Rerank 4 (Cohere blog)
    url: https://cohere.com/blog/rerank-4
    accessed: 2026-09-25
---

# Hybrid search and reranking (FTS5, sqlite-vec, Voyage, Cohere)

> **TL;DR** Adopt SQLite FTS5 BM25 now, since it is in the stdlib `sqlite3` build *(typical; verify FTS5 is compiled in)* and explainable. Trial embeddings (Voyage `voyage-4` family) fused with BM25 by reciprocal rank fusion, plus a reranker (Voyage `rerank-2.5` or Cohere Rerank 4), once the conditions in [retrieval-design.md](retrieval-design.md) are met. Anthropic does not offer its own embedding model, and its docs point to Voyage. `voyage-4-nano` is open-weight (Apache-2.0), which gives a local option for sensitive text.

## What it is
- **FTS5**: SQLite's full-text index. `bm25(table, w1, w2, …)` ranks matches with per-column weights (k1=1.2, b=0.75) ([sqlite.org](https://www.sqlite.org/fts5.html), accessed 2026-09-25).
- **sqlite-vec**: a vector search SQLite extension in pure C (Apache-2.0 OR MIT), with float, int8 and binary vectors. It is **pre-v1: "expect breaking changes"** ([GitHub](https://github.com/asg017/sqlite-vec), accessed 2026-09-25). At our size, numpy brute force is an equally good fallback.
- **Anthropic embeddings guide**: "Anthropic does not offer its own embedding model". It recommends Voyage `voyage-4` / `-large` / `-lite`, lists `voyage-4-nano` as open-weight on Hugging Face (Apache-2.0), lists `voyage-context-4` (contextualized chunk embeddings, 120k context), and recommends `rerank-2.5` "for most applications" ([platform.claude.com](https://platform.claude.com/docs/en/build-with-claude/embeddings), accessed 2026-09-25).
- **Voyage** (as of 2026-09-25): `voyage-4-large` $0.12, `voyage-4` $0.06 and `voyage-4-lite` $0.02 per M tokens, plus `voyage-context-4`. Rerankers: `rerank-3` $0.05 and `rerank-3-lite` $0.02 (200M free tokens each), and `rerank-2.5`/`-lite` ([pricing](https://docs.voyageai.com/docs/pricing), accessed 2026-09-25). rerank-2.5 is instruction-following, meaning it accepts a natural-language steer such as "prefer chunks with community quotes" ([blog](https://blog.voyageai.com/2025/08/11/rerank-2-5/)).
- **Cohere Rerank 4** (Pro and Fast, released 2025-12-11): 32k per-document context, 100+ languages. Prices are reported at about $0.0025 (Pro) and $0.002 (Fast) per search (secondary sources; see [Cohere](https://cohere.com/blog/rerank-4), accessed 2026-09-25).

## Why it matters for adapt-rfp
BM25 wins on exact tokens (acronyms, tract ids, "hsCRP"). Embeddings win on paraphrase, such as matching a rubric descriptor ("community voices… quotes or stories") to chunks that never use those words. A reranker scores query and chunk *jointly*, which fixes most fusion noise, and it is the cheapest quality lever in Anthropic's Contextual Retrieval results ([contextual-retrieval.md](contextual-retrieval.md)).

## How it would fit
```
index.sqlite:  chunks(meta…)  chunks_fts(title, summary, body)  vec_chunks(embedding)
search(q, filters) → WHERE filters → top-50 BM25 ∪ top-50 vector → RRF → rerank top-30 → top-k
```
- Embed per *variant*, prefixed with type, summary, places and orgs (a deterministic "contextual" prefix).
- Cache embeddings keyed by the variant text's sha256, so a rebuild only embeds changed text.
- Keep every score in the result for audit.

## Strengths
- One file, no server, rebuildable from git (DR-0005).
- API costs are negligible for a corpus under 1M tokens.

## Weaknesses / risks
- API calls send text off the machine, so restrict them by `sensitivity` (DR-0004).
- Embedding scores are less explainable than BM25 (medium inspectability).
- Model names and prices change fast (date-sensitive). Pin the model id in config and re-embed on upgrade.

## Verdict rationale
BM25 is adopt. Embeddings and rerank are trial, gated on a small recall eval.

Up: [knowledge representation](index.md)
