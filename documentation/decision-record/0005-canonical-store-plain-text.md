# 0005. Canonical library is plain-text Markdown in git; indexes are derived

- Status: Proposed
- Date: 2026-09-25
- Deciders: Ivan Heitmann; Claude (drafting)

## Context
The README asks for "progressive disclosure structured wiki documentation", an inventory/manifest or full-text database, and eventual operation from Claude web. LLM agents read Markdown well and can navigate a small index file first, then drill down. Humans need to review diffs of prose changes. Embeddings and NLP features are expensive to compute but fully reproducible.

## Decision (proposed)
- Library chunks, registries (facts, entities, glossary), and solicitation models are **plain text in git**: Markdown with YAML frontmatter for chunks, YAML for registries and solicitations.
- Layout supports progressive disclosure: `library/index.md` (short) → `library/<type>/index.md` → `library/<type>/<slug>.md`, with variants as sections or sibling files.
- A single command rebuilds a **derived index** (SQLite/DuckDB for metadata and full-text search, plus a vector index for embeddings) from the repo. The index is gitignored.

## Consequences
- Every change to canonical copy is reviewable, attributable, and revertible.
- No server is needed for the pilot. Cloud deployment can mount the same repo, or sync it into a hosted store later.
- Concurrent editing by many non-technical users isn't possible directly in git. M9 (Docs round-trip) covers that.

## Alternatives considered
- Database as source of truth: better concurrency, worse reviewability, and it locks us into one vendor early.
- Third-party memory system now: the README defers it to production. Revisit in a deployment DR.

## Open questions
- Variants: sections within one file, or sibling files? (Lean: sections, for chunks under ~5 variants.)
- Which embedding model (local vs API)? This affects cost and whether text leaves the machine (see DR-0004).

## Revisions
