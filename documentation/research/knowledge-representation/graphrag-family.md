---
title: GraphRAG family (Microsoft GraphRAG, LightRAG, Graphiti)
slug: graphrag-family
level: 3
parent: index.md
related: [graph-decision.md, retrieval-design.md, property-graphs.md]
tags: [graphrag, retrieval, knowledge-graph, llm-extraction]
status: draft
updated: 2026-09-25
kind: library
verdict: hold
fit: [M6]
license: GraphRAG MIT; LightRAG MIT; Graphiti Apache-2.0
maturity: emerging
inspectability: low
sources:
  - title: microsoft/graphrag (GitHub)
    url: https://github.com/microsoft/graphrag
    accessed: 2026-09-25
  - title: GraphRAG documentation
    url: https://microsoft.github.io/graphrag/
    accessed: 2026-09-25
  - title: HKUDS/LightRAG (GitHub)
    url: https://github.com/HKUDS/LightRAG
    accessed: 2026-09-25
  - title: getzep/graphiti (GitHub)
    url: https://github.com/getzep/graphiti
    accessed: 2026-09-25
---

# GraphRAG family (Microsoft GraphRAG, LightRAG, Graphiti)

> **TL;DR** These tools use an LLM to extract entities and relations from unstructured text into a graph, then retrieve over it. They help with "global" questions over large, uncurated corpora. We have a small, **curated** corpus with hand-ratified registries, so they would duplicate our registries with unratified, LLM-inferred facts. Hold. Graphiti's bi-temporal facts and episode provenance are ideas worth borrowing.

## What they are
- **Microsoft GraphRAG** (MIT): extracts an entity graph, builds community summaries, and offers Global, Local, DRIFT and Basic (vector) search. The docs say it beats baseline RAG when answers need "traversing disparate pieces of information" or holistic synthesis. The README warns that indexing "can be an expensive operation… start small". The repo now says it won't accept new PRs or features, only bug and security fixes ([GitHub](https://github.com/microsoft/graphrag), [docs](https://microsoft.github.io/graphrag/), accessed 2026-09-25).
- **LightRAG** (MIT, about 40k stars): a graph plus vector dual-level index, with query modes local/global/hybrid/naive/mix. Backends include NetworkX/JSON (default), Postgres, Neo4j, Milvus, Qdrant and others. It works with Claude models ([GitHub](https://github.com/HKUDS/LightRAG), accessed 2026-09-25).
- **Graphiti** (Apache-2.0, Zep): a temporal knowledge graph for agent memory. It has a bi-temporal fact validity model, episode provenance, hybrid (embedding + BM25 + traversal) retrieval, and incremental updates. It runs on Neo4j, FalkorDB or Neptune (Kùzu is deprecated) and ships an MCP server. Anthropic is supported, and structured-output LLMs are recommended ([GitHub](https://github.com/getzep/graphiti), accessed 2026-09-25).

## Why it matters for adapt-rfp
The README's "use graphs to model semantics" invites these tools. Their payoff depends on corpus size and curation. At hundreds to low thousands of short, typed, human-reviewed chunks, where the entities are *already* registered:
- the extraction LLM re-derives what the registries hold, with errors, at index cost;
- community summaries target "what are the themes of this corpus" questions, which M6/M7 don't ask;
- provenance becomes indirect (text → LLM → edge), which conflicts with the "every claim traces to a fact" rule.

## Where they could help later
- **Ingest assistance (M1)**: running LightRAG-style extraction over *raw* `projects/` sources to *propose* entities and facts for human ratification. graph-keeper's staging flow already does this with Claude, in Turtle, inspectably.
- **Very large archives**: if years of past proposals (thousands of documents) are dumped in unsegmented, a GraphRAG index could help exploration before curation.
- **Borrow from Graphiti**: `valid_from`/`valid_until` on facts and "episode" provenance map onto our fact schema ([registry-schemas.md](registry-schemas.md)).

## Strengths
- Strong on global and thematic queries over big corpora, and all three are open source.

## Weaknesses / risks
- Indexing cost, and graphs that are opaque and unratified (low inspectability).
- Most need a graph DB or Postgres stack, and GraphRAG itself is in maintenance mode (date-sensitive).
- Extra moving parts for Claude web deployment.

## Verdict rationale
Hold. Revisit only if an uncurated archive of more than about 1,000 documents needs exploratory search.

Up: [knowledge representation](index.md)
