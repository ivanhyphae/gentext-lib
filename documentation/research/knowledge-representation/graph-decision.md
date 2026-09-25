---
title: "Graph or not: decision criteria at our scale"
slug: graph-decision
level: 2
parent: index.md
related: [registry-schemas.md, rdf-toolchain.md, property-graphs.md, graphrag-family.md, skos.md]
tags: [graph, rdf, property-graph, graphrag, decision]
status: draft
updated: 2026-09-25
---

# Graph or not: decision criteria at our scale

> **TL;DR** At hundreds to low thousands of curated chunks, a graph database and LLM-extracted GraphRAG both cost more than they return. The relations we need (chunk → fact, chunk → org, org alias → canonical, variant-of) are foreign keys in YAML, and a Python loader can resolve them. Design the YAML so that an RDF export is mechanical. Build that export, and tend it with `graph-keeper`, only when one of the triggers below fires.

## What "graph" could mean here

| Option | Canonical store | Who builds edges | Fit |
|---|---|---|---|
| A. **YAML with typed id references** | git (DR-0005) | humans + M1 proposals | today |
| B. **Derived RDF view** (YAML → Turtle via rdflib, SHACL checks, SPARQL) | git YAML; `.ttl` derived | exporter | when triggered |
| C. **RDF canonical** (graph-keeper `graph/core.ttl` + `staging/`) | git Turtle | Claude proposes, human ratifies | for the *semantic* layer only |
| D. **Property-graph DB** (Neo4j; Kùzu is archived) | database | code | hold |
| E. **LLM-extracted graph** (GraphRAG, LightRAG, Graphiti) | tool's store | LLM | hold |

## Why not now

1. **The edges are already explicit.** DR-0003 frontmatter lists `facts[]`, `orgs[]`, `places[]`, `programs[]` and `lineage`. Resolving them is a dictionary lookup. The questions M6 and M7 ask are one hop: "chunks about Bay Point", "facts used by this chunk", "is 'Resource Conservation District' an alias of `org:ccrcd`?". SQL over the derived index answers these.
2. **Curated beats extracted.** GraphRAG-style tools infer entities and relations with an LLM at index time. Our registries are hand-ratified, and the truthfulness rules in AGENTS.md require provenance for every claim. An LLM-extracted graph adds a second, unratified source of "facts". Microsoft warns that indexing "can be an expensive operation", and its repo is now in maintenance mode ([graphrag-family.md](graphrag-family.md)).
3. **Inspectability.** YAML diffs are readable by non-technical colleagues. Turtle is readable but unfamiliar. A database is opaque in git.
4. **Scale.** A filtered slice of the library fits in Claude's context ([retrieval-design.md](retrieval-design.md)). Graph traversal earns its keep when the candidate set is too large to read. That is not our situation.

## Triggers to add layer B or C

Adopt the derived RDF view when **any two** of these hold, or any one holds persistently:

- **Multi-hop questions recur.** Examples: "which past project cases involved a partner that is also a co-applicant on this solicitation *and* used a dataset the funder names?", or "every chunk whose facts come from a source older than 3 years, for programs of funder X". If we keep writing ad-hoc Python joins for these, a SPARQL endpoint pays off.
- **Constraints span registries.** Examples: "every `partner-role` chunk must reference an org with `role: partner` for the target solicitation", or "no chunk with `sensitivity: internal` may link to a public template". SHACL expresses these declaratively, and pySHACL runs them in CI.
- **Taxonomy depth grows.** If topics and methods develop real `broader`/`narrower` hierarchies (e.g. `method/heat-modeling/utci`), and retrieval should expand a query to narrower terms, SKOS in RDF gives this for free.
- **Joining with other graphs.** The team wants library entities linked to the existing `graph-keeper` graph, or to ROR/Wikidata ids, and queried together.
- **Several consumers.** More than one tool (M6 compose, M7 QA, a dashboard) needs the same relational view, and keeping each one's join code in sync becomes a burden.

## What to do now so the switch is cheap

- **Typed, stable ids** (`org:ccrcd`, `place:bay-point`, `fact:chat-heat-events-bay-point`). An id maps directly to a URI, `https://hyphae.design/id/org/ccrcd` *(placeholder namespace)*.
- **SKOS-shaped labels** on entities and glossary terms: `pref_label`, `alt_labels`, `hidden_labels` (known misspellings such as "Counsel"), `definition`, `broader`, `related`, `exact_match` ([skos.md](skos.md)).
- **schema.org-shaped types** for orgs, projects and grants (`Organization`, `Project`, `MonetaryGrant`, `funder`, `sameAs`), plus ROR ids where they exist ([grant-ontologies.md](grant-ontologies.md)).
- **Relations as named fields**, never prose: `lineage: {derived_from: chunk:…, relation: shortened-from}`.
- **One schema definition** (pydantic or LinkML). With LinkML, JSON Schema, SHACL and an RDF mapping come from the same YAML schema ([frontmatter-schema-validation.md](frontmatter-schema-validation.md)).

The exporter then becomes a loop: for each validated object, emit `rdf:type`, labels and one triple per reference field. Run pySHACL on the result. Load it into rdflib (small) or pyoxigraph (faster, persistent) for SPARQL ([rdf-toolchain.md](rdf-toolchain.md)).

## Where graph-keeper fits

`graph-keeper` treats Turtle text as the source of truth and puts tentative triples in `staging/` for human ratification. Its principles ("schema trails data", "reuse > specialize > coin") match how the glossary and entity registry should evolve. Two options:

- **Conservative (recommended first).** YAML stays canonical. The exporter writes `graph/library.ttl` as a *derived* file, and graph-keeper is used read-only for "what do we know about X" and for insight generation over the neighborhood.
- **Semantic layer (later).** Relations that don't belong in chunk frontmatter move into graph-keeper-tended Turtle, where graph-keeper stages them for human ratification. Examples: "method X addresses rubric concept Y", "program A is a successor of program B". Chunks and facts stay YAML. This is option C, applied to the knowledge that is truly graph-shaped.

## Decision checklist (revisit at ~200 chunks or after the pilot)

- [ ] Count ad-hoc multi-hop joins written for M6/M7 (more than 3 distinct ones means build B).
- [ ] List cross-registry integrity rules (more than 5 means SHACL is worth it).
- [ ] Check whether topic/method hierarchy depth exceeds 2.
- [ ] Ask whether anyone needs the library joined to another graph.

Up: [knowledge representation](index.md)
