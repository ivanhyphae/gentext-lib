---
title: Proposed provenance schema for adapt-rfp
slug: schema
level: 2
parent: index.md
related: [span-anchoring.md, prov-o.md, llm-generation-records.md, ai-disclosure-standards.md]
tags: [provenance, schema, yaml, frontmatter]
status: draft
updated: 2026-09-25
---

# Proposed provenance schema for adapt-rfp

> **TL;DR** There are three plain-text artifacts: (1) a mandatory `provenance:` block in chunk frontmatter, (2) an agent registry plus one YAML file per LLM generation, and (3) an optional `<chunk>.prov.yaml` span sidecar that records exceptions only. Field names map one-to-one onto W3C PROV, so we can export to PROV-O later without migrating. This is a proposal for a future DR, not a decision.

> **Revision 2026-09-25 (maintainer):** authorship exists for **accountability and quality control**, not reuse rights: who to ask when there's a problem, and where weak text came from. Replace `owner` + `reuse` with `steward` (the person to ask) + `reviewed_by[]`. See DR-0008.

## Design rules

- **Chunk is the unit of truth.** Most questions ("can we reuse this?", "who do we credit?") are answered at the chunk level.
- **Spans record exceptions only.** A span needs a sidecar entry only when it differs from the chunk default.
- **Every agent is an id.** No free-text names in provenance fields. Names resolve through the registry, which also catches "Council/Counsel" (DR-0002).
- **Authorship ≠ ownership.** `authors[]` records who contributed. `owner` + `reuse` record who controls reuse.
- **Unknown is a valid value.** Never guess to fill a field.
- **Git holds the edit history.** We do not duplicate commit logs in YAML (see [git blame](git-blame-and-hashing.md)).

## 1. Chunk frontmatter (mandatory)

```yaml
---
id: method/utci-modeling
type: method
title: UTCI microclimate modeling
variant: v300            # this file's length variant
provenance:
  origin: mixed          # human | partner | ai-generated | ai-assisted | mixed | unknown
  digital_source_type: compositeWithTrainedAlgorithmicMedia  # IPTC term, optional
  authors:               # PROV wasAttributedTo, qualified with a role
    - agent: person:ivan-heitmann
      role: author       # author | editor | reviewer | prompter | translator
    - agent: org:i-relab
      role: author
      note: "Monitoring paragraph originally supplied by partner"
    - agent: ai:claude-opus-5-5
      role: drafter
      via: gen/2026-09-25-utci-shorten-01   # generation record id
  owner: org:hyphae      # who controls reuse
  reuse:
    - agent: org:i-relab
      terms: consent-per-use   # free | credit-required | consent-per-use | no-reuse
  sources:               # PROV hadPrimarySource / wasQuotedFrom
    - source: src:ehcrp-r2-ambrose-memorial-park   # manifest id (M0)
      locator: "Technical Capabilities > Modeling, para 2"
      sha256: 9f2c…      # of the extracted source text, not committed text
  derived_from:          # PROV wasDerivedFrom, qualified with a relation
    - chunk: method/utci-modeling
      variant: v600
      relation: shortened-from   # variant-of | shortened-from | adapted-for | merged-from | edited-in
      at_commit: 3fc8987
  asserts: [fact:bay-point-days-over-100f-2090s, fact:green-heart-hscrp]
  review:
    status: reviewed     # unreviewed | reviewed | canonical
    by: person:ivan-heitmann
    on: 2026-09-25
  spans: method/utci-modeling.prov.yaml   # optional sidecar
---
```

`origin` is a summary that a linter can recompute from `authors[]`. It exists so a quick filter ("show me all unreviewed AI-drafted text") needs only frontmatter.

## 2. Agent registry and generation records

`library/registry/agents.yaml`:

```yaml
- id: person:ivan-heitmann
  type: Person            # PROV Person
  org: org:hyphae
- id: org:i-relab
  type: Organization
  aliases: ["I-ReLab"]
- id: ai:claude-opus-5-5
  type: SoftwareAgent     # PROV SoftwareAgent
  provider: anthropic
  model: claude-opus-5-5
```

`library/provenance/generations/2026-09-25-utci-shorten-01.yaml` is one file per LLM call that produced text we kept (see [LLM generation records](llm-generation-records.md)):

```yaml
id: gen/2026-09-25-utci-shorten-01
activity: shorten        # draft | shorten | adapt | merge | translate | rewrite
agent: ai:claude-opus-5-5
on_behalf_of: person:ivan-heitmann   # PROV actedOnBehalfOf
at: 2026-09-25T15:42:00-07:00
tool: skill:draft-answer@0.1.0
prompt_ref: skills/draft-answer/prompts/shorten.md@3fc8987   # template, committed
prompt_sha256: 41ab…     # rendered prompt; raw text NOT committed if it quotes projects/
inputs:
  - chunk: method/utci-modeling
    variant: v600
    sha256: 77e0…
params: {target_words: 300}
output_sha256: c3d9…     # of raw model output, before human edits
```

## 3. Span sidecar (optional, exceptions only)

The quoted strings below are illustrative, not verified pilot text.

`library/method/utci-modeling.prov.yaml`:

```yaml
chunk: method/utci-modeling
variant: v300
anchored_at: 5e1a2b0          # commit where anchors last verified
spans:
  - id: s1
    select:                   # W3C TextQuoteSelector + position hint
      exact: "Sensors will be co-located with community-hosted sites to capture"
      prefix: "In partnership with I-ReLab, "
      suffix: " hourly air and surface temperatures"
      start: 412              # TextPositionSelector hint, code points
    authors: [{agent: org:i-relab, role: author}]
    reuse: consent-per-use
  - id: s2
    select:
      exact: "shade structures sized to the modeled afternoon heat load"
      prefix: "The design phase will prioritize "
      suffix: ", with"
    authors: [{agent: ai:claude-opus-5-5, role: drafter, via: gen/2026-09-25-utci-shorten-01}]
    review: {status: unreviewed}
  - id: s3
    select: {exact: "21–35 days over 100°F by the 2090s", prefix: "projected ", suffix: ", compared"}
    asserts: [fact:bay-point-days-over-100f-2090s]
    status: anchored          # anchored | fuzzy | orphaned
```

The CLI (`adapt-rfp prov check`) re-anchors every span. Exact matches keep `status: anchored`. Fuzzy matches become `fuzzy` with a score. Misses become `orphaned` and fail CI until a human resolves them. See [span anchoring](span-anchoring.md).

## Composed drafts (M6)

A draft carries the same sidecar format. Every sentence gets a span entry (in a draft, provenance is the point, not the exception):

```yaml
spans:
  - select: {exact: "Hyphae has modeled thermal comfort for …", prefix: "", suffix: " In Bay Point"}
    from: {chunk: capability/thermal-modeling, variant: v150, relation: adapted-for}
```

The QA module (M7) then checks that every factual span has `asserts` and that no span's source names a foreign place (context leakage).

## PROV mapping

| Our field | PROV |
|---|---|
| chunk / variant | `prov:Entity` |
| `authors[].agent` | `prov:wasAttributedTo` (qualified with `prov:hadRole`) |
| `derived_from` | `prov:wasDerivedFrom`, with `wasRevisionOf` / `wasQuotedFrom` subtypes |
| `sources` | `prov:hadPrimarySource` |
| generation record | `prov:Activity` with `used`, `wasAssociatedWith`, `actedOnBehalfOf` |
| `ai:*` | `prov:SoftwareAgent` |

Source: [W3C PROV-O](https://www.w3.org/TR/prov-o/), accessed 2026-09-25.

## What we deliberately leave out

- Per-keystroke edit history. Git commits and Docs revision history are enough.
- Signatures or C2PA manifests (see [AI disclosure standards](ai-disclosure-standards.md)).
- Automatic authorship inference. A derived tool may *suggest* authors, but a human confirms.

Up: [provenance index](index.md)
