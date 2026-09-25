---
title: Property graphs (Neo4j, Kùzu, NetworkX)
slug: property-graphs
level: 3
parent: index.md
related: [graph-decision.md, rdf-toolchain.md, graphrag-family.md]
tags: [graph, property-graph, cypher, neo4j, kuzu, networkx]
status: draft
updated: 2026-09-25
kind: platform
verdict: hold
fit: [M3, M10]
license: Neo4j Community GPLv3; Kùzu MIT (archived; unverified license); NetworkX BSD-3-Clause
maturity: mature
inspectability: low
sources:
  - title: Neo4j Community Edition
    url: https://neo4j.com/product/community-edition/
    accessed: 2026-09-25
  - title: kuzudb/kuzu GitHub wiki
    url: https://github.com/kuzudb/kuzu/wiki
    accessed: 2026-09-25
  - title: "Kuzu's legacy and the new wave of embedded graph databases (gdotv; secondary)"
    url: https://gdotv.com/blog/kuzu-legacy-embedded-graph-database-landscape/
    accessed: 2026-09-25
  - title: NetworkX on PyPI
    url: https://pypi.org/project/networkx/
    accessed: 2026-09-25
---

# Property graphs (Neo4j, Kùzu, NetworkX)

> **TL;DR** Hold on graph *databases*. Neo4j adds a server and an opaque store for a problem we don't have. Kùzu, the attractive embedded option, was **archived on 2025-10-10**. **NetworkX** is worth a trial as an in-memory, derived analysis tool (e.g. lineage trees, entity co-occurrence) built from the YAML on demand.

## What they are
- **Neo4j**: the leading property-graph DB (Cypher). Community Edition is GPLv3, single-server, without clustering, online backup or access control. AuraDB Free is reported as capped at 200k nodes / 400k relationships (secondary sources; see [neo4j.com](https://neo4j.com/product/community-edition/), accessed 2026-09-25).
- **Kùzu**: an embedded Cypher graph DB with built-in vector and full-text search, from the University of Waterloo. The repo was archived (read-only) on 2025-10-10 with a final release 0.11.3. Secondary reports say Apple acqui-hired the team and that maintenance has passed to community forks ([gdotv](https://gdotv.com/blog/kuzu-legacy-embedded-graph-database-landscape/), accessed 2026-09-25; secondary). Graphiti now labels its Kùzu backend "deprecated, unmaintained upstream" ([graphrag-family.md](graphrag-family.md)).
- **NetworkX 3.7** (2026-09-21, BSD-3-Clause, Python ≥3.12): an in-memory graph library for analysis, not storage ([PyPI](https://pypi.org/project/networkx/), accessed 2026-09-25).

## Why it matters for adapt-rfp
Property graphs are the usual backend for GraphRAG-style tools. Picking one pulls in a server, a non-diffable store and a sync job from git. Our queries are one-hop lookups over a few thousand nodes at most ([graph-decision.md](graph-decision.md)).

## How it would fit (if ever)
- **NetworkX (trial)**: `adapt-rfp graph` loads the registries and chunk references into a `MultiDiGraph` for a handful of reports: orphan facts, chunks with no place or org, lineage families (the forked Ambrose documents), and org co-occurrence. Nothing is persisted. It rebuilds in seconds.
- **Neo4j/others (hold)**: only if a future deployment needs a hosted multi-user graph API and the RDF view proves insufficient. Even then, it would be loaded from git, never canonical.

## Strengths
- Cypher is readable, and the tooling (Bloom, browsers) is polished.
- NetworkX adds no infrastructure, pairs well with Python checks, and is easy to test.

## Weaknesses / risks
- Vendor and maintenance risk, as Kùzu's sudden archival shows (date-sensitive).
- There is no standard interchange comparable to Turtle, so diffs and review are poor (low inspectability).
- Neo4j GPLv3 or commercial licensing matters if we ever ship it inside a product.

## Verdict rationale
Hold on graph DBs, and don't build on Kùzu. Trial NetworkX only for derived analytics.

Up: [knowledge representation](index.md)
