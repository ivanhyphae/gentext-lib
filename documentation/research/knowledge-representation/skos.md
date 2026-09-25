---
title: SKOS
slug: skos
level: 3
parent: index.md
related: [registry-schemas.md, rdf-toolchain.md, graph-decision.md]
tags: [taxonomy, controlled-vocabulary, glossary, w3c]
status: draft
updated: 2026-09-25
kind: standard
verdict: adopt
fit: [M3, M7]
license: W3C Recommendation (royalty-free)
maturity: mature
inspectability: high
sources:
  - title: SKOS Simple Knowledge Organization System Reference (W3C Recommendation, 18 August 2009)
    url: https://www.w3.org/TR/skos-reference/
    accessed: 2026-09-25
---

# SKOS

> **TL;DR** SKOS is the W3C model for thesauri and taxonomies: concepts with preferred, alternative and hidden labels, broader/narrower/related links, and cross-scheme matches. Adopt its *field vocabulary* for the glossary, topics and entity labels in YAML now. Emit real SKOS Turtle only if and when the RDF view is built.

## What it is
SKOS (W3C Recommendation, 2009-08-18) models knowledge organization systems "as-is", without forcing them into formal logic. Classes: `skos:Concept`, `skos:ConceptScheme`, `skos:Collection`. Labels: `prefLabel` (one per language), `altLabel`, and `hiddenLabel` (for search, e.g. misspellings). Relations: `broader`/`narrower` (plus transitive variants) and `related`. Documentation: `definition`, `scopeNote`, `notation`. Mapping: `exactMatch`, `closeMatch`, `broadMatch`/`narrowMatch` ([w3.org](https://www.w3.org/TR/skos-reference/), accessed 2026-09-25).

## Why it matters for gentext
The glossary problems in DR-0002 are SKOS problems:
- **UTCI**: one `prefLabel`, and the wrong expansion recorded as a forbidden variant. SKOS has no "forbidden" label, so we add a custom `forbidden_labels` field. `hiddenLabel` suits tolerated misspellings that should still match in search.
- **Topics** for chunks (extreme heat → microclimate modeling → UTCI modeling) are a `broader`/`narrower` hierarchy. Retrieval can expand a topic filter to its narrower concepts.
- **Funder vocabulary** (EHCRP's Harm Reduction, Belonging, …) is a separate `ConceptScheme` per solicitation. It maps to firm topics with `closeMatch` and is not merged into them, which honours the AGENTS.md separation.

## How it would fit
- YAML fields `pref_label`, `alt_labels`, `hidden_labels`, `definition`, `broader`, `related`, `exact_match`, `scheme` ([registry-schemas.md](registry-schemas.md)).
- M7 checks: an expansion must equal the `pref_label` of the matching `alt_label`, forbidden labels are errors, and hidden labels are warnings.
- Later: the exporter emits `skos:` triples, and SHACL enforces "exactly one prefLabel per language".

## Strengths
- Tiny, stable (17 years), and widely understood by librarians and linked-data tooling.
- Gives us a principled vocabulary instead of ad-hoc field names.

## Weaknesses / risks
- It is not a validation language: integrity constraints still need code or SHACL.
- Overbuilding taxonomies is a real risk for a small team. Keep hierarchies shallow and let them grow from use ("schema trails data").

## Verdict rationale
Adopt it as the field shape: zero cost now, and the RDF path stays open.

Up: [knowledge representation](index.md)
