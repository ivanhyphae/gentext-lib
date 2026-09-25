---
name: asset-discovery
description: Discover, triage, and record proposal assets (past proposals, solicitations, award lists, reports, datasets, funder guidance) that are not yet in the adapt-rfp library, using the Google Drive connector and web search, into the inventory manifest at inventory/assets.yaml. Use when asked to "find past proposals", "what do we have on X", "sweep Drive", "inventory sources", "what's missing for this application", or before building library chunks for a new solicitation.
---

# Asset discovery

Maintain `inventory/assets.yaml` (records) and `inventory/sweeps.yaml` (run log) in the adapt-rfp repo. The schema and lifecycle are in `src/adapt_rfp/inventory.py` and DR-0010. This skill covers **discovery and triage**. Acquisition and ingest are separate steps.

## Lifecycle

`wanted` → `discovered` → `include` | `defer` | `exclude` → `acquired` → `ingested` → `harvested`

- **wanted**: we know or suspect it exists but haven't located it. Needs a `hint` (where to look, who to ask).
- **exclude**: kept, not deleted, so later sweeps skip it. Group near-identical siblings, such as vendor quote families or duplicate copies, under one record and list their ids in `notes`.

## Procedure

1. **Start a sweep.** Pick an id `s-YYYY-MM-DD-<system>-NN` and append an entry to `sweeps.yaml` with the `method` and exact `queries`. Keep it honest: record `found` (results seen) and `recorded` (records written).
2. **Seed `wanted` from the target.** For a solicitation or working doc, list everything it references that we don't hold: cited reports, data tools, prior rounds, award lists, FAQs/webinars, forms, templates, and things teammates promised in meeting notes.
3. **Search Drive with metadata only.** Use `search_files` with `excludeContentSnippets: true` and `pageSize` 30–50. Query patterns that work:
   - Program and funder terms: `fullText contains 'Extreme Heat' and fullText contains 'Resilience'`, `title contains 'EHCRP'`
   - Document roles: `title contains 'proposal' or title contains 'narrative' or title contains 'RFP'`
   - Known projects and places from the library or boilerplate (Prescott, Stockton, Oakland STEP, Green Spine, AdaptOS, Bay Point…)
   - Folder walks: `parentId = '<folder id>'` for any folder recorded as `include`
   - Recency: `modifiedTime > '<date>'` for incremental sweeps
   - Page with `pageToken` until results stop being relevant, and say in the sweep notes where you stopped.
4. **Dedup before writing.** For each hit, run `uv run adapt-rfp inventory find gdrive <fileId>`. Exit code 0 means it's already recorded: update it if the metadata changed, and never create a duplicate.
5. **Triage from metadata first.** Title, owner, folder, mime, size, and dates are usually enough. Read content (`read_file_content`) only when the title is ambiguous and the item could be priority 1–2. Priority:
   - **1**: needed for a live application (currently EHCRP R2, due 2026-10-13)
   - **2**: high library value: submitted proposals, project deliverables with citable facts, current capability decks
   - **3**: nice to have
   - **exclude**: not Hyphae proposal prose or evidence (vendor quotes to us, IT, unrelated programs)
   - Meeting notes are `kind: notes`, `defer`. They're context only, never library chunks (DR-0004).
6. **Record each asset.** Required fields:
   - `id`: a readable slug, stable forever
   - `title`, `kind`, `status`, `priority`
   - `location`: system, id, url, mime, size, modified, owner, parent
   - `relevance.note`: *why* it matters, naming the chunk types or rubric question it serves
   - `discovered`: date, model id, sweep id
7. **Web sources.** Use WebSearch for funder pages: prior-round award lists, FAQs, webinar slides, cited reports. Record them with `system: web` and a `url`.
8. **Close out.** Run `uv run adapt-rfp inventory validate`, then `uv run adapt-rfp inventory index`, then `uv run pytest -q tests/test_inventory.py`. Commit `assets.yaml`, `sweeps.yaml`, and `index.md` together, with a message summarising the sweep's counts.

## Acquisition (after triage, per DR-0010)

- **Google Docs, text-only is enough:** the connector's `read_file_content` (with `includeComments: true` for working docs) → save under `sources/<asset-id>/<asset-id>.md` → set `status: acquired`, `local.via: connector-text`, and `local.sha256`.
- **Binary files and tab/style-faithful Docs:** don't pull them through the connector. `download_file_content` returns base64 through the model context, which is impractical beyond ~1 MB. Mark them `include` and leave them for the Drive API script or a manual download (`local.via: drive-api | manual`).
- **Large binaries (>25 MB):** commit the text export only, and record the Drive id as the source of truth.

## Guardrails

- Read-only against Drive. Never move, rename, share, or edit files.
- Don't copy personal contact details into records beyond the Drive `owner` (the person to ask).
- Don't guess file ids. Only record ids returned by the connector.
