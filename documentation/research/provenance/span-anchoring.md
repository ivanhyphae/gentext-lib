---
title: Span anchoring across edits and round-trips
slug: span-anchoring
level: 2
parent: index.md
related: [schema.md, web-annotation-selectors.md, fuzzy-anchoring.md, inline-markup.md, crdt-attribution.md, git-blame-and-hashing.md]
tags: [provenance, anchoring, standoff, round-trip, google-docs, claude-docs]
status: draft
updated: 2026-09-25
---

# Span anchoring across edits and round-trips

> **TL;DR** Anchor span provenance *outside* the text (standoff) with a W3C TextQuoteSelector (`exact` + `prefix` + `suffix`) plus a character-offset hint. Re-anchor after every edit with a three-step cascade: exact match, then position-guided fuzzy match (diff-match-patch / Bitap), then orphan. For Google Docs round-trips, anchor against the *diff* between what we pushed and what came back, not against the Docs editor's history. Inline markup survives neither paste nor prose editing, so keep it out of canonical files.

## Options compared

| Approach | Survives our edits? | Survives Docs paste? | Readable in git diff? | Cost |
|---|---|---|---|---|
| Inline Pandoc spans `[…]{by=org:i-relab}` | Yes, while editors leave the brackets alone | **No.** Stripped or mangled | Noisy | Low tooling, high clutter |
| CriticMarkup `{++ ++}{>> <<}` | Only as a *pending* change | **No** | Good for review | Low |
| Footnote-style markers `[^p1]` | Mostly | Partly, as literal text | OK | Clutters funder-facing copy |
| Offsets only (brat, TextPositionSelector) | **No.** Every edit shifts them | No | Clean text, opaque sidecar | Low |
| **Quote + context + offset hint (W3C)** | Yes, through small to moderate edits | Yes, re-anchored on harvest | Clean text, readable sidecar | Medium (one re-anchor tool) |
| CRDT attribution (Yjs v14, Automerge) | Yes, per character | No. Lost at export | Binary | High. Needs an editor we don't run |
| Sentence hashes | Exact copies only | Exact copies only | Opaque | Low. Good for *detection*, not anchoring |

Sources: [Web Annotation Data Model §4.2.4–4.2.5](https://www.w3.org/TR/annotation-model/), [brat standoff](https://brat.nlplab.org/standoff.html), [Pandoc manual](https://pandoc.org/MANUAL.html), [CriticMarkup](https://fletcher.github.io/MultiMarkdown-6/syntax/critic.html), all accessed 2026-09-25.

The W3C spec itself calls position selectors "very brittle with regards to changes to the resource". That is why the quote is primary and the offset is only a hint.

## The re-anchor cascade (`adapt-rfp prov check`)

Run it on each commit (pre-commit hook or CI) and at every harvest:

1. **Normalize** both texts: NFC, collapse whitespace, strip Markdown emphasis, straighten quotes. The W3C model requires selectors to be computed on normalized text. Store the normalization version in the sidecar.
2. **Exact:** find `prefix+exact+suffix`, then `exact` alone. A unique hit sets `status: anchored` and refreshes the offset hint.
3. **Fuzzy:** search near the old offset for `exact` with a Bitap/Myers approximate match (diff-match-patch `match_main`, or rapidfuzz). Confirm with fuzzy prefix and suffix, as Hypothes.is does. If the score is at or above the threshold (proposed 0.85), set `status: fuzzy`, rewrite `exact` to the new text, and keep the old text in `was:`.
4. **Orphan:** otherwise set `status: orphaned` and fail the check. A human re-attaches the span, splits it, or deletes it.

Rule: **re-anchoring may move a span, but it never changes the span's authors.** If the matched text changed materially (similarity below 1.0), the tool appends `edited: {by: <commit author or unknown>, at_commit: …}`. Authorship accretes. It is never overwritten.

## Round-trip through Claude Docs and Google Docs (M9)

What we control: push, then harvest. What we don't control: what happens in between.

```
library chunk@commit A ──push──► Claude Docs ──(manual paste)──► Google Docs ──(export)──► harvest
       │                                                                              │
       └──────── three-way compare: A (pushed text)  vs  returned text ───────────────┘
```

- At **push**, record `pushed: {doc: <url-or-id>, at_commit: A, sha256: …}` in a harvest ledger.
- At **harvest**, diff the pushed text against the returned text with diff-match-patch, sentence by sentence. Unchanged sentences keep all span provenance. Changed sentences get `edited-in: <doc>`, `editor: unknown` until a human declares otherwise. The harvest skill should ask "who edited this?" and suggest names only if the Docs revision list shows a single editor.
- Google Docs keeps suggestion authors and revision history inside the product. The public Docs API shows suggestions and (in Developer Preview) can accept or create them, but plain copy-paste and export drop all of it. Don't design around that data. Treat it as optional evidence. Source: [Google Docs API, work with suggestions](https://developers.google.com/workspace/docs/api/how-tos/suggestions), accessed 2026-09-25.
- Claude Docs round-trip specifics (comment or authorship export) are *(unverified)*. Assume text only.

## Granularity: what to anchor

- **Sentence** is the default span. Sentences are stable enough to re-anchor, and they match how people copy text.
- **Clause or phrase** only for fact assertions (numbers, names), where the `exact` string *is* the fact and a mismatch is a QA signal in itself.
- **Paragraph or chunk** means no span at all. That level belongs in frontmatter.

## Failure modes to expect

- **Merged or split sentences.** One span matches half of a new sentence, or two spans overlap. The tool reports this and never auto-merges authors.
- **Repeated boilerplate.** The same `exact` string appears twice in a chunk. Prefix/suffix and the offset hint break the tie. If they can't, the span is ambiguous and a human must resolve it.
- **Length variants.** Anchors are per variant file. A shortened variant starts with an empty sidecar, and `derived_from` carries the lineage. Optionally, the tool proposes spans by fuzzy-matching the parent variant's spans, as suggestions only.
- **Silent decay.** If nobody fixes orphans, the sidecar becomes wrong. CI failure is the forcing function. The alternative is deleting the sidecar and falling back to chunk-level provenance, which is honest.

## Verdict

Adopt standoff W3C-style selectors with a small Python re-anchor tool (diff-match-patch + stdlib `unicodedata`). Build it after the chunk-level schema has proven useful in the pilot, not before.

Up: [provenance index](index.md)
