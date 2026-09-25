# 0003. Module decomposition

- Status: Proposed (first sketch; granularity accepted as a starting point 2026-09-25)
- Date: 2026-09-25
- Deciders: Ivan Heitmann; Claude (drafting)

## Context
The README lists nine intents. The pilot (DR-0002) shows what the data actually looks like. We need module boundaries that (a) let the pilot vertical slice be built soon, (b) keep the funder-neutral library separate from funder-specific solicitation models, and (c) keep every deterministic check usable *without* an LLM, so skills orchestrate tools instead of replacing them.

## Decision (proposed)

Ten modules in four layers. **Bold** marks modules the pilot slice needs.

```
            ┌─────────────────────── M8 Skills / plugin surface ───────────────────────┐
            │                M9 Collaboration surface (Claude Docs round-trip)          │
            └───────────────────────────────────────────────────────────────────────────┘
  Authoring:     **M6 Compose**  ──────────►  **M7 QA / checks**  ◄── M4 Characterize
                     ▲                              ▲       ▲
  Knowledge:   **M2 Library** ◄─► **M3 Facts & entities** (◄─► optional graph)   **M5 Solicitations**
                     ▲                              ▲                                 ▲
  Intake:      **M0 Ingest** ──► **M1 Segment & classify** ─────────────────────────────┘
  Infra:       M10 Storage, index & deployment
```

### M0 Ingest: sources → normalized text + manifest
- Converters for DOCX, PDF, Google Docs export, and Markdown. Output is structure-preserving Markdown (headings, lists, tables) plus a **source manifest** entry: id, path, sha256, project, funder, date, authors, sensitivity.
- Pilot need: DOCX/PDF only. Stdlib DOCX reading already works; `pdftotext -layout` works for the guidelines.

### M1 Segment & classify: normalized text → candidate chunks
- Split on heading structure, then on paragraph boundaries within a section.
- Classify each segment by **chunk type** (see M2), or mark it *context-only* (meeting notes, action items, contact blocks, brainstorms). Context-only segments are never promoted without a human.
- **Near-duplicate detection** (shingling/MinHash, then embeddings) across sources, so forked documents collapse to one chunk with variants.
- Emits *candidates* for human review. Nothing enters the library automatically.

### M2 Library: canonical chunks (the "wiki")
- One Markdown file per chunk, YAML frontmatter, organized for **progressive disclosure**: `library/index.md` → topic/type index pages → chunk file → its variants. (See DR-0005.)
- Proposed chunk types from the pilot: `project-case`, `capability`, `network` (local knowledge/relationships), `site-context`, `need-statement`, `method` (modeling, monitoring, engagement, design, stewardship…), `partner-role`, `org-profile`, `template` (outreach letters), `boilerplate`.
- Frontmatter sketch: `id, type, title, summary, owner (hyphae|partner:<id>), voice, topics[], places[], orgs[], programs[], facts[] (refs to M3), sources[] (manifest ids + locator), variants[] {id, words, purpose}, lineage {derived_from, relation}, sensitivity, status (draft|reviewed|canonical), last_reviewed`.
- Length variants are first-class: e.g. `method/utci-modeling` with 60-, 150-, and 300-word variants.

### M3 Facts & entities
- **Fact registry**: atomic, citable claims (numbers, dates, dollar amounts, counts, outcomes) with source, retrieval date, and validity window. Examples: "Green Heart: 13–20% lower hsCRP", "Bay Point tracts 06013313203, 06013314105", "CHAT Heat Health Events 3.55".
- **Entity registry**: organizations (with canonical names and aliases, which catches "Council/Counsel"), people-as-roles, places, programs/funders, datasets/tools, Hyphae projects.
- **Glossary**: canonical terms and acronyms, which catches UTCI.
- Optional **semantic graph** (README: "if sufficiently useful"). Start with YAML registries. Promote to RDF/Turtle via the existing `graph-keeper` skills only if cross-entity queries prove necessary. (Candidate future DR.)

### M4 Characterize: classical NLP + embeddings (tool library, no LLM)
- Per chunk/draft: word and sentence counts, readability (textstat), sentence-length distribution, passive voice, hedges/boosters, NER (spaCy), keyphrases, acronym usage, lexical overlap.
- Embeddings for retrieval and similarity (chunk↔chunk, chunk↔rubric descriptor).
- Results are cached as derived data, never canonical.

### M5 Solicitations: RFP → requirements model
- Per solicitation: `solicitations/<funder>/<program>/<round>/`, holding structured YAML for **questions** (id, prompt, word limit, points, rubric bands with descriptor text and extracted *evidence expectations*), **constraints** (budget % floors/ceilings, durations, award ranges), **eligibility** rules, **deliverables**, **deadlines**, and **funder vocabulary** (e.g., the four EHCRP values).
- Produces a **compliance matrix** (requirement → where addressed → status).
- Extraction is LLM-assisted, then human-verified. The YAML is canonical once reviewed.

### M6 Compose: requirement + library → draft
- For a target question: retrieve candidate chunks (M2 + embeddings) → select → adapt to place/funder/voice → fit to the word limit (prefer existing variants over LLM compression) → emit a draft with an **inline provenance map** (sentence → chunk/fact ids).
- Unsourced claims become visible placeholders (`[[NEEDS SOURCE: …]]`), never invented.

### M7 QA / checks: draft → report
Deterministic checks first, LLM judgment second:
- Word/character limits per question.
- Glossary and acronym consistency; entity-name canonicalization.
- **Context leakage**: place, org, and funder names that don't belong to the target (e.g., "Fresno County" in a Bay Point draft).
- Fact provenance: every number or claim resolves to M3.
- Rubric coverage: for each rubric "High" descriptor, check that the expected evidence is present (e.g., community quotes/stories, named partners, funding streams). Uses embeddings plus an LLM judge.
- Style: boosters, filler, AI-tells (can call the existing `humanizer` skill), readability targets.
- Cross-answer redundancy within one application.
- Output: a machine-readable report, rendered for humans.

### M8 Skills / plugin surface
Anthropic-format skills that wrap M0–M7 CLIs, e.g. `ingest-source`, `find-copy`, `model-solicitation`, `draft-answer`, `check-draft`, `compliance-matrix`, `harvest-edits`. Later, an MCP server so Claude web can operate the system end to end (README target).

### M9 Collaboration surface
- Push drafts, with provenance and QA annotations, to Claude Docs for team editing. **Harvest** the edited text back as new chunk variants with lineage (`edited-in: <doc>`).
- Pilot: manual round-trip is fine.

### M10 Storage, index & deployment
- Git repo = canonical (library, registries, solicitations). Derived index (SQLite or DuckDB + vector store) rebuilt by a command.
- Cloud target and third-party memory are deferred to a later DR once the slice works locally.

### Pilot vertical slice (from DR-0002)
M0 → M1 → M2 (≈15–25 chunks: firm experience, Bay Point context, methods) → M3 (glossary + facts for those chunks) → M5 (EHCRP Appendix F narrative questions) → M6 (one question) → M7 (checks that catch the DR-0002 defects). M4 only as far as M7 needs it. M8: one or two skills. M9, M10: manual.

## Consequences
- Deterministic tools (M0, M1, M4, M7 checks) can be tested without an LLM. LLM steps (classification, rubric extraction, adaptation, judging) always hand off to human review.
- Two canonical stores (library vs solicitations) keep content funder-neutral, at the cost of a join step in M6/M7.
- More metadata on each chunk means more curation effort. M1 must propose metadata so humans only confirm it.

## Alternatives considered
- **RAG over raw documents** (no curated library): quick to start, but it reproduces the fork/leakage/inconsistency problems the pilot already shows, and it can't hold length variants or provenance.
- **Graph-first** (RDF as the canonical store): expressive, but it slows the slice and is harder for non-technical colleagues to edit. Kept as an optional M3 layer.
- **LLM-only QA**: can't reliably enforce word limits, names, or provenance. Deterministic checks come first.

## Open questions
1. Chunk granularity: section-level (e.g., "Modeling" paragraph) or claim-level? Proposal: section-level chunks referencing claim-level facts.
2. Ownership: how do we mark and handle partner-authored text (I-ReLab, CCRCD) in the library?
3. Does M5 extraction need to cover budget/workbook constraints in the slice, or narrative questions only?
4. Where do solicitation *summaries* written by the team (e.g., the NOFA summary in the working doc) belong: M5 notes, or discarded?
5. Should M9 target Claude Docs, Google Docs (where the team works today), or both?

## Revisions
- 2026-09-25: Maintainer accepted section-level chunks as a starting point, to be revisited as more cases arrive. Partner-authored text goes *in* the library with authorship provenance (DR-0008). M9 targets Claude Docs, with manual paste to Google Docs (DR-0007).
