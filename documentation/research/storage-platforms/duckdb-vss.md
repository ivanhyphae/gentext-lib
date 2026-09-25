---
title: DuckDB + vss
slug: duckdb-vss
level: 3
parent: index.md
related: [comparison.md, sqlite-fts5-vec.md, lancedb.md]
tags: [derived-index, analytics, vector-search, duckdb]
status: draft
updated: 2026-09-25
kind: library
verdict: assess
fit: [M4, M7, M10]
license: MIT
maturity: mature
inspectability: high
sources:
  - title: DuckDB vss extension docs
    url: https://duckdb.org/docs/current/core_extensions/vss
    accessed: 2026-09-25
  - title: duckdb-vss repository
    url: https://github.com/duckdb/duckdb-vss
    accessed: 2026-09-25
---

# DuckDB + vss

> **TL;DR** **Assess**, for analytics rather than serving. DuckDB is excellent for ad-hoc analysis of M4 features (readability distributions, reuse counts, near-duplicate clusters) and can query our SQLite index or Parquet directly. Its HNSW index persistence is still behind an experimental flag, so don't make it the primary index.

## What it is
DuckDB is an embedded columnar OLAP database (MIT). The **vss** extension adds HNSW indexes (via usearch) for `ARRAY` columns, and the `fts` extension adds BM25 full-text search.

## Why it matters for gentext
M4 produces per-chunk metrics, and M7 produces reports over drafts. Questions like "which boilerplate appears in more than 3 applications?" or "sentence-length distribution by chunk type" are analytic queries that DuckDB answers well. It can `ATTACH` the SQLite index read-only, so we get this without a second copy.

## How it would fit
An optional `gentext analyze` command or notebook that opens `index.db` through DuckDB's sqlite scanner. It isn't part of the serving path.

## Strengths
- Fast, embedded, SQL-rich (window functions, `PIVOT`), and it reads Parquet, CSV, JSON, and SQLite.
- Well maintained, large community.

## Weaknesses / risks
- **vss persistence is experimental**: HNSW indexes on disk need `SET hnsw_enable_experimental_persistence = true`. WAL recovery for custom indexes is incomplete, and a crash with uncommitted changes can corrupt the index. The index is re-serialized in full at every checkpoint.
- Two embedded engines is one more than we need for serving.

## Verdict rationale
Right tool for analysis, wrong tool for the canonical index in 2026. Revisit if vss persistence graduates from experimental.

Parent: [index.md](index.md)
