---
title: SQLite + FTS5 + sqlite-vec
slug: sqlite-fts5-vec
level: 3
parent: index.md
related: [comparison.md, duckdb-vss.md, lancedb.md, git-markdown-vault.md]
tags: [derived-index, full-text, vector-search, sqlite]
status: draft
updated: 2026-09-25
kind: library
verdict: adopt
fit: [M2, M3, M4, M6, M7, M10]
license: SQLite public domain; sqlite-vec MIT/Apache-2.0
maturity: mature
inspectability: high
sources:
  - title: SQLite FTS5 extension
    url: https://sqlite.org/fts5.html
    accessed: 2026-09-25
  - title: sqlite-vec releases
    url: https://github.com/asg017/sqlite-vec/releases
    accessed: 2026-09-25
  - title: sqlite-vec on PyPI
    url: https://pypi.org/project/sqlite-vec/
    accessed: 2026-09-25
  - title: SQLite vec1 extension
    url: https://sqlite.org/vec1
    accessed: 2026-09-25
---

# SQLite + FTS5 + sqlite-vec

> **TL;DR** **Adopt** as the derived index. One gitignored `index.db` holds chunk metadata tables, an FTS5 table (BM25), and a `vec0` table of embeddings. It rebuilds from the repo in seconds and ships inside any container.

## What it is
- **SQLite**: an embedded SQL database that ships with Python's stdlib.
- **FTS5**: SQLite's built-in full-text search, with a `bm25()` ranking function (k1=1.2, b=0.75 hard-coded; lower is better, so sort ascending).
- **sqlite-vec** (Alex Garcia): a `vec0` virtual table for float/int8/bit vectors with KNN queries. Stable **0.1.9** (2026-03-31). **0.1.10** alphas (April 2026) add ANN indexes (rescore, DiskANN, experimental IVF). Still pre-1.0.
- **vec1**: a newer *official* SQLite ANN extension (v0.7, IVFADC+OPQ). The SQLite team says "testing is insufficient." Treat it as a fallback to watch.

## Why it matters for gentext
The corpus is small, so brute-force KNN (the stable sqlite-vec path) is exact and fast enough, with no ANN tuning. Metadata filters (type, place, owner, sensitivity), keyword search, and semantic search all live in one SQL file we can open with `sqlite3` or Datasette.

## How it would fit
- `gentext index rebuild`: parse frontmatter → `chunks`, `variants`, `facts`, `entities`, `requirements` tables; body text → `chunks_fts`; embeddings → `chunks_vec`.
- Embeddings are cached by `sha256(text)+model` in a sidecar so rebuilds don't re-embed unchanged text (DR-0005 "expensive but reproducible").
- Hybrid retrieval: take the top k from FTS5 and from vec0, then fuse with reciprocal-rank fusion in Python.
- The same file is baked into the MCP server image at deploy ([remote-mcp-hosting.md](remote-mcp-hosting.md)).

## Strengths
- Zero ops, one file, universal, and fully inspectable.
- FTS5 is extremely mature, and it covers M7 needs such as "does 'Fresno' appear in this draft?"

## Weaknesses / risks
- sqlite-vec is single-maintainer and pre-1.0, with some API churn between releases. Pin the version, and keep a pure-NumPy fallback (a few thousand vectors fit in memory).
- Loading extensions needs a Python build with `enable_load_extension`. The `sqlite-vec` wheel handles most cases, but check macOS system Python.
- Concurrent multi-writer access is not the goal. It's a read-mostly index.

## Verdict rationale
It's the simplest thing that serves every module, and it's the easiest to throw away and rebuild. Upgrade to Postgres only when the index must be shared live ([supabase.md](supabase.md)).

Parent: [index.md](index.md)
