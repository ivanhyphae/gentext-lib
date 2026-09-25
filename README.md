# adapt-rfp

**Adapt Hyphae's existing proposal writing to the standard a new solicitation sets.**
Find and triage past material, extract reusable passages with provenance, model what each RFP/NOFA actually asks for, and check drafts against it, with Claude doing the reading and writing and people making the calls.

> **Working on it?** Start at [`documentation/status.md`](documentation/status.md) (current state, next steps, how to resume in a cloud session), then [`AGENTS.md`](AGENTS.md) (working agreements for people and agents).

---

## Why

Every proposal Hyphae writes rebuilds from the same raw material: firm experience, project outcomes, methods, site context, partner track records. That material sits in dozens of Google Docs, PDFs and decks, copied forward from one application to the next. The copying causes problems:

- **Duplicates and forks.** The same boilerplate lives in many working docs in slightly different versions.
- **Context leakage.** Text reused from one client still names the old one. A real example: "…for Fresno County" inside a Bay Point application.
- **Inconsistency.** The same acronym gets two expansions (UTCI), and partner names get misspelled.
- **Missing evidence.** Facts and figures lose their sources, and drafts miss what the rubric rewards.
- **Unknown authorship.** Hyphae, partner and AI-written text blend together, so when something is wrong nobody knows who to ask.

Meanwhile each solicitation sets its own bar: exact questions and word limits, scoring rubrics, budget rules, and guidance scattered across FAQs, TA guides and external criteria. adapt-rfp treats the archive and the bar as two structured, inspectable things, and does the work of fitting one to the other.

## How it works

```
                 DISCOVER                    TRIAGE (spend tokens in proportion to value)                 ADAPT (next)
  Google Drive ─┐                    ┌──────────────┐   ┌──────────────────┐   ┌─────────────────────┐
  funder sites ─┼─► inventory ─────► │ T1 profile   │─► │ T2 card (Haiku)  │─► │ T3 extract (Sonnet) │─► library ─► compose ─► check
  local files  ─┘   (what exists,    │ no LLM: text,│   │ bounded: outline │   │ verbatim chunks +   │   (T4)      (M6)      (M7)
                     what's wanted)  │ outline, dups│   │ + openings →     │   │ quoted facts, by    │     ▲                   ▲
                                     └──────────────┘   │ hold / reference │   │ anchor, never       │     │                   │
                                                        │ / ignore / drop  │   │ paraphrase          │     │                   │
                                                        └──────────────────┘   └─────────────────────┘     │                   │
                                                                                                           │                   │
  SOLICITATION MODEL ── questions (verbatim from the form) · standards (every doc that sets the bar, with precedence) · requirements
                        · applications (one per site × partner permutation) ────────────────────────────────┴───────────────────┘
```

- **Discover (M11).** An inventory of every asset we have or want, with a reproducible sweep log. Agents sweep Drive and funder websites following a written method ([`skills/asset-discovery`](skills/asset-discovery/SKILL.md)).
- **Profile (T1, free).** Deterministic text extraction (pandoc with Google Docs tab awareness, pdftotext/pypdf, openpyxl), a section outline, contact-detail counts, and near-duplicate detection across the whole corpus.
- **Card (T2, Haiku 4.5).** One small bounded call per document. The model sees the outline and section openings, never the whole document, and returns a validated triage card: summary, a disposition (**hold / reference / ignore / drop**), which live questions or gaps it serves, reusable sections, fact candidates, and flags such as context-leakage risk.
- **Extract (T3, Sonnet 5).** Only for held sections, in order of need. The model proposes chunks as *start/end anchors*, and code slices the exact source text, so a candidate can never contain paraphrased or invented prose. A fact survives only if its supporting quote appears verbatim.
- **Solicitation model.** Questions copied word-for-word from the actual form (the form wins over the guidelines; differences are recorded), plus a list of every *standard* that sets the bar, requirements not tied to a question, and one record per application permutation. Standards are never mined for prose; they define what gets checked.
- **Adapt (next).** Promote candidates into a curated library with provenance, build a fact registry, compose answers per application, and check them (word limits, leftover notes, leakage, glossary, rubric evidence, prose quality) before a human pastes them into the team's Google Doc.

## Status

Built during a pilot on a **live application**: LCI's Extreme Heat and Community Resilience Program, Round 2, Early Infrastructure, with two ARPD-led applications for Ambrose Memorial Park and Ambrose Center Park in Bay Point (due 2026-10-13). The pilot is a shadow contribution alongside the lead writer's normal Google Docs process.

| Component | State |
|---|---|
| Discovery & inventory (M11) | ✅ 182 assets tracked; 104 acquired into `sources/`; 9 wanted, including evidence gaps |
| Profile (T1) | ✅ all acquired sources |
| Cards (T2) | ✅ 104 cards: 55 hold, 46 reference, 3 ignore |
| Extraction (T3) | ✅ 111 candidate chunks from the first 6 hold documents (to be redone with Sonnet, in need order) |
| Solicitation model | ✅ EHCRP R2: questions, standards, requirements, 3 applications |
| Library promotion, fact registry, compose, checks | ⏳ next ([`documentation/backlog.md`](documentation/backlog.md)) |
| Skills / MCP server for Claude web | ⏳ later (Cloud Run, [DR-0009](documentation/decision-record/0009-deployment-path.md)) |

Total model spend to build and run all of the above: **about $2.30**.

## Quick start

```bash
uv sync                                   # Python 3.12 + repo-local .venv (uv-managed; see DR-0006)
uv run pytest -q

uv run adapt-rfp inventory validate       # check the manifest
uv run adapt-rfp inventory index          # regenerate inventory/index.md
uv run adapt-rfp inventory list --status wanted

uv run adapt-rfp profile                  # T1 for every acquired asset (no LLM)
uv run adapt-rfp card show-prompt <id>    # see exactly what the model will see
uv run adapt-rfp extract --plan           # which held sections would be extracted
```

**With an API key** (local only: put `ANTHROPIC_API_KEY` in `.env`, which is gitignored):

```bash
uv run --env-file .env adapt-rfp card run [ids]      # Batch API, Haiku; skips unchanged docs; logs cost
uv run --env-file .env adapt-rfp extract [ids]       # Batch API, Sonnet; raw outputs saved
uv run adapt-rfp extract --revalidate build/extract-raw/<run>   # re-slice saved outputs for free
```

**Without a key** (Claude Code cloud sessions): both model tiers have a sub-agent path.
`card prepare` / `extract --prepare` write self-contained prompt files, Claude Code sub-agents answer them, and `card ingest` / `extract --revalidate` validate and save. See [`documentation/status.md`](documentation/status.md#resuming-in-a-cloud-session). Setup script for cloud environments: [`scripts/cloud-setup.sh`](scripts/cloud-setup.sh).

## Repository layout

```
AGENTS.md / CLAUDE.md          working agreements for people and agents (CLAUDE.md just imports AGENTS.md)
documentation/
  status.md                    start here: state, next steps, handoff
  backlog.md                   tooling not yet built
  decision-record/             numbered decisions (DR-0001 … 0013)
  research/                    progressive-disclosure research wiki (~150 pages, start at index.md)
inventory/                     assets.yaml (manifest), sweeps.yaml (sweep log), index.md (generated),
                               profiles/ (T1), cards/ (T2), card-runs.yaml (cost log)
solicitations/<funder>/<program>/<round>/
                               solicitation.yaml (+ standards), questions.yaml, requirements.yaml, applications/
sources/<asset-id>/            acquired files and text exports
projects/                      original pilot sources as first received
library/_candidates/           T3 candidate chunks (verbatim, with provenance); not yet the library
skills/asset-discovery/        Agent Skill: how to sweep Drive/web into the inventory
src/adapt_rfp/                 package + CLI: inventory, extract (text), profile, card, candidates
tests/                         pytest
scripts/cloud-setup.sh         Claude Code cloud environment setup
```

This is a **private repository**. It holds client and partner documents on purpose; see [DR-0004](documentation/decision-record/0004-source-corpus-confidentiality.md).

## Principles

- **Never invent.** Every claim that goes to a funder traces to a source. Gaps show up as visible notes, e.g. `{>>TK source: tree count, Stockton AB 617<<}`, never as plausible filler.
- **Verbatim by construction.** Extraction slices real text; models point at it and never rewrite it.
- **Authorship is provenance.** Every chunk records who wrote it (a person, org, or AI model with its inputs) and who reviewed it, so problems can be traced and someone can answer for them ([DR-0008](documentation/decision-record/0008-authorship-provenance.md)).
- **Standards ≠ content.** Documents that set the bar are modeled and checked against; documents we draw from are mined. The two are never confused.
- **Spend tokens in proportion to value.** Free deterministic steps first, cheap bounded model calls next, expensive reasoning only where it pays ([DR-0011](documentation/decision-record/0011-content-triage-funnel.md)).
- **Plain text in git.** Canonical data is Markdown and YAML you can diff and review. Indexes and caches are derived and rebuildable ([DR-0005](documentation/decision-record/0005-canonical-store-plain-text.md)).
- **People decide.** Models triage, extract and draft. Promotion into the library, approval of drafts, and anything sent outside the team are human calls ([DR-0007](documentation/decision-record/0007-collaboration-workflow-shadow-pilot.md)).

## Models

| Tier | Model | Why |
|---|---|---|
| Cards (T2) | Claude Haiku 4.5 | In a side-by-side test Sonnet 5 agreed on 10/12 dispositions at ~8× the cost |
| Extraction (T3) | Claude Sonnet 5 | Beat Haiku on chunk boundaries (library-sized chunks), quoted facts (39 vs 22) and anchor accuracy (3% vs ~11% misses) |
| Composition & review (next) | Claude Opus, in session | Where judgment and voice matter |
| Future option | Gemini on Google Cloud | Server-side cards on the Cloud Run MCP server; cross-family second-opinion reviewer |

## Goals

The original intent of the project, and where each stands:

- **Catalog archival proposal copy** (grants, qualifications, marketing) in an inventory with metadata: ✅ inventory, profiles, cards
- **Characterize text with classical NLP and embeddings**: ⏳ research done ([nlp-quality](documentation/research/nlp-quality/index.md), [prose-signals](documentation/research/prose-signals/index.md)); checks next
- **Graphs for semantics, if useful**: deferred on purpose; a derived RDF view only when specific triggers fire ([research](documentation/research/knowledge-representation/graph-decision.md))
- **A progressive-disclosure library of reusable chunks**: ⏳ candidates exist; promotion is next
- **Skills and plugins that let an LLM understand, generate and QC prose rigorously**: 🟡 CLI + one skill; more skills and a Cloud Run MCP server planned
- **A collaborative working surface for copy-editing**: 🟡 Claude Docs for iteration, human paste into Google Docs ([DR-0007](documentation/decision-record/0007-collaboration-workflow-shadow-pilot.md))
- **Inventory and check against solicitation requirements**: 🟡 solicitation model built; checks next
- **Quality-check output with NLP and embeddings**: ⏳ designed ([research](documentation/research/prose-signals/span-feedback-schema.md)); not built
- **Operable end-to-end from Claude web**: 🟡 works in Claude Code cloud sessions today; hosted MCP server later
