---
title: "Claude Docs ↔ Google Docs workflow"
slug: docs-roundtrip
level: 2
parent: index.md
related: [claude-docs.md, google-drive-connector.md, delivery-architecture.md, ../provenance/index.md]
tags: [collaboration, claude-docs, google-docs, M9, harvest]
status: draft
updated: 2026-09-25
---

# Claude Docs ↔ Google Docs workflow

> **TL;DR** Draft and iterate in **Claude Docs**, one doc per application and one tab per question. Claude writes, comments and revises there through the Docs connector. Harvest reviewed text back into `library/` through a adapt-rfp tool that records lineage. A human pastes the final blocks into the tabbed **Google Doc**. Claude can read that Google Doc afterwards through the Drive connector for a final QA pass, but it can't edit it.

## The loop

```
library/ + solicitation YAML
   │  (skill: draft-answer → MCP/CLI: draft_context, check_draft)
   ▼
Claude Docs  ── one doc per application, one tab per question ──
   │  humans edit inline and comment; "@Claude" threads trigger revisions
   │  (skill: check-draft re-runs checks on the tab's text; QA notes as comments)
   ▼
harvest  (skill: harvest-edits → propose_variant → git branch/PR)
   ▼
Google Doc (tabbed, final)  ← human pastes blocks
   │  (Drive connector: read_file_content → adapt-rfp check on the final text)
   ▼
submission
```

## What each surface can actually do (verified 2026-09-25)

| Need | Claude Docs | Google Drive connector |
|---|---|---|
| Claude creates a doc | Yes, via the Docs connector (`batch` create) | Creates *new* files. Text uploads convert to Google Docs by default *(observed in the tool schema)* |
| Claude edits existing text | Yes: find/replace, block replace, insert, table cells | **No.** `update_file` changes only title and parent folder *(observed tool schema)*; third-party coverage agrees ([usecarly](https://www.usecarly.com/blog/claude-google-docs-integration/)) |
| Tabs | Yes: create, order, nest | Reads Docs as Markdown. Whether all tabs of a tabbed Doc come through is *(unverified)* |
| Comments | Claude reads threads, replies, anchors comments on words; mentions route to Claude | Docs page: "can't read a file's comments or suggested edits". The tool schema in this session exposes `includeComments` *(conflict, test it)* |
| Export | Word, PDF, Markdown (connector guide, Docs help); help centre also lists Google Docs *(conflict)* | n/a |
| Version history | **None** | Google's own |
| Sharing | Team/Enterprise: inside the org only; Pro/Max: link | Google's own |

Sources: [Claude Docs help](https://support.claude.com/en/articles/16923645-get-started-with-claude-docs), [Google Drive connector docs](https://claude.com/docs/connectors/google/drive), plus the Claude Docs connector's own guide text and the Drive tool schemas read in this session.

## Design choices

**One Claude Doc per application, one tab per narrative question.** This matches the tabbed Google Doc, so each paste is tab → tab. Put question id, word limit and points in the tab name or lead line (from M5). A "QA" tab holds the latest `check_draft` summary.

**Provenance travels as comments, not inline markup.** Inline `[chunk:…]` tags would get pasted into the Google Doc by accident. Anchor a comment on each adapted sentence with its chunk/fact ids instead. Keep `{>>TK source: …<<}` placeholders inline, because they *should* block a paste. Comment limits: 1000 threads per doc and 100 comments per thread (Docs connector guide).

**Harvest is Claude-mediated.** Our MCP server can't read Claude Docs. Only Claude can, through the Docs connector. The `harvest-edits` skill tells Claude to read the tab, diff it against the draft that `draft_context` produced, and call `propose_variant(chunk_id, text, lineage={edited_in: <doc link>, tab, date})`. The fallback is Export → Markdown, then `adapt-rfp harvest file.md`.

**Git is the history.** Claude Docs keeps no versions, so snapshot a tab's text into the harvest PR at each milestone (review round, submission).

**Final check on the Google Doc.** After pasting, Claude reads the Google Doc through Drive (Markdown conversion) and runs `check_draft` on each section. This catches paste errors, leftover placeholders and leakage such as "Fresno County" before submission.

## Risks

- **Beta churn.** Claude Docs launched 2026-09-16 in beta ([Claude blog](https://claude.com/blog/cowork-is-now-claude)), so APIs and behaviour will move. Keep the workflow degradable to Export → Markdown.
- **Org gating.** It's off by default on Enterprise, and unavailable for CMEK, ZDR or HIPAA orgs (Docs help).
- **Confidentiality.** Draft tabs may quote internal strategy. Claude Docs sharing is org-internal on Team/Enterprise, but on Pro/Max anyone with the link can view (Docs help). Pick deliberately (DR-0004).
- **Two sources of truth during a deadline.** Freeze Claude Docs once pasting starts. Late edits go in the Google Doc and are harvested from it by reading through Drive.

## Pilot recipe (P0)

1. In Claude Code, run the `draft-answer` skill, which writes Markdown to scratch.
2. Claude creates the Claude Doc with one tab per question through the Docs connector (available in this Claude Code session as a claude.ai connector).
3. The team edits and comments. Claude answers the threads.
4. Run `check-draft` against each tab's text, then paste into the Google Doc.
5. After submission, run `harvest-edits` → PR.

Parent: [index.md](index.md)
