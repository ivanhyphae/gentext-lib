---
title: Frontmatter schema validation (pydantic, JSON Schema, LinkML)
slug: frontmatter-schema-validation
level: 3
parent: index.md
related: [registry-schemas.md, rdf-toolchain.md, graph-decision.md]
tags: [schema, validation, yaml, pydantic, linkml]
status: draft
updated: 2026-09-25
kind: library
verdict: adopt
fit: [M2, M3, M5, M7, M10]
license: pydantic MIT; LinkML Apache-2.0
maturity: mature
inspectability: high
sources:
  - title: LinkML homepage
    url: https://linkml.io/
    accessed: 2026-09-25
  - title: LinkML generators (JSON Schema, SHACL, Pydantic, OWL, SQL)
    url: https://linkml.io/linkml/generators/index.html
    accessed: 2026-09-25
  - title: JSON Schema
    url: https://json-schema.org/
    accessed: 2026-09-25
---

# Frontmatter schema validation (pydantic, JSON Schema, LinkML)

> **TL;DR** Every chunk frontmatter block and registry entry must validate against one schema, enforced in pre-commit and CI. Adopt **pydantic v2 models** as the source of truth, export **JSON Schema** for editors and non-Python tools, and **assess LinkML**, which would generate pydantic, JSON Schema, SHACL and OWL from one YAML schema and so make the graph path nearly free.

## What they are
- **pydantic**: Python data models with validation. `Model.model_json_schema()` exports JSON Schema *(API per pydantic v2 docs, not re-fetched)*. It fits DR-0006 (Python ≥3.12, uv).
- **JSON Schema**: the language-neutral schema. Editors (VS Code YAML extension) can autocomplete and lint frontmatter against it. The 360Giving grants standard is itself published as JSON Schema ([grant-ontologies.md](grant-ontologies.md)).
- **LinkML**: a YAML schema language (Apache-2.0) whose generators emit JSON Schema, SHACL, RDF/OWL, pydantic, SQL DDL and more. It gives every element a URI and has Schemasheets for spreadsheet-based authoring ([linkml.io](https://linkml.io/), accessed 2026-09-25).

## Why it matters for adapt-rfp
Metadata is only useful if it is consistent: an `orgs:` entry that is not a registry id is a silent leakage bug. Validation also makes cross-reference checks cheap, e.g. that every `facts[]` id exists and every `lineage.derived_from` resolves.

## How it would fit
```
src/adapt_rfp/schema.py        # pydantic: Chunk, Variant, Fact, Org, Place, Program, Term…
schema/*.schema.json         # generated; referenced by editors via yaml-language-server comment
adapt-rfp validate             # loads repo → models → referential-integrity pass → report
.pre-commit-config.yaml      # runs adapt-rfp validate on changed files
```
- Two passes: (1) *shape* (types, enums, required fields) and (2) *integrity* (ids resolve, no alias shared by two orgs, variant word counts match the actual text, `sensitivity` compatible with links).
- With LinkML, pass 2 can partly move to generated SHACL run by pySHACL over the RDF export ([rdf-toolchain.md](rdf-toolchain.md)).

## Strengths
- pydantic: familiar, fast, excellent error messages, no new language.
- LinkML: a single source for validation, docs and semantic mapping, and the most elegant bridge from YAML to RDF.

## Weaknesses / risks
- pydantic-only means the RDF mapping has to be hand-written later (about 100 lines).
- LinkML is a bigger dependency with its own learning curve, and its generated pydantic classes are less idiomatic *(unverified; assess in a spike)*.
- JSON Schema cannot express cross-file referential integrity, so the second pass stays in code.

## Verdict rationale
Adopt pydantic plus exported JSON Schema now for the pilot. Assess LinkML in a half-day spike: model `Org` and `Term` and compare the generated pydantic and SHACL. If it is clean, switch before the registries grow.

Up: [knowledge representation](index.md)
