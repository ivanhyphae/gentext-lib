# Tooling backlog

> Built so far: M11 discovery/inventory, T1 profile, T2 cards, T3 extraction, solicitation model files. Everything below is **not built**. The policy is to build as needed for the live application, in roughly this order. Module ids refer to DR-0003; tiers to DR-0011.

## Needed for the Oct 13 application (next)

| # | Item | Module | Notes |
|---|---|---|---|
| 1 | **Fact registry** (`library/facts/*.yaml`): pydantic schema, `gentext facts add/verify`, source + locator + access date, verification status | M3 | Seed from candidate `facts`. Verification = quote found in the source text + human confirm. |
| 2 | **Promotion (T4)**: `gentext promote <candidate>` → `library/<type>/<slug>.md` with DR-0008 provenance (steward, authors, reviewed_by), split/merge, sensitivity tag | M2 | Candidates are staging only. Promotion is a human/Opus decision. |
| 3 | **Draft scaffold per application/question**: `solicitations/.../applications/<app>/answers/<qid>.md` with a sentence→source provenance map | M6 | Composition is done by Claude (Opus) in-session from facts and chunks, not a pipeline. |
| 4 | **Deterministic checks** `gentext check <draft>`: word limit, leftover `{>>TK`, glossary/acronym (UTCI), entity-name near-misses (rapidfuzz), place/org leakage against the application's allowed set, booster lexicon | M7 | See `documentation/research/nlp-quality/check-catalog.md`. Emits the unified finding record (`research/prose-signals/span-feedback-schema.md`). |
| 5 | **Glossary + entity registry seed** (`library/glossary/`, `library/entities/`) with SKOS-style labels | M3 | Needed by #4. Seed: UTCI, CHAT, VCP, DAC/SDAC, ARPD, CCRCD, CSAHC (Caribbean South America Hispanic Council), Bay Point Garden Club. |

## Soon after

| # | Item | Module | Notes |
|---|---|---|---|
| 6 | Rubric-coverage pass (witness-style LLM judge; quotes + rubric line, validated) | M7 | `research/llm-evaluation/adversarial-review-pass.md` |
| 7 | Prose signals v1 (`gentext signals`): concreteness/anchor density percentiles vs exemplar corpus, slop lexicon | M4/M7 | `research/prose-signals/index.md` |
| 8 | Fuzzy anchor fallback for T3 (rapidfuzz) | T3 | Recovers the remaining unmatched anchors. Raw outputs are saved, so it can run with `--revalidate`. |
| 9 | Card prompt c4: stop over-matching wanted-asset need ids; split cards for very long docs | T2 | Known defects in DR-0011. |
| 10 | Needs-ordered extraction: rank hold sections by `serves_needs` hits on live questions before spending | T3 | Haiku leans generous on `hold` (55/104). |
| 11 | Discovery sweep of the 6 unwalked folders ("Current Proposals", "AdaptOS (EH)", "Ambrose Stormwater", …) | M11 | Follow `skills/asset-discovery/SKILL.md`. |
| 12 | OCR for scanned PDFs (Marker locally, or Claude PDF input) | M0 | 2 failed acquisitions: `sgc22127-signed-grant-agreement`, `prescott-final-report-deck-2020`. |
| 13 | `.odt` extraction (pandoc reads ODT) | M0 | `harry-hines-proposal-content-2021` needs a manual download first. |

## Later

| # | Item | Module | Notes |
|---|---|---|---|
| 14 | Skills wrapping the funnel (`triage-sources`, `draft-answer`, `check-draft`) | M8 | Only asset-discovery exists. |
| 15 | Drive API acquisition script (tabs via `includeTabsContent`; binary files) | M0 | Also answers the open "tab styles" question. Needs `gcloud auth application-default login` with Drive scope. |
| 16 | Remote MCP server on Cloud Run (FastMCP; OAuth for claude.ai connector) | M8/M10 | DR-0009 |
| 17 | Claude Docs ↔ repo harvest (edited text back in as variants with lineage) | M9 | DR-0007 |
| 18 | Gemini backend for cards on the Cloud Run server | T2 | DR-0011 revision |
| 19 | Derived SQLite index (FTS5 + sqlite-vec) | M10 | DR-0005; not needed at the current scale. |
