---
title: git blame and sentence content-hashing
slug: git-blame-and-hashing
level: 3
parent: index.md
related: [span-anchoring.md, precedents.md, fuzzy-anchoring.md]
tags: [git, blame, content-addressing, hashing, near-duplicate]
status: draft
updated: 2026-09-25
kind: technique
verdict: adopt
fit: [M1, M2, M7, M10]
license: GPL-2.0 (git)
maturity: mature
inspectability: high
sources:
  - title: git-blame documentation
    url: https://git-scm.com/docs/git-blame
    accessed: 2026-09-25
---

# git blame and sentence content-hashing

> **TL;DR** Git already records *who committed* each line, and `git blame -M -C -C -C` follows moved and copied lines across files. That is commit-level provenance for free, but it is line-granular and names the committer, not the author. A derived **sentence-hash index** (normalize, SHA-256 each sentence) adds cheap detection of verbatim reuse across chunks, drafts, and harvested docs. **Adopt both, as derived views**. Neither replaces declared authorship.

## What it is

- **git blame** annotates each line with the last commit that changed it. `-M` detects lines moved within a file. `-C` detects lines copied from other files in the same commit. `-C -C` adds the file-creating commit, and `-C -C -C` searches any commit. `--ignore-revs-file` skips reformatting commits. There is no word-level blame. `-w` only ignores whitespace.
- **Sentence content-addressing**: split into sentences, normalize (case, whitespace, quotes), hash. Identical hashes in two places mean verbatim reuse. This is the same idea as git blobs, applied at a finer grain.

## Why it matters for adapt-rfp

- Blame answers "who in the repo last touched this?", which is an audit trail that costs nothing.
- Hashes answer "where else does this exact sentence appear?", including the Fresno boilerplate reused in a Bay Point doc (DR-0002 context leakage). They also let the harvest step (M9) recognize our own sentences coming back from Google Docs.

## How it would fit

- **Write one sentence per line in `library/` chunks** (semantic line breaks). Then line-granular blame becomes sentence-granular. It is a cheap convention with a large payoff. Markdown renders the lines as one paragraph.
- Add a `.git-blame-ignore-revs` file for bulk reformatting commits.
- The derived index (M10) stores `sentence_sha → [(chunk, variant, line)]`. It is rebuilt, not committed. MinHash (M1) covers the near-duplicate cases that hashes miss.

## Strengths
- No new infrastructure. Fully inspectable. Survives forever in history.
- Hash lookups are exact and fast. They complement fuzzy anchoring.

## Weaknesses / risks
- The committer is often the person or agent who *pasted* the text, not its author. A partner's paragraph committed by Ivan blames Ivan, and an LLM-drafted paragraph blames whoever committed it. Declared `authors[]` stays necessary.
- One edited character changes the hash. Hashes only detect exact copies.
- One-sentence-per-line is a discipline that ingest (M0) and harvest (M9) must enforce automatically.

## Verdict rationale

Adopt. Git is already the canonical store (DR-0005), so this provenance comes free. Label it clearly as *custody* (who changed the file), distinct from *authorship*.

Up: [provenance index](index.md)
