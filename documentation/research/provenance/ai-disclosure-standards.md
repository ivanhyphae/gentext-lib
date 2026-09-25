---
title: "AI disclosure standards: C2PA and IPTC digitalSourceType"
slug: ai-disclosure-standards
level: 3
parent: index.md
related: [text-watermarking.md, llm-generation-records.md, schema.md]
tags: [ai-disclosure, c2pa, iptc, content-credentials, standard]
status: draft
updated: 2026-09-25
kind: standard
verdict: trial
fit: [M2, M6]
license: open specifications (C2PA, IPTC NewsCodes CC-BY, unverified)
maturity: emerging
inspectability: medium
sources:
  - title: C2PA Technical Specification 2.4 (A.8 unstructured text, A.9 structured text)
    url: https://spec.c2pa.org/specifications/specifications/2.4/specs/C2PA_Specification.html
    accessed: 2026-09-25
  - title: IPTC Digital Source Type NewsCodes vocabulary
    url: https://cv.iptc.org/newscodes/digitalsourcetype/
    accessed: 2026-09-25
  - title: IPTC guidance on metadata for synthetic media
    url: https://iptc.org/news/iptc-publishes-metadata-guidance-for-ai-generated-synthetic-media/
    accessed: 2026-09-25
  - title: c2pa-unstructured-text reference implementation (third party)
    url: https://github.com/writerslogic/c2pa-unstructured-text
    accessed: 2026-09-25
---

# AI disclosure standards: C2PA and IPTC digitalSourceType

> **TL;DR** **IPTC digitalSourceType** is a small controlled vocabulary for how media was made (`humanEdits`, `trainedAlgorithmicMedia`, `compositeWithTrainedAlgorithmicMedia`, …). **Trial** it as an optional enum in chunk frontmatter so our labels line up with an industry term set. **C2PA** signed manifests now have text embeddings in spec 2.4 (invisible Unicode variation selectors for plain text, delimited blocks for structured text). They are overkill for an internal library and fragile under paste. Hold them unless a funder asks for content credentials.

## What it is

- **IPTC Digital Source Type** (NewsCodes, updated 2022–2024). Relevant terms and definitions:
  - `digitalCreation`: created by a human using non-generative tools.
  - `humanEdits`: augmentation or correction by humans using non-generative tools.
  - `trainedAlgorithmicMedia`: created algorithmically using an AI model trained on captured content.
  - `compositeWithTrainedAlgorithmicMedia`: augmentation or correction using a generative AI model.
  - `algorithmicallyEnhanced`: modification without changing main content (e.g., cleanup).
  - `composite`: a mix of elements, any of which may or may not be generative AI.

  The vocabulary was designed for images and video in XMP. C2PA reuses it in `digitalSourceType` action parameters.
- **C2PA** (Content Credentials). This is a cryptographically signed manifest of assertions (actions, ingredients, creator) bound to an asset by hash. Spec 2.4 has **A.8 Embedding Manifests into Unstructured Text** (manifest bytes encoded as non-rendering Unicode variation selectors, bound with a data-hash assertion, "only where no other embedding method is feasible") and **A.9 Structured Text** (Markdown, YAML, source code). Implementations exist, mostly from third parties (e.g., writerslogic, Encypher). A third-party repo notes the unstructured-text wire format should be treated as draft until it appears in a released spec. That conflicts with the 2.4 spec page, which includes A.8, so check which applies.

## Why it matters for adapt-rfp

Funders and clients may start asking "was this AI-written?". Using IPTC's terms for `origin` keeps our answer legible outside the team, with no invented taxonomy.

## How it would fit

`provenance.digital_source_type` is optional. A linter derives it from `authors[]`: only human authors gives `digitalCreation`/`humanEdits`, AI drafter plus human editor gives `compositeWithTrainedAlgorithmicMedia`, and unreviewed AI output gives `trainedAlgorithmicMedia`. We would not embed C2PA manifests in library Markdown.

## Strengths
- IPTC terms are precise, stable, and free to reuse.
- C2PA is the only widely backed *signed* provenance chain.

## Weaknesses / risks
- The IPTC terms describe *media*. "Captured content" maps awkwardly onto prose.
- Invisible C2PA characters in text get stripped by editors and paste, and can break word counts or funder portals. Signing adds key management.
- The statuses of the text sections differ between sources (see above).

## Verdict rationale

Trial the IPTC enum (cheap and derivable). Hold C2PA embedding.

Up: [provenance index](index.md)
