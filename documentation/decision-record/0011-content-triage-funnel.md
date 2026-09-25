# 0011. Content triage funnel: spend tokens in proportion to value

- Status: Proposed (2026-09-25)
- Date: 2026-09-25
- Deciders: Ivan Heitmann; Claude (drafting)

## Context
- One solicitation has already produced ~80 inventory records and ~36 MB of sources (≈350k words of text), including a 69k-word working doc, a 50k-word survey dump, and two submitted proposals of 20–27k words each. More sweeps are running.
- The maintainer: *if we discover 50 documents we shouldn't burn tokens trying to incorporate all of it; we need to discern which things need to be held and which can be ignored or deleted.* In another project they used Marker OCR → sage-wiki, which has more features than we need here. They suggest Haiku sub-agents for bulk processing.
- DR-0010 triages on **metadata only** (title, owner, folder, size). That's enough to find things, but not enough to decide what inside a document is worth keeping.
- Cloud deployment of an LLM pipeline is hard (DR-0009). Whatever we build must run locally first, from Claude Code, and later as a batch job without redesign.

## Decision (proposed)
Process documents through a **funnel of increasingly expensive tiers**. Only survivors advance, and each tier writes a small, durable artefact, so no document is processed twice.

| Tier | What runs | Input | Output (in git) | Gate to next tier |
|---|---|---|---|---|
| **T0 Inventory** (exists) | metadata triage (DR-0010) | Drive/web metadata | `inventory/assets.yaml` record | `include` |
| **T1 Profile** | deterministic, no LLM: convert (pandoc / pdftotext; Marker only for scanned or image PDFs), outline, word counts, near-duplicate check against everything already profiled (MinHash), contact-detail scan | the file | `inventory/profiles/<id>.yaml`: outline (headings plus words per section), duplicate-of links, PII flags | not a duplicate; has prose sections |
| **T2 Card** | **Haiku**, one bounded call per document: outline plus the first ~150 words of each section, never the whole document (≈4–8k tokens in) | profile + section heads | `inventory/cards/<id>.yaml`: summary, per-section type guess, reuse value, the active needs it serves, and a **disposition** | disposition = `hold` |
| **T3 Extract** | **Haiku** per *selected section*: segment into candidate chunks and facts using DR-0003 chunk types | held sections only | `library/_candidates/…` (not yet the library) | human or Opus promotion |
| **T4 Promote/Compose** | **Opus/Sonnet** and humans | candidates + solicitation model | library chunks, drafts | none: this is where expensive reasoning happens |

**Dispositions** (set at T2, can be overridden by a human):
- `hold`: extract candidates (T3). This covers submitted proposals, project deliverables with citable facts, and current capability text.
- `reference`: keep the source and card; don't chunk. Retrieve on demand when a question needs it (guidelines, TA guides, cited reports).
- `ignore`: keep the card only. It exists and is summarised, but won't be touched again.
- `drop`: remove the file from `sources/`, set the inventory status to `exclude`, and keep the record so sweeps skip it.

**Relevance is needs-driven ("pull", not "push").** A card scores a document against the **current needs list**:
- the questions and evidence expectations of active solicitation models (DR-0012)
- the inventory's `wanted` items
- library gaps

So the funnel spends tokens on whatever helps the live application first. The same document can be re-scored cheaply from its card when a new solicitation arrives, with no re-reading.

**Orchestration: a script, not ad-hoc agents, for the bulk tiers.**
- T1 and T2 run as `gentext profile` and `gentext card`: Python using the Anthropic API with Haiku.
  - Versioned prompts in the repo.
  - Pydantic-validated card output.
  - Results cached by `(sha256, prompt version)`.
  - Tokens and cost logged per run.
  - Batch API for large sweeps.
- This works identically from a laptop, Claude Code, or later a Cloud Run job.
- Claude Code **Haiku sub-agents** stay useful for exploratory or one-off passes, and for T3 on a handful of sections. They aren't the system of record, because their prompts and outputs are harder to version and re-run.

## Consequences
- Most documents stop at T1 (duplicates, forks) or T2 (`reference`/`ignore`). Opus-level tokens are spent only on held sections and on composition.
- Cards and profiles give a progressive-disclosure layer between an inventory line and the full text. Claude can scan 100 cards without reading 100 documents.
- Needs an API key and a small budget for Haiku. Card quality needs a spot-check: on the pilot, compare Haiku's disposition with a human call for ~20 documents before trusting it.
- Adds `profiles/` and `cards/` directories under `inventory/`. They're small YAML files, committed, and rebuildable (but cached so they aren't recomputed).

## Alternatives considered
- **Marker → sage-wiki:** it has worked for the maintainer at larger scale, but it adds a feature-rich system to run and learn. Marker stays available for scanned PDFs (the local GPU can run it).
- **Opus reads everything:** simplest, but it's the cost and latency problem the maintainer describes, and it scales badly across solicitations.
- **Embeddings-only triage:** cheap, but embeddings can't say *why* a document matters or propose a disposition. Use them inside T2 scoring as a helper, not as the gate.

## Open questions
- Is "first ~150 words per section" enough for Haiku to judge a section? Tune on the pilot.
- Should `drop` physically delete from `sources/` (git history keeps it anyway) or just mark it? Lean: delete files over 1 MB, mark the rest.
- Where do Claude Docs and meeting-notes context enter the funnel? Lean: T1/T2 only, disposition `ignore` or `reference`, never `hold` without a human.

## Revisions
- 2026-09-25: **Model split by tier, from a side-by-side test.** Cards: Sonnet 5 agreed with Haiku on 10/12 dispositions at ~8× the cost, so T2 stays on Haiku. Extraction: on the same 6 Bay Point sections, Sonnet 5 produced 32 library-sized chunks (Haiku: 13, some >1,000 words), 39 quoted facts (22), and 3% anchor misses (~11%), for ~$0.07/section sync, so **T3 defaults to Sonnet 5**, with a 25-word minimum chunk size. Added `extract --prepare` so the sub-agent backend covers T3 as well as T2, and a pypdf fallback when `pdftotext` is absent (cloud sessions).
- 2026-09-25: **T3 implemented** (`gentext extract`). Haiku proposes chunks as start/end *anchors*, and code slices the exact source text (whitespace- and markup-insensitive), so candidates are verbatim by construction. Facts are kept only if their quote occurs in the chunk. Sections ≥90% contained in an already-extracted section are skipped. Raw outputs are saved under `build/extract-raw/<run>/`, and `--revalidate` re-slices them with no API cost. First run: 44 sections → **111 candidates**, 190 kept facts, 14 unmatched anchors (~11%), **≈$0.15**. Context-leakage flags work: 7 raised; the "Monument Corridor" flag in both Bay Point pre-apps was verified as a deliberate citation of the CCHS 2015 case study (p. 34), not leakage. A bug where the schema helper stripped a property literally named `title` was caught and fixed, with a regression test.
- 2026-09-25: Card batch 2 (prompt c3, section ids): 97/97 cards, **≈$0.65**. Dispositions: 55 hold, 46 reference, 3 ignore. Haiku leans generous on `hold`, so T3 should be ordered by needs (live questions first), not run on every hold.
- 2026-09-25: First batch run, prompt c2: 35/35 cards, 0 errors, 278k input / 43k output tokens, **≈$0.25**. Dispositions: 6 hold, 1 ignore, 28 reference, 0 drop (every item was already triaged `include`). Agent spot-check found sensible calls and useful flags (for example, context-leakage risk in the Fresno doc's "Stuff from other projects"). Known defects: (1) repeated heading names give duplicate section paths, so cards can't name a section uniquely; the fix is to add section ordinals (`§n`) in prompt c3; (2) wanted-item need ids get over-matched (such as `ehcrp-r2-webinars-office-hours`). Human spot-check still pending.
- 2026-09-25: T1 (`gentext profile`) and T2 (`gentext card run|prepare|ingest`) implemented. The maintainer added an API key in `.env` for batch runs. First runs: 35 profiles in ~3 s; a 2-card sync test cost ≈$0.017. Pending: a human spot-check of ~20 dispositions before relying on them.
- 2026-09-25: **Model access is a pluggable backend** (the maintainer raised API-key availability in cloud Claude Code). `gentext card` separates *prompt building and output validation* (deterministic, in the repo) from *execution*:
  - `subagent` (default for the pilot): `gentext card prepare` writes bounded prompt files; Claude Code spawns Haiku sub-agents that return JSON; `gentext card ingest` validates and caches the results. This needs **no API key**. It uses the session's own Claude auth and works the same locally and in cloud sessions (sub-agents behave the same in cloud sessions per the Claude Code docs, accessed 2026-09-25).
  - `api`: direct Anthropic API or Batch API for large unattended runs, with `ANTHROPIC_API_KEY` from `.env` locally (gitignored, loaded with `uv run --env-file .env`) or from Google Secret Manager on Cloud Run (DR-0009).
  - `gemini` (future, maintainer suggestion): when the MCP server runs on Cloud Run (DR-0009), it can run T2 cards server-side with a Gemini Flash-class model through Google's managed model platform (Vertex AI, renamed in 2026, see `documentation/research/prose-signals/a-google-cloud-nl-vertex.md`). It authenticates with the Cloud Run service account, so there's no API key, and bills to the existing Google Cloud account. Claude calls a tool such as `card(asset_id)` and gets back only the small card, so bulk text never enters Claude's context. The same prompt files and pydantic card schema apply (use Gemini's structured-output mode). Verify the current model names, pricing, and structured-output support at build time, and spot-check card quality against the Haiku baseline, since dispositions must be comparable across backends. It could also serve as the cross-family second-opinion judge in M7.
  - Cloud Claude Code with the `api` backend: environment variables on a cloud environment are readable by anyone using that environment, and the docs warn against putting secrets there. Proxy-attached "API credentials" exist only on Pro/Max plans, not Team/Enterprise yet. So cloud sessions use the `subagent` backend.
