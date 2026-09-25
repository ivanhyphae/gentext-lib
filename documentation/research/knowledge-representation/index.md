---
title: Knowledge representation
slug: index
level: 1
parent: ../index.md
related: [../../decision-record/0003-module-decomposition.md, ../../decision-record/0005-canonical-store-plain-text.md]
tags: [knowledge-representation, registries, retrieval, graph, progressive-disclosure]
status: draft
updated: 2026-09-25
---

# Knowledge representation

> **TL;DR** Keep the library and registries as plain Markdown and YAML, laid out for progressive disclosure (an `llms.txt`-style index, then type indexes, then chunk files). Validate every file against one schema. Shape the glossary and entity fields so they map one-to-one onto SKOS and schema.org. That lets us generate an RDF view later without migrating anything. Retrieval starts with index navigation, metadata filters and SQLite FTS5 (BM25). Add embeddings and a reranker once the corpus outgrows the context window. Don't adopt a graph database or GraphRAG at our scale. Adopt an RDF layer, built from the YAML and tended with `graph-keeper`, only when one of the triggers in [graph-decision.md](graph-decision.md) fires.

## The question

How should M2 (library) and M3 (facts, entities, glossary) be structured so that Claude can find, trust and reuse chunks? Is a semantic graph ("if sufficiently useful", README) worth the cost?

## What we have to represent

- **Chunks**: prose with metadata, length variants and lineage. Section-level, a few hundred words each (DR-0003).
- **Facts**: atomic claims with a source, a locator and a validity window.
- **Entities**: organizations with aliases, places, programs and funders, datasets, Hyphae projects.
- **Glossary**: a canonical term, variants, forbidden variants (the UTCI collision) and a definition.
- **Solicitations**: questions, rubric bands, constraints (M5; already YAML in DR-0003).

Expected size: the pilot has about 15–25 chunks, and the foreseeable corpus is hundreds to low thousands. At about 300 words per chunk, 1,000 chunks come to roughly 400k tokens *(estimate)*. That is past the ~200k-token line under which Anthropic advises putting the whole knowledge base in the prompt ([contextual-retrieval.md](contextual-retrieval.md)). A metadata-filtered slice (one chunk type, one place) will usually fit under it.

## Landscape in one table

| Layer | Options surveyed | Verdict |
|---|---|---|
| Wiki layout and navigation | [llms.txt](llms-txt.md), [Agent Skills progressive disclosure](agent-skills-progressive-disclosure.md), [LLM-wiki pattern](llm-wiki-pattern.md) | adopt the pattern |
| Human viewing | [Obsidian, Bases/Dataview, Quartz, MkDocs/Zensical](obsidian-and-renderers.md) | trial Obsidian as viewer; hold on publishing |
| Schema and validation | [pydantic, JSON Schema, LinkML](frontmatter-schema-validation.md) | adopt pydantic → JSON Schema; assess LinkML |
| Registry shapes | [minimal registry schemas](registry-schemas.md) | adopt |
| Vocabulary | [SKOS](skos.md) | adopt as field *shape*, not as a file format |
| Graph (RDF) | [rdflib, Oxigraph, pySHACL, graph-keeper](rdf-toolchain.md) | assess; derived view only |
| Graph (property) | [Neo4j, Kùzu, NetworkX](property-graphs.md) | hold (NetworkX: trial for derived analysis) |
| LLM-built graphs | [GraphRAG, LightRAG, Graphiti](graphrag-family.md) | hold |
| Retrieval | [hybrid BM25 + embeddings + rerank](hybrid-search-and-reranking.md), [Contextual Retrieval](contextual-retrieval.md) | adopt BM25 now; trial embeddings and rerank |
| External ontologies | [schema.org, ROR/Funder Registry, VIVO, CERIF/FRAPO, 360Giving](grant-ontologies.md) | borrow terms and IDs; don't adopt whole ontologies |

## Recommendation

1. **Progressive disclosure is the primary retrieval mechanism.** `library/index.md` follows the llms.txt shape: H1, a blockquote summary, then H2 sections that list `[title](path): one-line summary`. Each type index does the same. Chunk frontmatter carries a `summary` field that the indexes are generated from. This mirrors the three-level loading in Agent Skills: metadata first, body second, referenced files last.
2. **One schema, many views.** Define chunk and registry models once, in pydantic (or LinkML, if we want SHACL and RDF output for free). Export JSON Schema and validate in pre-commit and CI. The derived SQLite index is built from the validated objects.
3. **Registries are YAML, one file per entity type or one file per entity.** Ids are stable typed slugs (`org:ccrcd`, `fact:bay-point-tracts`). Fields map onto SKOS and schema.org (`pref_label`, `alt_labels`, `hidden_labels`, `same_as`) so that an RDF export is mechanical. See [registry-schemas.md](registry-schemas.md).
4. **Deterministic retrieval first**: metadata filters (type, place, org, program, sensitivity, owner), then FTS5 BM25 over title, summary and body. Add embeddings (e.g. Voyage) plus a reranker when a filtered candidate set no longer fits comfortably in context, or when recall tests fail. See [retrieval-design.md](retrieval-design.md).
5. **Graph: not now.** Write a ~100-line exporter from YAML to Turtle when a trigger fires: repeated multi-hop questions, constraints that span registries, or the wish to join the library with the existing `graph-keeper` graph. The YAML stays canonical. The `.ttl` is derived or staged for ratification.

## Children

Level 2:
- [graph-decision.md](graph-decision.md): graph or not, decision criteria at our scale
- [retrieval-design.md](retrieval-design.md): how Claude finds chunks, facts and entities

Level 3 cards:
- [llms-txt.md](llms-txt.md)
- [agent-skills-progressive-disclosure.md](agent-skills-progressive-disclosure.md)
- [llm-wiki-pattern.md](llm-wiki-pattern.md)
- [obsidian-and-renderers.md](obsidian-and-renderers.md)
- [frontmatter-schema-validation.md](frontmatter-schema-validation.md)
- [registry-schemas.md](registry-schemas.md)
- [skos.md](skos.md)
- [rdf-toolchain.md](rdf-toolchain.md)
- [property-graphs.md](property-graphs.md)
- [graphrag-family.md](graphrag-family.md)
- [hybrid-search-and-reranking.md](hybrid-search-and-reranking.md)
- [contextual-retrieval.md](contextual-retrieval.md)
- [grant-ontologies.md](grant-ontologies.md)

Up: [research index](../index.md)
