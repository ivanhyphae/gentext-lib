---
title: gentext research — overview
slug: index
level: 0
parent: ../decision-record/README.md
children:
  - storage-platforms/index.md
  - knowledge-representation/index.md
  - ingest-conversion/index.md
  - nlp-quality/index.md
  - llm-evaluation/index.md
  - provenance/index.md
  - claude-platform/index.md
  - prior-art/index.md
tags: [synthesis]
status: draft
updated: 2026-09-25
---

# gentext research — overview

> **TL;DR** Build it; buy nothing. Keep the canonical library as **plain Markdown/YAML in the private git repo**, with a **rebuildable SQLite index** (FTS5 + sqlite-vec). Convert sources with **pandoc**. Catch the pilot's defects with **deterministic checks first** (Vale, spaCy rules, acronym extraction, fuzzy names, MinHash). Then run an **adversarial LLM pass in which the judge acts as a witness**: every finding must quote the draft and cite a rubric line, and scores stay advisory. Record **authorship in chunk frontmatter** (PROV terms), with optional span sidecars for exceptions only. Deliver it as **one Python core → CLI → Skills + a FastMCP server**, shipped as a plugin. Pilot in local Claude Code. Claude web runs end to end once the MCP server is hosted. Supabase later, only as a derived mirror. Notion and third-party "memory" products: no.

Read the conventions in [conventions.md](conventions.md). Each topic below is a level-1 page that links further down.

## Recommended stack by module (DR-0003)

| Module | Recommendation | Verdict | Read more |
|---|---|---|---|
| M0 Ingest | pandoc `docx+styles`, `--track-changes=all` + Lua filter; `pdftotext` + regex for rubric text; pdfplumber for real tables; Google Docs API `includeTabsContent=true` for tabbed docs | adopt | [ingest-conversion](ingest-conversion/index.md) |
| M1 Segment | Our own heading-path splitter; MinHash/LSH (datasketch) for forks and variants; Docling as a second opinion | adopt / trial | [heading-chunking](ingest-conversion/heading-chunking.md), [minhash-lsh](nlp-quality/minhash-lsh.md) |
| M2 Library | Markdown + YAML frontmatter, llms.txt-style progressive-disclosure indexes, pydantic → JSON Schema validation in pre-commit/CI, one sentence per line | adopt | [knowledge-representation](knowledge-representation/index.md) |
| M3 Facts/entities | YAML registries shaped like SKOS (`pref_label`/`alt_labels`/`hidden_labels`) with schema.org/ROR ids; RDF view only when [triggers](knowledge-representation/graph-decision.md) fire | adopt; graph = hold | [registry-schemas](knowledge-representation/registry-schemas.md) |
| M4 Characterize | spaCy, textstat/TextDescriptives, hype/booster lexicon; embeddings (local sentence-transformers or open-weight `voyage-4-nano`) to rank evidence, not to decide pass/fail | adopt / trial | [nlp-quality](nlp-quality/index.md) |
| M5 Solicitations | Claude PDF + Citations for human-verified extraction; compliance matrix with a word-for-word check against the solicitation | adopt | [compliance-matrix](prior-art/compliance-matrix.md) |
| M6 Compose | Retrieve with metadata filters + BM25, then embeddings/rerank only after a recall test; curated metadata as the contextual-retrieval prefix | adopt / trial | [retrieval-design](knowledge-representation/retrieval-design.md) |
| M7 QA | Deterministic catalog → fact verification → rubric-checklist panel → skeptical reviewer → one rebuttal; stages modelled on color-team reviews | adopt | [check-catalog](nlp-quality/check-catalog.md), [adversarial-review-pass](llm-evaluation/adversarial-review-pass.md) |
| Provenance | `provenance:` frontmatter block (PROV-O terms) + per-generation records; opt-in `*.prov.yaml` span sidecars using Web Annotation text-quote selectors | adopt / trial | [provenance](provenance/index.md), [schema](provenance/schema.md) |
| M8 Surface | One Python core + JSON CLI; Skills for procedure; FastMCP (Streamable HTTP, OAuth) for data and checks; one plugin | adopt | [delivery-architecture](claude-platform/delivery-architecture.md) |
| M9 Collaboration | Claude Docs for iteration; manual paste into Google Docs; harvest edits back through Claude | adopt (DR-0007) | [docs-roundtrip](claude-platform/docs-roundtrip.md) |
| M10 Storage/deploy | Git canonical; SQLite FTS5 + sqlite-vec derived; Claude Code on the web now, hosted MCP next; Supabase only as a derived mirror if needed | adopt; Supabase = assess | [storage-platforms](storage-platforms/index.md) |

## Phasing

1. **Now → 2026-10-13 (pilot):** local Claude Code, CLI + skills, Claude Docs drafts. Checks aimed at Harm Reduction Q1/Q2.
2. **After submission:** re-ingest the final submitted doc, harvest the edits, calibrate the LLM judge against a small human gold set, and package the plugin.
3. **Then:** host the MCP server (read + check tools) as a claude.ai connector, then add write tools that open PRs.
4. **Only if needed:** Supabase mirror, RDF layer, reranker.

## Cross-cutting findings

- **Scores are not decisions.** 2026 studies of LLMs reviewing grants found inflated, compressed scores that matched funding decisions at or below chance. What we deliver is the quoted findings. [judge-reliability](llm-evaluation/judge-reliability.md)
- **Distinctiveness is a risk.** AI-assisted proposals read as less distinctive (PNAS 2026), and some funders restrict AI-drafted text. Record each funder's AI policy in the solicitation model. [funder-ai-policies](prior-art/funder-ai-policies.md)
- **Watch licenses:** pymupdf4llm (AGPL), YAKE (AGPL/LGPL conflict), `language_tool_python` (GPL; call a self-hosted server over HTTP instead), Bespoke-MiniCheck-7B (non-commercial).
- **Data leaving the machine** (DR-0004): local or open-weight embeddings are viable, so no API is required for sensitive text.

## Conflicts and unverified claims to test

- **Google Docs tabs and styles.** The maintainer's experience is that the API doesn't expose styles for tabbed docs. The ingest research found per-tab `namedStyles` when using `includeTabsContent=true`, and suspects that code reading only the legacy top-level fields sees just the first tab. Test on a real tabbed doc. [google-docs-tabs](ingest-conversion/google-docs-tabs.md)
- **Claude Docs → Google Docs export:** the help centre and the connector guide disagree. [claude-docs](claude-platform/claude-docs.md)
- **Drive connector reading every tab:** unverified. [google-drive-connector](claude-platform/google-drive-connector.md)
- **Skill sharing across a claude.ai org:** the docs disagree.
- **MCP hosting costs** (e.g., Prefect Horizon free tier): vendor claims go stale fast. [remote-mcp-hosting](storage-platforms/remote-mcp-hosting.md)

## Topics

- [Storage & platforms](storage-platforms/index.md): git vs SQLite/DuckDB/LanceDB vs Supabase/Notion; agent memory; remote MCP hosting.
- [Knowledge representation](knowledge-representation/index.md): progressive-disclosure wiki, registries, SKOS, graph-or-not, retrieval.
- [Ingest & conversion](ingest-conversion/index.md): converters tested on the pilot, Google Docs tabs, chunking.
- [NLP quality](nlp-quality/index.md): deterministic and statistical checks mapped to the pilot's defects.
- [LLM evaluation](llm-evaluation/index.md): rubric judging, the adversarial pass, judge bias, eval harnesses.
- [Provenance](provenance/index.md): authorship over chunks and spans; PROV-O; anchoring spans across edits.
- [Claude platform](claude-platform/index.md): Skills, plugins, MCP, Claude Docs, API features, Agent SDK.
- [Prior art](prior-art/index.md): RFP libraries, grant-AI tools, compliance matrices, color teams.

## Candidate decision records

These follow from the research. Each is still to be written and ratified.

- Accept DR-0005 (plain text + SQLite derived index) and DR-0006 (Python/uv), with pandoc added as a system dependency.
- Provenance schema (resolves DR-0008): Layer-1 frontmatter fields and the agent registry.
- QA architecture: deterministic catalog + witness-style LLM pass; scores advisory.
- Delivery architecture: core → CLI → Skills + MCP → plugin; phasing as above.
- Graph deferral, with explicit triggers.
