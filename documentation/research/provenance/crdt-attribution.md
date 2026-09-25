---
title: "CRDT and editor attribution: Yjs, Automerge, Google Docs"
slug: crdt-attribution
level: 3
parent: index.md
related: [span-anchoring.md, git-blame-and-hashing.md]
tags: [crdt, collaboration, yjs, automerge, google-docs, attribution]
status: draft
updated: 2026-09-25
kind: library
verdict: assess
fit: [M9]
license: MIT (Yjs, Automerge)
maturity: emerging
inspectability: low
sources:
  - title: Yjs, attributing content (v14 AttributionManager docs)
    url: https://github.com/yjs/yjs/blob/main/attributing-content.md
    accessed: 2026-09-25
  - title: y-simple-attribution-server (WIP)
    url: https://github.com/yjs/y-simple-attribution-server
    accessed: 2026-09-25
  - title: Automerge Rust docs (ActorId)
    url: https://docs.rs/automerge/latest/automerge/
    accessed: 2026-09-25
  - title: Google Docs API, work with suggestions
    url: https://developers.google.com/workspace/docs/api/how-tos/suggestions
    accessed: 2026-09-25
---

# CRDT and editor attribution: Yjs, Automerge, Google Docs

> **TL;DR** Real-time editors can know, per character, who inserted what. Yjs v14 adds an `AttributionManager` that maps content ids to attributes. Its own docs attribute edits to "Bob" or to an AI model. Automerge tags every change with an actor id. Google Docs keeps suggestion and revision authors internally. All of this is lost the moment text is exported or pasted, which is exactly our workflow. **Assess only**, as a possible future M9 surface.

## What it is

- **Yjs v14**: content is identified by ids. `IdSet`/`IdMap` map id ranges to attributions such as insert, delete, and format by a user. A companion `y-simple-attribution-server` (marked WIP) attributes incoming updates to the authenticated user. The docs' example attributes content to an AI model as well as to humans. Timestamps appear only conceptually *(unverified in implementation)*. v14 was still shipping pre-releases in 2026 (Gutenberg's upgrade issue tracks it) *(check before relying)*.
- **Automerge**: every change carries an `ActorId`, so history can be walked to find who inserted each character. Actor ids identify sessions or devices, not people, so an app must map actor → person.
- **Google Docs**: the UI shows suggestion authors and revision history. The Docs API can read suggestions (`suggestedInsertionIds`, `SuggestionsViewMode`). A Developer Preview adds writing and accepting suggestions. Exporting or copying plain text drops all attribution.

## Why it matters for adapt-rfp

These tools show that character-level authorship is *technically* straightforward when you own the editor. They also show that we don't. Our text passes through Claude Docs, then a clipboard, then Google Docs, then export. No CRDT metadata survives that path.

## How it would fit

Only if M9 later adopts a Yjs-based editing surface we control. Even then, its attribution would be *harvested into* our standoff sidecar format at save time, with git and YAML staying canonical.

## Strengths
- Precise, automatic, no human declaration needed. Yjs explicitly models AI contributors.

## Weaknesses / risks
- Binary, opaque state (low inspectability). Tied to one editor.
- Records keystrokes, not intellectual authorship. Pasting a partner's paragraph attributes it to the paster.
- Yjs v14 attribution is new and partly WIP.

## Verdict rationale

Assess. It is useful as evidence and inspiration. It is not a foundation while the team works in Google Docs.

Up: [provenance index](index.md)
