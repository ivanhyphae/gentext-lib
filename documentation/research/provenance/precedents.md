---
title: "Precedents: WikiWho and proposal content libraries"
slug: precedents
level: 3
parent: index.md
related: [git-blame-and-hashing.md, schema.md]
tags: [precedent, wikipedia, rfp-software, loopio, authorship]
status: draft
updated: 2026-09-25
kind: product
verdict: assess
fit: [M2, M9]
license: WikiWho MIT (unverified); Loopio/Responsive proprietary
maturity: mature
inspectability: medium
sources:
  - title: "WikiWho: Precise and Efficient Attribution of Authorship of Revisioned Content (WWW 2014)"
    url: https://archives.iw3c2.org/www2014/proceedings/proceedings/p843.pdf
    accessed: 2026-09-25
  - title: wikiwho/WikiWho (GitHub)
    url: https://github.com/wikiwho/WikiWho
    accessed: 2026-09-25
  - title: "TokTrack: token provenance dataset for English Wikipedia (arXiv 1703.08244)"
    url: https://arxiv.org/pdf/1703.08244
    accessed: 2026-09-25
  - title: "Loopio Help: Stacks, Categories, Sub-Categories, and Tags"
    url: https://support.loopio.com/hc/en-us/articles/360020729493-How-Can-I-Structure-My-Library-Content-Stacks-Categories-Sub-Categories-and-Tags
    accessed: 2026-09-25
  - title: "Loopio Help: Library Health report (entry owner, review cycle status)"
    url: https://support.loopio.com/hc/en-us/articles/53779616055955-How-Can-I-Report-on-My-Library-Health
    accessed: 2026-09-25
---

# Precedents: WikiWho and proposal content libraries

> **TL;DR** Two reference points bracket our design. **WikiWho** proves that token-level authorship over a full revision history is computable (reported at >95% accuracy on English Wikipedia), but only when *every* revision is captured, which ours are not. **RFP content libraries** like Loopio track provenance at the *entry* level (owner, reviewer, review cycle, tags) and do no span-level authorship. Our layered scheme sits between them: entry-level by default, spans by exception. **Assess** both as inspiration, not as dependencies.

## WikiWho (Flöck & Acosta, WWW 2014)

- **What:** an algorithm that tracks the origin revision of each token (≈ word) across all revisions of a wiki page, including deletions and *reinsertions*. It splits text into paragraphs, then sentences, then tokens, and matches unchanged units by hash before diffing the rest. The repo reports ">95% accuracy for EN.Wikipedia". The paper reports higher precision than earlier approaches. **TokTrack** is a released dataset of this provenance for English Wikipedia. Wikimedia hosts a `wikiwho_api` service, and WhoColor visualizes authorship by colour.
- **Lesson for adapt-rfp:** the hierarchical *hash-then-diff* approach (paragraph → sentence → token) is exactly what our harvest step should do ([git blame and hashing](git-blame-and-hashing.md)). Token-level authorship depends on an unbroken chain of revisions with known editors. Our Google Docs paste breaks that chain, so declared provenance must fill the gap.

## Proposal content libraries (Loopio, Responsive)

- **What (Loopio, from its help centre):** library *entries* are Q&A pairs organized by Stacks (with access control), Categories, Sub-Categories, and Tags. Each entry has an **Entry Owner** and **Review Cycles**, and reports show review status (completed, in progress, overdue, none). Responsive (formerly RFPIO) offers comparable library moderation and review features *(not verified in this pass)*.
- **What they don't do:** no publicly documented sub-entry (sentence-level) authorship or partner-attribution *(unverified; absence is hard to prove)*. Provenance is effectively "who owns and last reviewed this entry".
- **Lesson for adapt-rfp:** entry-level **owner + review cadence + tags** is the commercial baseline. Our frontmatter should match it (`owner`, `review.status/by/on`). Span provenance and AI generation records are where we would go beyond the commercial tools.

## Legal clause libraries

Contract-drafting teams keep clause libraries with approved fallback variants, owners, and "approved by legal" status. That is analogous to our length variants and review status. No primary source was checked in this pass *(unverified)*.

## Verdict rationale

Assess. Adopt the *patterns* (hierarchical hashing from WikiWho, owner and review cycles from Loopio). Take on neither as a dependency.

Up: [provenance index](index.md)
