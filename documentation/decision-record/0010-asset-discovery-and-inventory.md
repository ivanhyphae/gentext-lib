# 0010. Asset discovery and inventory (module M11)

- Status: Accepted (2026-09-25)
- Date: 2026-09-25
- Deciders: Ivan Heitmann; Claude (drafting)

## Context
- The maintainer: *we should keep track of proposal assets that may not exist in the library yet… a discovery phase and an inventory aren't really represented… there was an EHCRP Round 1 that could be useful reference material, and there are entire proposals in Google Drive that should be considered for inclusion. Claude can largely do this automatically via the Google connector but needs a method and a store for the manifest.*
- DR-0003's M0 (Ingest) starts from files already in hand. Nothing covers *finding* them, deciding which are worth having, or remembering what was already rejected.
- First probes (2026-09-25):
  - **Drive search via the connector works well on metadata.** Three queries surfaced ~85 files. They included submitted proposals (Fresno 2024, EPA Dallas Green Spine), the live Google Doc behind the pilot DOCX, a 2023 "Extreme Heat Grant" folder, the DePave LA report, capability decks, and the "Upcoming Grants" pipeline sheet.
  - **The results are noisy.** Vendor quotes to Hyphae, IT RFPs, and meeting notes all came back, so triage is essential.
  - **Web search found the public EHCRP Round 1 awards list** and related LCI pages.
- Connector limits: `download_file_content` returns base64 through the model context, which is impractical for multi-MB binaries. `read_file_content` gives a text rendering (with comments for Google Docs), which is enough for triage and for simple ingest.

## Decision
1. Add **M11 Discovery & inventory**, upstream of M0. Module numbers are ids, not order.
2. **Store:** plain YAML in git, like the library (DR-0005).
   - `inventory/assets.yaml`: one record per asset. It's a list, human-diffable, and validated by pydantic (`src/gentext/inventory.py`).
   - `inventory/sweeps.yaml`: a log of discovery runs (who, when, system, exact queries, counts). Every asset links to the sweep that found it, so each search can be reproduced and audited.
   - `inventory/index.md`: **generated** progressive-disclosure view (counts, then open work, then holdings, deferred, excluded, sweeps). A test fails if it's stale.
3. **Lifecycle:** `wanted → discovered → include | defer | exclude → acquired → ingested → harvested`.
   - `wanted` covers things we know should exist but haven't located (cited reports, the Full Application workbook, pre-app feedback, community quotes). It requires a `hint`.
   - `exclude` records are kept so sweeps don't re-triage them.
4. **Dedup key:** `(location.system, location.id)` is unique, and slugs are unique. `gentext inventory find <system> <id>` is the pre-write check.
5. **Method:** the `skills/asset-discovery/SKILL.md` Agent Skill. It sets query patterns, metadata-first triage, priority rules (1 = live application, 2 = library value, 3 = nice to have, exclude), web sweeps, and close-out (validate → index → test → commit).
6. **Acquisition paths:**
   - **connector-text:** Google Docs via `read_file_content` → `sources/<asset-id>/…md`.
   - **drive-api:** a small script using the team's Google Cloud credentials. It uses Docs API `includeTabsContent`, which also tests the tab/style question from the research. It will be written when needed.
   - **manual:** a human downloads into `projects/` or `sources/`.
   - **web:** fetch public URLs.
   - **Size rule:** don't commit binaries over 25 MB; commit their text export, and keep the Drive id as the source of truth.
7. Acquired files record `local.path` + `sha256`. M0's manifest then refers to the inventory id, so provenance runs asset → source file → chunk.

## Consequences
- Claude, in Code or on the web with the Drive connector, can run sweeps unattended and leave an auditable trail. Humans review triage in `index.md` diffs.
- The inventory doubles as a to-do list for the live application. The priority-1 `wanted` items are exactly the evidence gaps in the Harm Reduction answers: CCHS 2015, CHAT, VCP/DAC records, community voices.
- One YAML file will get long (hundreds of records). That's acceptable. Revisit and split per system if merge conflicts appear.
- `owner` emails from Drive are stored as "who to ask". That's consistent with DR-0004 (relaxed) and DR-0008 (accountability).

## Alternatives considered
- **A spreadsheet in Drive:** familiar to the team, but not validated or versioned alongside the code, and awkward for agents to update safely. We could mirror it to a Sheet later, one-way.
- **One file per asset:** merge-friendly, but hundreds of tiny files for mostly excluded items. A single list is easier to scan and diff at this scale.
- **Adding it to the M0 manifest:** it conflates "things we might want" with "files we converted".

## Revisions
