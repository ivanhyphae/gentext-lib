---
title: Hosted vector databases (Turbopuffer, Pinecone, Qdrant)
slug: hosted-vector-dbs
level: 3
parent: index.md
related: [comparison.md, sqlite-fts5-vec.md, lancedb.md, supabase.md]
tags: [vector-search, saas, hosted]
status: draft
updated: 2026-09-25
kind: service
verdict: hold
fit: [M6, M10]
license: Turbopuffer and Pinecone proprietary; Qdrant Apache-2.0 (engine)
maturity: mature
inspectability: low
sources:
  - title: turbopuffer pricing
    url: https://turbopuffer.com/pricing
    accessed: 2026-09-25
  - title: Pinecone, updated free plan
    url: https://www.pinecone.io/blog/updated-free-plan/
    accessed: 2026-09-25
  - title: Qdrant pricing
    url: https://qdrant.tech/pricing/
    accessed: 2026-09-25
---

# Hosted vector databases (Turbopuffer, Pinecone, Qdrant)

> **TL;DR** **Hold.** These services are built for millions to billions of vectors. We'll have thousands. They add a vendor, a copy of confidential text or embeddings, and a network hop, and our corpus gets nothing in return. If we ever need hosted vectors, pgvector in the Postgres we'd adopt anyway ([supabase.md](supabase.md)) is the better choice.

## What they are (2026-09, pricing via vendor pages and secondary summaries)
- **Turbopuffer**: object-storage-first serverless vector + full-text search. Plans are monthly *minimums* on metered usage. The Launch minimum reportedly dropped from $64 to $16 in June 2026 *(secondary; verify)*. Scale is $256 and Enterprise $4,096+.
- **Pinecone**: managed vector DB. The free Starter tier offers about 2 GB storage, 5 indexes, 2M write / 1M read units per month, AWS us-east-1 only, paused after 3 weeks idle *(secondary; verify)*.
- **Qdrant**: open-source engine (Apache-2.0, self-hostable) plus Qdrant Cloud. The free cluster is 1 GB RAM / 4 GB disk, suspended after 1 week idle and deleted after 4 weeks *(secondary; verify)*.

## Why it matters for gentext
Mostly it doesn't, at our scale. The one legitimate draw is having a hosted index that the MCP server can query without redeploying, but Postgres + pgvector gives us that along with our metadata tables.

## Strengths
- Mature ANN, managed ops, and hybrid search on Turbopuffer and Qdrant.
- Qdrant can be self-hosted if a dedicated engine were ever needed.

## Weaknesses / risks
- Inspectability is low: an opaque hosted index.
- Free tiers pause or delete when idle, which is a bad fit for a proposal library used in bursts.
- Embeddings of confidential text are still derived confidential data (DR-0004).
- Metadata filters end up split between two systems.

## Verdict rationale
Solves a scale problem we won't have. Revisit only if the library grows by more than two orders of magnitude, for example if we start indexing raw source archives.

Parent: [index.md](index.md)
