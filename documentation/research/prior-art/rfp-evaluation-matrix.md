---
title: rfp-evaluation-matrix (open source)
slug: rfp-evaluation-matrix
level: 3
parent: proposal-management-practice.md
related: [compliance-matrix.md, ../provenance/index.md]
tags: [open-source, claude, compliance-matrix, citation-gate, python]
status: draft
updated: 2026-09-25
kind: library
verdict: trial
fit: [M5, M7]
license: MIT
maturity: experimental
inspectability: high
sources:
  - title: eugeniawang/rfp-evaluation-matrix (GitHub)
    url: https://github.com/eugeniawang/rfp-evaluation-matrix
    accessed: 2026-09-25
  - title: GitHub topic rfp-automation
    url: https://github.com/topics/rfp-automation
    accessed: 2026-09-25
---

# rfp-evaluation-matrix (open source)

> **TL;DR** A tiny MIT-licensed Claude project that turns a public-sector RFP into a 12-column evaluation matrix in which **every cell is cited to page and line**, and a **stdlib checker refuses the matrix** if any cited text or number is not literally in the source. It is too young to depend on (3 commits, 0 stars), but the **citation-gate pattern** is the best open-source idea found. **Trial** the pattern in M5.

## What it is

A Claude project folder with Python utilities (`extract.py`, `check_matrix.py`, `write_matrix.py`). Claude reads the RFP and fills a fixed schema. Code then verifies it.

Columns: `#` · RFP section · RFP criterion · Points · Input needed · Input data source · Evaluation criteria · Proposal section · Owner · Claude does · Human check · Status. Six come from the RFP with page-line citations. Three are left blank for the firm's own knowledge.

## The citation gate

From the README: text must match **whole words from the cited lines on a single page**, numbers must appear on the cited lines, every key must fit the schema, and **point totals must reconcile**. The checker rejects paraphrases, respellings, invented figures, wrong citations, and totals that don't add up, and tests show it refuses malformed matrices before rendering.

## Why it matters for adapt-rfp

- It is the same "LLM proposes, deterministic code disposes" split as DR-0003, applied to M5 extraction.
- It defends against the one failure an LLM-extracted requirements model must never have: a requirement or point value that isn't in the solicitation.
- Columns like "Claude does" and "Human check" make the human/AI division of labor explicit per row. That is a nice inspectability touch for the M5 matrix and for M8 skill output.

## How it would fit

- M5: after LLM extraction from `pdftotext -layout` output (page-aware), run a `verify-solicitation` check. Each `source.quote` must be a whole-word substring of the cited page/lines, and each `points` value must appear there. Rubric points per question must sum to the published total.
- M7: the same gate for *fact* citations in drafts. A number in a draft must literally appear in its cited M3 fact or source locator.
- Borrow the pattern and write our own ~100 lines rather than depend on the repo.

## Strengths

- Small, readable, stdlib-only verifier; highly inspectable.
- Tests that prove refusal behavior.

## Weaknesses / risks

- Experimental: 3 commits, no stars or forks, single author (as of 2026-09-25). Maintenance status unknown.
- Literal matching is brittle on PDF extraction artifacts (hyphenation, ligatures, line wraps). Normalize whitespace and hyphenation before matching.
- Covers evaluation criteria only, not budgets or eligibility.

## Context: the rest of open source

The GitHub `rfp-automation` topic lists 19 repos (0–8 stars), mostly RAG answer bots for sales and security questionnaires, and the curated `ai-for-grant-writing` list (~4.2k stars) is prompts and links. No open-source project offers a governed proposal content library. *Build* is the only option for the core.

## Verdict rationale

**Trial**: implement the gate in the pilot's M5 slice (EHCRP Appendix F) and see how many LLM extraction errors it catches.

Up: [Proposal management practice](proposal-management-practice.md)
