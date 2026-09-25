---
title: Google Drive connector
slug: google-drive-connector
level: 3
parent: index.md
related: [docs-roundtrip.md, claude-docs.md, claude-projects.md]
tags: [google-docs, google-drive, connector, M0, M9]
status: draft
updated: 2026-09-25
kind: service
verdict: adopt
fit: [M0, M7, M9]
license: proprietary (Google-built connector)
maturity: mature
inspectability: medium
sources:
  - title: Google Drive connector (Claude docs)
    url: https://claude.com/docs/connectors/google/drive
    accessed: 2026-09-25
  - title: Use Google Workspace connectors (Help Center)
    url: https://support.claude.com/en/articles/10166901-use-google-workspace-connectors
    accessed: 2026-09-25
  - title: "Claude + Google Docs: what the integration can and can't do (third party)"
    url: https://www.usecarly.com/blog/claude-google-docs-integration/
    accessed: 2026-09-25
---

# Google Drive connector

> **TL;DR** Google builds and runs this connector, and it lets Claude search Drive and **read** Docs (as Markdown), Sheets (CSV) and Slides. It can **create** new files but **can't edit an existing Google Doc's content**. **Adopt** for reading: intake of team drafts and a final QA pass on the submission Doc. Human pasting into the final Doc stays.

## What it is

- **Tools** (schemas observed in this session, 2026-09-25): `search_files`, `list_recent_files`, `get_file_metadata`, `get_file_permissions`, `read_file_content`, `download_file_content`, `create_file`, `copy_file`, `share_file`, `trash_file`, and `update_file`, which changes **title and parent folder only**.
- **Read.** Google Docs, Sheets, Slides, PDF, Office, ODF and images. Docs arrive as Markdown without images. The Google export cap is ~10 MB, and very large files may come back incomplete.
- **Comments.** The official page says Claude "can't read a file's comments or suggested edits". The tool schema in this session has `includeComments` for Docs, Sheets and Slides. *Conflict: test on a real Doc.*
- **Tabs.** Whether a tabbed Google Doc's non-first tabs are all included is *(unverified)*. Test it before relying on the final QA read.
- **Create.** Uploads text, with conversion to native Google Docs on by default. Creating a Doc from our Markdown is possible, but formatting fidelity is *(unverified)*.
- **Setup.** Each user signs in with their own Google account. On Team/Enterprise an Owner must add the connector first. Drive files can go into project knowledge only in *private* projects.
- **Timeline.** Workspace connectors expanded in 2026. Third-party reporting puts the integration update at 2026-02-24 *(secondary source)*.

## Why it matters for gentext

The team works in Google Docs today (DR-0003 Q5), and the final application is a tabbed Google Doc. The connector lets Claude read the team's working docs for **M0 ingest** without downloading DOCX files by hand. It also lets Claude read the **final** Doc so M7 checks can run on what will actually be submitted.

## How it would fit

- `ingest-source` skill: Drive search → `read_file_content` → `gentext ingest --stdin --source gdrive:<fileId>`, recording the file id and modified time in the manifest.
- Final QA: read the submission Doc → `check_draft` per section → report leftover `{>>TK …<<}`, leakage and word overruns.
- **Not** a write target for final prose. A human pastes (see [docs-roundtrip.md](docs-roundtrip.md)).
- For full Google Docs editing we would need our own MCP server calling the Google Docs API (`documents.batchUpdate`). Out of scope. *(assess later)*

## Strengths

- First-party, per-user OAuth, respects Drive permissions.
- Claude re-reads the live file each time, so it doesn't work from stale copies.

## Weaknesses / risks

- Can't edit existing content or suggest edits.
- Comment and tab coverage unclear (see above).
- Markdown conversion loses images and may flatten some structure.
- Confidential sources (DR-0004) flow into chat context. Keep them out of shared projects.

## Verdict rationale

Adopt for reading and verification, which is cheap and first-party. Its write limits are why Claude Docs is the iteration surface.

Parent: [index.md](index.md)
