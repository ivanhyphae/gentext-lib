# 0006. Python + uv; classical NLP stack

- Status: Proposed
- Date: 2026-09-25
- Deciders: Ivan Heitmann; Claude (drafting)

## Context
The sibling `hyphae_ai_skills` repo uses Python with `uv`. Anthropic skills bundle Python scripts well. The classical NLP ecosystem (spaCy, textstat, scikit-learn, datasketch) is Python-native. The dev machine has `pdftotext` but not `pandoc` or `python-docx`.

## Decision (proposed)
- Python ≥3.12, `uv` for environments and lockfiles, package `gentext` under `src/`, CLI entry point `gentext <module> <command>`.
- Initial dependencies, added only when a module needs them:
  - Ingest: `python-docx` (or stdlib XML), `pypdf`/`pdfplumber`, or shell out to `pdftotext`.
  - Characterize: `spacy` (+ `en_core_web_sm`), `textstat`.
  - Dedup: `datasketch` (MinHash).
  - Embeddings: TBD (DR-0005 open question).
  - Data: `pyyaml`/`ruamel.yaml`, `pydantic` for frontmatter/registry schemas.
- Tests with `pytest`. The DR-0002 QC defects are the first fixtures.

## Consequences
- One language across tools and skills.
- spaCy models add install weight, so they stay optional behind an extra.

## Alternatives considered
- TypeScript/Bun: fine for an MCP server later, weaker for classical NLP.

## Open questions
- Should the MCP server (M8, cloud) be Python (FastMCP) too? Lean: yes.

## Revisions
