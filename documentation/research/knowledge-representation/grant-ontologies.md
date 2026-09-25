---
title: Grant and organization vocabularies (schema.org, ROR, VIVO, CERIF/FRAPO, 360Giving)
slug: grant-ontologies
level: 3
parent: index.md
related: [registry-schemas.md, skos.md, rdf-toolchain.md]
tags: [ontology, schema-org, grants, organizations, identifiers]
status: draft
updated: 2026-09-25
kind: standard
verdict: trial
fit: [M3, M5]
license: schema.org CC BY-SA 3.0 (unverified); ROR data CC0 (unverified); 360Giving open
maturity: mature
inspectability: high
sources:
  - title: schema.org Grant
    url: https://schema.org/Grant
    accessed: 2026-09-25
  - title: Open Funder Registry to transition into ROR (Crossref)
    url: https://www.crossref.org/blog/open-funder-registry-to-transition-into-research-organization-registry-ror/
    accessed: 2026-09-25
  - title: ROR, transition from Open Funder Registry
    url: https://ror.readme.io/docs/funder-registry
    accessed: 2026-09-25
  - title: FRAPO (SPAR Ontologies)
    url: https://sparontologies.github.io/frapo/current/frapo.html
    accessed: 2026-09-25
  - title: VIVO ontology / FRAPO discussion (vivo-isf-ontology issue 749)
    url: https://github.com/openrif/vivo-isf-ontology/issues/749
    accessed: 2026-09-25
  - title: 360Giving Data Standard
    url: https://www.360giving.org/about/data-standard/
    accessed: 2026-09-25
---

# Grant and organization vocabularies (schema.org, ROR, VIVO, CERIF/FRAPO, 360Giving)

> **TL;DR** Borrow **schema.org** type and property names (`Organization`, `Project`, `Grant`/`MonetaryGrant`, `FundingScheme`, `funder`, `fundedItem`, `sameAs`) and **ROR** ids for organizations that have one. Look at **360Giving**'s JSON Schema for award fields. Don't adopt VIVO, CERIF or FRAPO: they model research administration in far more depth than a design lab's proposal library needs.

## What they are
- **schema.org Grant**: "a grant, typically financial or otherwise quantifiable, of resources", with `funder`, `sponsor` and `fundedItem`. The subtype `MonetaryGrant` uses `MonetaryAmount`. Related types: `Project`, `ResearchProject`, `FundingScheme` ([schema.org](https://schema.org/Grant), accessed 2026-09-25).
- **ROR** (Research Organization Registry) and the **Crossref Open Funder Registry**: Crossref is transitioning funder identification to ROR. Members can already deposit ROR ids in place of Funder ids. Funder Registry ids remain in existing metadata, and the registry stays available "for the foreseeable future", while new Crossref systems are designed around ROR ([Crossref](https://www.crossref.org/blog/open-funder-registry-to-transition-into-research-organization-registry-ror/), [ROR docs](https://ror.readme.io/docs/funder-registry), accessed 2026-09-25). ROR coverage of California state agencies, special districts and CBOs is *unverified* and probably partial.
- **VIVO**: an ontology of researchers, outputs and institutions, built on BFO, FOAF, Dublin Core and others. **CERIF** is the EU research-information standard, and **FRAPO** is its OWL 2 DL rendering for grants, funders, projects and partners ([FRAPO](https://sparontologies.github.io/frapo/current/frapo.html), accessed 2026-09-25). A VIVO issue notes that FRAPO lacks concepts such as principal investigator ([issue 749](https://github.com/openrif/vivo-isf-ontology/issues/749)). A newer, lighter alternative is **DINGO** (projects and grants linked data, 2020; not reviewed).
- **360Giving**: the UK open grants data standard, authoritative as JSON Schema (`360-giving-schema.json`), with about 10 required fields and spreadsheet-friendly publishing ([360giving.org](https://www.360giving.org/about/data-standard/), accessed 2026-09-25).

## Why it matters for adapt-rfp
Using established names costs nothing and makes a future RDF export, or a JSON-LD rendering for a website, straightforward. Stable external ids (ROR, Wikidata) help deduplicate orgs across partners and funders. The heavy ontologies would force modeling that we don't need, e.g. BFO roles and temporal qualifiers.

## How it would fit
- Entity `type` values come from schema.org: `Organization`, `GovernmentOrganization`, `Place`, `FundingScheme` (programs), `MonetaryGrant` (awards won), `Project` (Hyphae project cases).
- Add `same_as: [https://ror.org/…, https://www.wikidata.org/entity/Q…]` where they exist.
- Hyphae project cases record `funder`, `amount` (fact ref), `period` and `role`, in the spirit of 360Giving's field names *(field-by-field alignment not done)*.
- Funder vocabulary and rubric concepts stay in the M5 solicitation model as their own SKOS schemes ([skos.md](skos.md)).

## Strengths
- schema.org is ubiquitous and stable. ROR is open and increasingly the funder identifier of record.

## Weaknesses / risks
- schema.org is loose: it has no constraints, so we still need our own schema.
- Most local partners won't have ROR ids.

## Verdict rationale
Trial: borrow names and ids now, and revisit the heavier ontologies only if we exchange data with a research-information system.

Up: [knowledge representation](index.md)
