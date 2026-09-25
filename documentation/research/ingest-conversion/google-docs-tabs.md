---
title: "Google Docs tabs: what the API can and can't do"
slug: google-docs-tabs
level: 2
parent: index.md
related: [apps-script-tab-export.md, pandoc.md, converter-comparison.md]
tags: [google-docs, tabs, docs-api, drive-api, apps-script, ingest]
status: draft
updated: 2026-09-25
---

# Google Docs tabs: what the API can and can't do

> **TL;DR** The Docs API fully supports tabs. `documents.get?includeTabsContent=true` returns `tabs[]`, with nested `childTabs`, and each tab has its own `documentTab` holding `body`, `namedStyles`, lists and inline objects. Text styles *are* available per tab. What the API lacks is **per-tab export**: Drive `files.export` (DOCX, Markdown, HTML) has no tab parameter. The only per-tab export is an undocumented `&tab=` URL parameter. The claim that "the API doesn't expose text styles with tabs" most likely comes from reading legacy top-level fields, which hold only the first tab, or from `TextStyle` holding only overrides.

## What the Docs API does (verified)

- **Two response shapes.** With `includeTabsContent=true`, content moves into `document.tabs`, and the top-level `body`, `documentStyle` and `namedStyles` stay empty. Without it, the top-level fields hold **only the first tab**, and `tabs` is empty. A field mask that names `tabs` implies `true`. ([documents.get](https://developers.google.com/workspace/docs/api/reference/rest/v1/documents/get))
- **Per-tab content.** Each `Tab` has `tabProperties` (id, title, index, nesting), `childTabs`, and `documentTab`. The `documentTab` carries body, headers, footers, footnotes, `documentStyle`, `namedStyles`, lists, named ranges and inline/positioned objects. ([Work with tabs](https://developers.google.com/workspace/docs/api/how-tos/tabs), updated 2026-09-03)
- **Links are tab-aware.** `link.bookmarkId` and `link.headingId` are deprecated in favour of `link.bookmark` and `link.heading`, which include a `tabId`. (same source)
- **Writes.** `batchUpdate` requests take a `tabId` and default to the first tab. The exceptions are `ReplaceAllText` and the named-range requests, which apply to all tabs. (same source)
- **Styles are inherited.** Each paragraph carries `paragraphStyle.namedStyleType` (e.g. `HEADING_2`), which is all a heading-based segmenter needs. `TextStyle` on a run holds **only explicit overrides**. Effective bold/size values have to be resolved against that tab's `namedStyles`. ([Structure of a document](https://developers.google.com/workspace/docs/api/concepts/structure))
- **Comments** are not in `documents.get`. They come from the Drive API comments resource *(standard behaviour, not re-checked today)*. Suggestions come inline via `suggestionsViewMode`.

**Verdict on the reported problem:** we could not confirm it from the documentation. A converter written before tabs existed (late 2024) that reads `document.body` will silently get only tab 1. One that sets `includeTabsContent` but still reads `document.body` will get nothing. Either failure would look like "styles missing". *(We have not reproduced this against a live tabbed doc. That needs OAuth to the team's Drive.)*

## What Drive export does

- `files.export` supports DOCX, `text/markdown`, HTML, zipped HTML, PDF, ODT, RTF, EPUB and TXT for Docs. ([Export MIME types](https://developers.google.com/workspace/drive/api/guides/ref-export-formats), updated 2026-09-03). Markdown import/export arrived in July 2024 ([Workspace Updates](https://workspaceupdates.googleblog.com/2024/07/import-and-export-markdown-in-google-docs.html)).
- **No tab selector.** Google's own developer-relations post says the official `files.export` API doesn't support per-tab exports. It uses the undocumented `https://docs.google.com/document/d/{ID}/export?format=pdf&tab={tabId}` and warns that it could change ([Poehnelt, 2025-10-28](https://dev.to/googleworkspace/exporting-individual-tabs-from-google-docs-as-pdfs-2903)). Community scripts use the same parameter with `format=html` ([gist](https://gist.github.com/alxzndr1/710ede4f71ba9a759cebc4b97454555a)).
- **Which tabs does the API export include?** This is not documented. The UI's File → Download asks "Current tab" or "All tabs", and the default is current tab ([Docs Help](https://support.google.com/docs/answer/15499791)). One third-party write-up says Drive export returns a single monolithic file with all tabs ([datacrew.space, 2025-01-15](https://datacrew.space/blog/google-drive-sync-split-tabs-markdown)) *(unverified)*.
- **Our pilot DOCX** (exported by the team) contains `Title`-styled paragraphs at what look like tab starts, plus 11 section breaks. It appears to be an "all tabs" export. Tab ids are lost in the DOCX. *(Mapping unverified.)*

## Apps Script

`DocumentApp` has `Document.getTabs()`, `Tab.getChildTabs()`, `Tab.asDocumentTab().getBody()`, and `getActiveTab()`/`setActiveTab()` for bound scripts ([Apps Script tabs guide](https://developers.google.com/apps-script/guides/docs/tabs), updated 2026-09-03). A script can walk each tab's body, read `Paragraph.getHeading()`, and write per-tab Markdown or JSON to Drive, with no OAuth app to maintain. See [apps-script-tab-export.md](apps-script-tab-export.md).

## Options for adapt-rfp M0

| Route | Tab ids | Heading styles | Comments | Effort | Inspectable |
|---|---|---|---|---|---|
| A. Docs API JSON (`includeTabsContent`) → our converter → Markdown per tab | yes | yes (`namedStyleType`) | via Drive API | medium (write the walker) | high: raw JSON is archived |
| B. Drive export DOCX (all tabs) → pandoc | lost; `Title` paragraphs as proxy | yes | yes (`--track-changes=all`) | low | high |
| C. `export?format=html&tab=` per tab → pandoc | yes | via CSS classes | no | low, but **undocumented** | medium |
| D. Apps Script exporter → Markdown/JSON in Drive | yes | yes | no | low to medium | medium (script lives in Google) |
| E. Drive `text/markdown` export | no | yes | no | lowest | high, but tabs merge or drop |

**Recommendation:** start the pilot with **B**, since the DOCX files already exist. Build **A** once Drive access is set up. Archive the raw Docs JSON next to the Markdown so that tab ids, heading ids and revision ids become part of the manifest locator (`source: gdoc:{docId}#tab={tabId}&heading={headingId}`). This gives the most inspectable lineage and survives renamed tabs. Test B against A on one document to settle the Title-paragraph question.

Up: [index.md](index.md)
