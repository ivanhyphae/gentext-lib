# Status and handoff: start here

> Last updated **2026-09-25**, end of the first working session (local Claude Code, Opus 5.5). The next session is expected to be **Claude Code in the cloud** (mobile). Read this page, then `AGENTS.md`, then whatever it points to.

## One-paragraph state

`adapt-rfp` has a working **intake funnel**:
1. discovery (M11)
2. deterministic profiling (T1)
3. Haiku triage cards (T2)
4. Sonnet extraction of verbatim candidate chunks (T3)

It also has a **solicitation model** for the live application (LCI EHCRP Round 2, due **2026-10-13 14:00 PT**) and a research wiki behind every design choice. Nothing has been *promoted* into the library, and no draft answers exist yet. That is the next phase (T4 promotion, M3 facts, M6 compose, M7 QA).

## The live application (real help, shadow contribution: DR-0002, DR-0007)

- **Applications:** two ARPD-led pre-applications, Ambrose Memorial Park and Ambrose Center Park (lead writer James; ARPD contact Lori), plus an exploratory I-ReLab track. Model: `solicitations/lci/ehcrp/round-2/` (`questions.yaml` is verbatim from the Full Application Form; `standards:` and `requirements.yaml` cover everything else that sets the bar).
- **Round 1 history:** Hyphae's R1 application (CEJC lead, COMMON project) was submitted and interviewed but not awarded, and LCI encouraged reapplying.
- **Findings for James:**
  - The Full Application Form's **Harm Reduction Q2 adds "expected harm reduction outcomes"**, and the TA guide wants measurable metrics with who/how/when. Current drafts have none.
  - The Harm Reduction Q1 "High" band wants **community voices**. The best lead is `ambrose-resilience-hub-survey` (35 responses; James, March 2026). Needs consent and anonymization; it contains respondent emails.
  - **PSE Healthy Energy 2026** names Bay Point an acute PM2.5 hot spot. It is newer evidence than the 2015 CCHS report the drafts cite.
  - The "Monument Corridor" references in both pre-apps are a legitimate citation of the CCHS 2015 case study (p. 34), not context leakage.
  - The Round 1 awards PDF says 46 projects / ~$32M; LCI's web copy says 47 / $32.4M. Don't cite either without reconciling.
  - **Only the "SHORTENED VERSION" project description was submitted** in each pre-app (maintainer, 2026-09-26). Both working docs hold only the *Memorial* Park shortened version. The Center Park submitted text is a wanted asset (`ehcrp-r2-ambrose-center-preapp-submitted`, ask James). The longer working-doc answers (2a/5/6a) are drafts, not submissions.
  - **The Ambrose Community Center resilience hub is not part of the Center Park EHCRP proposal.** Its survey is still usable as evidence of residents' heat concerns (aggregates only).
  - **"Limited access to home air conditioning"** (both pre-apps) is not supported by its cited source: CCHS 2015 Table 3 (p. 32) rates Bay Point *Low* on that factor.
  - **LCI pre-app feedback, Center Park** (`sources/ehcrp-r2-preapp-feedback-center/`, 2026-09-26). The actionable items are in `applications/ambrose-center-park.yaml` → `preapp_feedback`:
    - **No Planning Document** in the narrative. It is the *primary* Early Infrastructure deliverable (§3.6), and the demonstration supports it.
    - **No harm reduction** in the description.
    - **Belonging** needs developing (Appendix B).
    - **CCRCD is not an eligible co-applicant.** Bay Point Garden Club or CSAHC would be; CCRCD can be a Contributor (§6.4).
    - **The funding-priority status must be SDAC, not DAC.**
    - The core infrastructure itself was judged clearly defined and eligible.
  - Memorial Park feedback is still wanted (`ehcrp-r2-preapp-feedback`).
- **Drafts in progress:** `solicitations/lci/ehcrp/round-2/applications/ambrose-center-park/answers/hr-q1.md`, `hr-q2.md` (draft-2). Q2 is blocked on the submitted scope.

## Where things are

| What | Where | State |
|---|---|---|
| Decision records | `documentation/decision-record/` (0001–0012) | 0011 and 0012 accepted provisionally (revisit after the EHCRP application) |
| Research wiki | `documentation/research/index.md` | 9 topics, ~150 pages |
| Inventory | `inventory/assets.yaml` (182 records), `index.md`, `sweeps.yaml` | 104 acquired, ~72 include/defer, 8 wanted |
| Sources | `sources/<asset-id>/` + `projects/EHCRP Round 2/` | committed (private repo) |
| Profiles (T1) | `inventory/profiles/<id>.yaml` | all acquired |
| Cards (T2, Haiku, prompt c3) | `inventory/cards/<id>.yaml`, cost log `inventory/card-runs.yaml` | 104 cards: 55 hold / 46 reference / 3 ignore |
| Candidates (T3) | `library/_candidates/<asset>/<sid>-<n>-<slug>.md`, `extract-runs.yaml` | 111 candidates from the first 6 hold docs, extracted with **Haiku** (before Sonnet became the default) |
| Skill | `skills/asset-discovery/SKILL.md` | discovery method |

Total model spend so far is about **$2.30** (cards ≈ $1.00, extraction ≈ $0.15, Sonnet comparison tests ≈ $1.20).

## Model choices (tested 2026-09-25)

- **Cards: Haiku 4.5.** Sonnet 5 agreed on 10 of 12 dispositions at about 8× the cost and was, if anything, more generous with `hold`.
- **Extraction: Sonnet 5** (now the default in `candidates.py`). On the same 6 sections Sonnet gave 32 library-sized chunks vs Haiku's 13 (some over 1,000 words), 39 quoted facts vs 22, and 3% anchor misses vs ~11%. Cost is about $0.07/section sync, roughly half that in a batch.

## Resuming in a cloud session

1. **Environment setup script:** `scripts/cloud-setup.sh` (installs uv if missing, runs `uv sync`; poppler is optional because PDF extraction falls back to pypdf). The `build/` text cache is gitignored and rebuilds automatically.
2. **No API key in cloud sessions** (DR-0011): the key lives in the local `.env` (gitignored). On Team plans, cloud-environment variables are readable by anyone using the environment, so don't put the key there. Use the **sub-agent backends** instead:
   - Cards: `uv run adapt-rfp card prepare [ids]` → a Haiku sub-agent per file in `build/card-prompts/` returns card JSON → collect into `{asset_id: card}` → `uv run adapt-rfp card ingest results.json`.
   - Extraction: `uv run adapt-rfp extract --prepare [ids]` → a Sonnet sub-agent per file in `build/extract-prompts/` writes its JSON to `build/extract-raw/<run>/<asset>__<sid>.json` → `uv run adapt-rfp extract --revalidate build/extract-raw/<run>`.
3. **Google Drive:** discovery and acquisition use the claude.ai Google Drive connector if the session has it. Otherwise work from what is already in `sources/`.
4. **Work on a branch, never on `main`** (AGENTS.md → Git). Commit at your own judgment, push the branch, and open a PR for the maintainer to merge.

## Next steps (in order)

1. **Re-extract with Sonnet** (batch, or sub-agents in the cloud), in need order, not all 55 holds. The first targets are the Bay Point / Ambrose holds:
   - `ehcrp-r2-ambrose-memorial-gdoc` and `ehcrp-r2-ambrose-center-gdoc` (live versions)
   - `ambrose-center-park-gi-additional-funding`
   - `ambrose-center-park-ceqa-project-description`
   - `ehcrp-r1-cejc-common-application-draft`
   - `ambrose-memorial-ugg-concept-form`
   - `willow-pass-bus-stop-gi-concept`
   - `past-proposals-doc`
   - Handle `ambrose-resilience-hub-survey` separately: personal data, quotes need consent.
2. **Build the Bay Point fact registry (M3)** from candidate facts, verifying each against its source (page numbers, access dates). Start with CCHS 2015, CHAT, VCP/DAC tract designations, PSE 2026, and the Highway 4 / Willow Creek / land-donation site facts.
3. **Draft Harm Reduction Q1 + Q2** per application, from facts and candidates. Every claim needs provenance; gaps become `{>>TK …<<}`. Run the checks (word limit, leakage, glossary/UTCI, rubric evidence), then iterate in **Claude Docs** with the maintainer (DR-0007). Nothing goes to James until the maintainer approves.
4. Then Partnership Q2, using the ARPD/Ambrose Center Park green-infrastructure track record.

See `documentation/backlog.md` for the tooling backlog.

## Open questions for the maintainer

- Is there any Round 1 interview or feedback material (Brent)? It is recorded as a wanted asset.
- Which funders were behind the successful Ambrose Center Park green stormwater grants? (Wanted item; the "Ambrose Stormwater" folder is not yet walked.)
- Should "card" be renamed (e.g., "triage record")? It was borrowed from catalog cards / model cards.
