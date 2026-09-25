---
title: Provenance and authorship of text
slug: index
level: 1
parent: ../index.md
related: [schema.md, span-anchoring.md]
tags: [provenance, authorship, lineage, ai-disclosure, annotation]
status: draft
updated: 2026-09-25
---

# Provenance and authorship of text

> **TL;DR** Record provenance in two layers. **Layer 1 (mandatory):** a `provenance:` block in every chunk's YAML frontmatter, using W3C PROV terms (who, from what, by which activity), plus a small file per LLM generation. **Layer 2 (optional):** a standoff `*.prov.yaml` sidecar that anchors *exceptions* (a partner's sentence, an AI-drafted clause, a fact assertion) to spans with W3C Web Annotation text-quote selectors, re-anchored fuzzily after edits. Do not use inline markup in canonical text, and do not rely on watermarks, C2PA, or Google Docs history. Span-level provenance is the can of worms. Keep it opt-in, exceptions-only, and allowed to decay to "unknown" honestly.

> **Revision 2026-09-25 (maintainer):** authorship exists for **accountability and quality control**, not reuse rights: who to ask when there's a problem, and where weak text came from. Replace `owner` + `reuse` with `steward` (the person to ask) + `reviewed_by[]`. See DR-0008.

## The question

The user wants to know, for any string in a proposal: who wrote it (Hyphae staff, a partner, an AI model with a given prompt), who edited it, which source document and chunk it came from, and which facts it asserts. That record has to survive edits, forks, length variants, and a round-trip through Claude Docs and manual paste into Google Docs. DR-0002 (lesson 9) and DR-0003 (open question 2) already flag partner-authored text as a need.

## Landscape in one screen

| Need | Best precedent | Our use |
|---|---|---|
| Vocabulary for who/what/how | [W3C PROV-O](prov-o.md) | Borrow the terms. Serialize as YAML, not RDF |
| Point at a substring without editing it | [Web Annotation selectors](web-annotation-selectors.md), [brat standoff](web-annotation-selectors.md#brat-standoff) | Sidecar spans |
| Keep anchors alive after edits | [Hypothes.is fuzzy anchoring, diff-match-patch](fuzzy-anchoring.md) | Re-anchor on every commit, then flag orphans |
| Inline marks in the text | [CriticMarkup, Pandoc spans](inline-markup.md) | Review drafts only. Never canonical |
| Line history for free | [git blame, sentence hashes](git-blame-and-hashing.md) | Commit-level "who changed it", plus derived copy detection |
| Live per-keystroke authorship | [CRDT attribution: Yjs, Automerge, Google Docs](crdt-attribution.md) | Out of scope. Round-trips lose it |
| AI disclosure labels | [C2PA, IPTC digitalSourceType](ai-disclosure-standards.md) | Reuse IPTC's *terms* as an enum |
| Detecting AI text after the fact | [Watermarking (SynthID-Text)](text-watermarking.md) | Hold. Unreliable after editing |
| Recording an LLM call | [Generation records and OTel GenAI conventions](llm-generation-records.md) | One YAML file per generation |
| Prior art at scale | [WikiWho, Loopio/Responsive libraries](precedents.md) | Token-level is possible. Commercial libraries stop at the entry level |

## Recommendation

1. **Chunk-level frontmatter is mandatory.** Fields: `origin`, `authors[]` with roles, `owner` and `reuse` terms, `sources[]`, `derived_from[]` with a relation, `generated_by` → a generation record, and `asserts[]` → fact ids. See [schema](schema.md).
2. **Agents live in a registry.** People, organizations, and AI models are all PROV agents with stable ids (`person:…`, `org:…`, `ai:…`). AI models appear as `softwareAgent` entries with a model id and a date.
3. **Generation records are small YAML files.** Each one holds the model, date, operator, skill or prompt *reference*, and input chunk ids with content hashes. Raw prompts that quote `projects/` text must not be committed (DR-0004).
4. **Span sidecars are optional and record exceptions only.** Every span inherits the chunk default. A sidecar lists only the spans that differ, such as "this sentence is I-ReLab's" or "this clause was AI-drafted and not yet human-reviewed". Anchors use `exact` + `prefix` + `suffix`, with a position hint. See [span anchoring](span-anchoring.md).
5. **A CLI re-anchors and lints on every change.** It re-anchors sidecars, marks orphaned spans `status: orphaned` for human triage (it never guesses silently), and checks that every `asserts` fact still resolves.
6. **Round-trips degrade honestly.** Text harvested from Google Docs is diffed against the version we pushed. Unchanged spans keep their provenance. Changed spans become `editor: unknown` until a human declares the editor at harvest.

## Can-of-worms risks

- **False precision.** A span record looks authoritative even when it is a guess. Allow `confidence` and `unknown`.
- **Blended sentences.** A sentence rewritten by three people has no single author. Record `authors[]` with roles, not one owner.
- **Curation cost.** Span sidecars can go stale faster than anyone maintains them. That is why they record exceptions only and orphans fail loudly.
- **Confidential prompts.** Generation provenance can leak source text. Store hashes and ids.
- **Legal meaning.** "Author" here means contribution, not copyright or ownership. Keep `owner`/`reuse` separate from `authors`.

## Pages

Level 2:
- [Proposed provenance schema for gentext](schema.md)
- [Span anchoring across edits and round-trips](span-anchoring.md)

Level 3 cards:
- [W3C PROV-O / PROV-DM](prov-o.md)
- [Web Annotation selectors and brat standoff](web-annotation-selectors.md)
- [Inline markup: CriticMarkup, Pandoc spans, footnotes](inline-markup.md)
- [Fuzzy re-anchoring: Hypothes.is and diff-match-patch](fuzzy-anchoring.md)
- [git blame and sentence content-hashing](git-blame-and-hashing.md)
- [CRDT and editor attribution: Yjs, Automerge, Google Docs](crdt-attribution.md)
- [AI disclosure standards: C2PA and IPTC digitalSourceType](ai-disclosure-standards.md)
- [Text watermarking: SynthID-Text](text-watermarking.md)
- [LLM generation records](llm-generation-records.md)
- [Precedents: WikiWho and proposal content libraries](precedents.md)

Up: [research index](../index.md)
