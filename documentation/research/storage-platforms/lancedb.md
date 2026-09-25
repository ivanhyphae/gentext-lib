---
title: LanceDB
slug: lancedb
level: 3
parent: index.md
related: [comparison.md, sqlite-fts5-vec.md, hosted-vector-dbs.md]
tags: [derived-index, vector-search, hybrid-search, embedded]
status: draft
updated: 2026-09-25
kind: library
verdict: assess
fit: [M4, M6, M10]
license: Apache-2.0
maturity: emerging
inspectability: medium
sources:
  - title: LanceDB documentation
    url: https://docs.lancedb.com/
    accessed: 2026-09-25
  - title: LanceDB site
    url: https://www.lancedb.com/
    accessed: 2026-09-25
  - title: LanceDB native full-text search
    url: https://www.lancedb.com/blog/feature-full-text-search
    accessed: 2026-09-25
---

# LanceDB

> **TL;DR** **Assess.** It's an embedded, Apache-2.0 vector database with built-in hybrid search, reranking, and dataset versioning. It's more capable than we need at our scale, and its Lance columnar files are less inspectable than a SQLite file. Keep it as the upgrade if retrieval quality work outgrows sqlite-vec.

## What it is
An in-process retrieval library on the Lance columnar format. It supports vector search (IVF-PQ/HNSW), native full-text search, hybrid search with rerankers, SQL filters, ACID with schema evolution, and automatic table versioning. There's also a commercial LanceDB Cloud/Enterprise. 2026 updates include Lance-native SQL via DuckDB and git-style branching/shallow clone for datasets (vendor blog; not verified in depth).

## Why it matters for gentext
If M6 retrieval needs reranking, multiple embedding models per chunk, or multimodal data (site photos, heat maps), LanceDB does it embedded with no server. Its versioning partly echoes our lineage needs.

## How it would fit
It would replace the `chunks_fts` and `chunks_vec` tables of the [SQLite index](sqlite-fts5-vec.md), with metadata still in SQLite or duplicated into Lance.

## Strengths
- Hybrid search and rerankers out of the box, and fast.
- Embedded Python API, and it's open source.

## Weaknesses / risks
- **Inspectability**: Lance files need LanceDB or DuckDB to read. There's no universal CLI like `sqlite3`.
- Fast-moving, VC-backed vendor ($30M Series A, June 2025), so API churn is likely.
- Overkill for hundreds to thousands of chunks.

## Verdict rationale
It's a credible "phase 1.5" retrieval engine, but it adds a format and a dependency for capabilities our corpus size doesn't yet need.

Parent: [index.md](index.md)
