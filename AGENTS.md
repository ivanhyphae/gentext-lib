# AGENTS.md

Guidance for AI agents (Claude Code, Claude web, others) and human collaborators working in `gentext-lib`.

## What this repo is

A library and toolkit for Hyphae's **archival proposal prose**: grant narratives, qualifications, firm experience, project descriptions, and marketing copy. The goals (see `README.md`):

1. Catalog source documents and the reusable text chunks inside them, with metadata and provenance.
2. Characterize chunks with classical NLP and embeddings.
3. Model solicitations (RFPs/NOFAs) as checkable requirements.
4. Compose new drafts from library chunks, then quality-check them against requirements, facts, and style.
5. Expose all of this to an LLM as skills/plugins, with a collaborative editing surface.

The module plan lives in `documentation/decision-record/0003-module-decomposition.md`. Read it before adding code.

## Repo layout

```
README.md                         intent and targets
AGENTS.md                         this file
documentation/decision-record/    numbered decision records (see below)
documentation/research/          progressive-disclosure research wiki (start at index.md)
projects/                         RAW client/solicitation sources, committed (private repo, DR-0004)
```

Planned (not yet created; see DR-0003): `library/` (canonical chunks as Markdown), `solicitations/`, `src/gentext/`, `skills/`, `tests/`.

## Pilot case

**EHCRP Round 2**: California LCI Extreme Heat and Community Resilience Program, Early Infrastructure tier, Ambrose Memorial Park / Bay Point (Contra Costa), with a sibling CNRA Urban Greening concept proposal for Bay Point transit stops. Sources are in `projects/EHCRP Round 2/`. Full application due **2026-10-13 14:00 PT**.

This is a **real application, and the goal is real help.** It is a *shadow contribution*: the lead grant writer (James) runs the customary Google Docs authoring process, and this pilot runs in parallel. Output is offered as paste-ready text blocks, iterated in Claude Docs; a human pastes them into the final Google Doc (DR-0007). Never edit the team's Google Docs directly, and never contact partners or funders. See DR-0002 for what the pilot contains and what it teaches us.

## Working agreements

### Decision records
- Every structural choice (module boundaries, storage, schemas, dependencies, deployment) gets a record in `documentation/decision-record/NNNN-kebab-title.md`, using the template in that folder's `README.md`.
- Records are iterative. Start as **Proposed**, then move to **Accepted** after a human agrees. If a decision changes, write a new record that **Supersedes** the old one; don't rewrite history. Small clarifications to an existing record go in its `Revisions` section, with the date.
- Add every new record to the index in `documentation/decision-record/README.md`.
- If you're unsure whether something needs a record: if a future collaborator would ask "why is it like this?", write one.

### Confidentiality
- This is a **private repo**. Sample and pilot sources under `projects/` are committed deliberately (DR-0004). They still contain personal contact details, internal meeting notes, partner assessments, and pre-decisional strategy, so never copy raw source text into anything *outside* the repo (public artifacts, shared links, web tools, third-party APIs) unless a human asks.
- Only text that has been deliberately promoted into `library/` (with a `sensitivity` tag) is shareable, and only according to that tag.
- Meeting notes and internal strategy are *context*, not library chunks, unless a human promotes them.

### Truthfulness of prose
- This system produces claims made to funders. **Never invent** facts, figures, dates, dollar amounts, partner names, quotes, or citations. Any factual claim in generated text must trace to a library chunk or fact with provenance. If no source exists, leave a visible placeholder such as `[[NEEDS SOURCE: tree count for Stockton project]]`.
- Keep the lineage when adapting a chunk (which chunk, which variant, what changed).
- **Authorship is essential provenance.** Final proposals mix Hyphae, partner, and AI-written text without distinction, but the library must record who wrote what: human author/org, or AI model + inputs, and who edited or approved it. Record it at chunk level always, and at span level where it matters (DR-0008).
- Watch for **context leakage**: text reused from one client/place and still naming the old one. The pilot contains a real case: firm boilerplate in the Bay Point doc ends with "…for Fresno County."

### Terminology
- Canonical terms and acronym expansions go in a controlled glossary (planned: `library/glossary/`). Known pilot collision: UTCI appears as both "Universal Thermal Climate Index" (correct) and "Urban Thermal Comfort Index". Use the glossary form.
- Funder vocabulary (e.g., EHCRP's *Harm Reduction, Partnership, Belonging, Lasting Community Benefits*) belongs to the solicitation model. Don't mix it into the firm glossary.

### Working with source files
- Tools present on the dev machine: `pdftotext` (poppler) and `python3`. `pandoc` and `python-docx` are not installed. DOCX can be read with stdlib `zipfile` + `xml.etree` on `word/document.xml`.
- Write extraction output and other intermediates to a scratch/temp directory, not the repo, until the ingest module defines where derived text lives.

### Code conventions (proposed, see DR-0006)
- Python ≥3.12, managed with `uv`, matching the sibling `hyphae_ai_skills` repo.
- Plain-text canonical data (Markdown + YAML frontmatter). Databases and indexes are *derived* and must be rebuildable from the repo.
- Skills follow the Anthropic skill format (`SKILL.md` + scripts + references).

### Related repos (siblings in `hyphae-dev/`)
- `hyphae_ai_skills`: existing Hyphae Claude skills (bpmn, tana-paste, graph-charts, everhour).
- `design-system`: Hyphae brand/design system, for any rendered output.
- The `graph-keeper` skills (RDF/Turtle knowledge graph in git) are candidates for the optional semantic-graph layer (DR-0003, M3).

### Git
- Until the maintainer says otherwise (expected at a milestone), **work directly on `main` and commit at your own judgment**: small, coherent commits with descriptive messages, whenever a unit of work is done (a DR, a research topic, a module step). Don't push unless asked.
- Do not commit generated indexes, embeddings, or bulk extracted text. Those are derived and rebuildable.
