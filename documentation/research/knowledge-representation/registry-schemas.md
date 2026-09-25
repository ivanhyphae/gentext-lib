---
title: Minimal registry schemas
slug: registry-schemas
level: 3
parent: index.md
related: [skos.md, grant-ontologies.md, frontmatter-schema-validation.md, graph-decision.md]
tags: [registries, yaml, schema, facts, entities, glossary]
status: draft
updated: 2026-09-25
kind: technique
verdict: adopt
fit: [M2, M3, M7]
license: n/a
maturity: emerging
inspectability: high
sources:
  - title: SKOS Reference (W3C Recommendation)
    url: https://www.w3.org/TR/skos-reference/
    accessed: 2026-09-25
  - title: schema.org Grant
    url: https://schema.org/Grant
    accessed: 2026-09-25
  - title: ROR, transition from Open Funder Registry
    url: https://ror.readme.io/docs/funder-registry
    accessed: 2026-09-25
---

# Minimal registry schemas

> **TL;DR** There are four registries (entities, facts, glossary, sources) plus chunk frontmatter. All ids are typed slugs, all labels are SKOS-shaped, and all links are id references. Values below come from DR-0002. `# ->` comments show the RDF term each field would export to.

## Layout
```
library/registry/orgs.yaml  places.yaml  programs.yaml  datasets.yaml
library/registry/facts/<topic>.yaml
library/glossary/terms.yaml
library/sources.yaml          # manifest ids only; raw files stay in projects/ (DR-0004)
```

## Entity (org)
```yaml
- id: org:ccrcd                               # -> URI
  type: Organization                          # -> schema:Organization
  pref_label: Contra Costa Resource Conservation District   # -> skos:prefLabel
  alt_labels: [CCRCD]                         # -> skos:altLabel
  hidden_labels: [Contra Costa Resources Conservation District]  # known misspelling -> skos:hiddenLabel
  kind: special-district                      # controlled list
  places: [place:contra-costa-county]
  same_as: []                                 # ROR / Wikidata URIs when known -> schema:sameAs
  relationship: partner                       # to Hyphae: partner | client | funder | peer
  notes_ref: null                             # never inline internal assessments (DR-0004)
  reviewed: 2026-09-25
```
`hidden_labels` is what makes the "Council/Counsel" and "Resource(s)" checks deterministic: M7 flags any hidden label that appears in a draft.

## Place and program
```yaml
- id: place:bay-point
  type: Place                                 # -> schema:Place
  pref_label: Bay Point
  within: place:contra-costa-county           # -> schema:containedInPlace
  identifiers: {census_tracts: ["06013313203", "06013314105"]}
  context_leak_guard: true                    # M7: flag if present in drafts for other places

- id: program:lci-ehcrp
  type: FundingScheme                         # -> schema:FundingScheme
  pref_label: Extreme Heat and Community Resilience Program
  alt_labels: [EHCRP]
  funder: org:ca-lci                          # -> schema:funder
  solicitations: [solicitations/lci/ehcrp/round-2/]
```

## Fact
```yaml
- id: fact:bay-point-extreme-heat-days-2090s
  claim: "21–35 days over 100°F by the 2090s"
  value: {min: 21, max: 35, unit: days/yr, threshold: "100°F", horizon: 2090s}
  about: [place:bay-point]
  source: {id: src:TBD, locator: "p. ?"}      # unknown -> leave TBD, M7 reports it
  retrieved: null
  valid_until: null                           # or a date for time-sensitive stats
  status: needs-source                        # needs-source | sourced | verified
```
Every number in a draft must resolve to a `fact:` id, or it becomes `{>>TK source: …<<}`.

## Glossary term
```yaml
- id: term:utci
  pref_label: Universal Thermal Climate Index # -> skos:prefLabel
  alt_labels: [UTCI]                          # accepted forms
  forbidden_labels: [Urban Thermal Comfort Index]   # custom; M7 error if seen
  definition: >-                              # -> skos:definition
    Biometeorological index of thermal stress…
  broader: term:thermal-comfort-index         # -> skos:broader
  scheme: glossary:hyphae                     # funder vocab lives in solicitations/, not here
```

## Chunk frontmatter (reference fields only)
```yaml
id: chunk:method/utci-modeling
type: method
summary: How Hyphae models pedestrian heat exposure with UTCI.
owner: hyphae
voice: firm
topics: [topic:extreme-heat, topic:microclimate-modeling]
places: []                                    # funder-neutral: empty is a feature
orgs: []
terms: [term:utci]
facts: []
variants: [{id: v150, words: 150, purpose: pre-app}, {id: v300, words: 300}]
lineage: {derived_from: null, relation: null}
sensitivity: shareable
status: reviewed
```

## Design rules
1. **Ids are forever.** Rename labels, never ids. When two entities merge, keep both ids and add `replaced_by:` (graph-keeper's "heal by equivalence").
2. **Controlled lists** (`type`, `kind`, `relationship`, `status`, `sensitivity`, topics) live in one `vocab.yaml`, and the schema enums are generated from it.
3. **No prose facts inside entities.** Numbers go in `facts`.
4. **People are roles**, not personal records, e.g. `role:ccrcd-project-lead`, with no contact details (DR-0004).

Up: [knowledge representation](index.md)
