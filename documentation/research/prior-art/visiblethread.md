---
title: VisibleThread
slug: visiblethread
level: 3
parent: proposal-management-practice.md
related: [compliance-matrix.md, plain-language-guidelines.md]
tags: [proposal-qa, acronyms, readability, shred, govcon]
status: draft
updated: 2026-09-25
kind: product
verdict: hold
fit: [M4, M5, M7]
license: proprietary (SaaS and on-premise)
maturity: mature
inspectability: medium
sources:
  - title: VisibleThread, Acronym Check
    url: https://www.visiblethread.com/acronym-checks/
    accessed: 2026-09-25
  - title: VisibleThread Docs 2.12 release note (search summary)
    url: https://www.visiblethread.com/news/visiblethread-docs-2-12-now-available/
    accessed: 2026-09-25
  - title: "Conniff, Shred for Success (APMP Western 2023): tools slide"
    url: https://apmp-western.org/wp-content/uploads/2023/10/WRC2023-Conniff-Shred-For-Success.pdf
    accessed: 2026-09-25
---

# VisibleThread

> **TL;DR** A GovCon proposal QA suite: RFP shredding into compliance matrices, **acronym checks**, readability/grade level, and "watchword" lists. **Hold** as a product. **Borrow** its acronym-check taxonomy and watchword idea into M7, where they are small deterministic functions.

## What it is

Commercial software (browser-based and on-premise, per APMP Western's tool review) used by federal proposal teams. The same workspace covers "shred, compliance matrix, writing, readability and watchword checks".

## The acronym check (the part we want)

VisibleThread's page lists four failure types:

1. **Undefined** acronyms.
2. **Conflicting definitions** (same acronym, different expansions).
3. **Used before defined.**
4. **Repeated definitions.**

Output is an annotated Word or Excel file flagging each occurrence. The vendor claims "100% accuracy" *(unverified marketing)*.

The pilot's UTCI defect ("Universal Thermal Climate Index" vs "Urban Thermal Comfort Index") is type 2. Checking against the M3 glossary adds a fifth type: **non-canonical expansion** (defined consistently, but not the glossary form).

## Other checks

- Readability metrics and a per-document "Grade Level" score (v2.12).
- **Watchwords**: user-defined term lists to flag, such as banned phrases, competitor names, or weak words. For adapt-rfp: boosters ("unprecedented", "cutting-edge"), AI-tells, and *other clients' place names* (leakage).

## Why it matters for adapt-rfp

It shows that a proposal-QA product is mostly a set of plain, explainable, deterministic checks, not AI. That supports DR-0003's "deterministic checks first" rule.

## How it would fit

- M7 `acronyms` check: regex candidate extraction (`\b[A-Z]{2,}s?\b`) + definition-pattern detection ("Full Name (ABC)") + glossary lookup, reporting the five types with locations.
- M7 `watchwords` check: YAML lists in the repo (`library/glossary/watchwords.yaml`) with categories and suggested fixes. It can share rules with a Vale style if the style-lint research adopts Vale.
- M4: readability via textstat, already planned.

## Strengths

- Clear, testable check definitions.
- Proven in federal proposal workflows.

## Weaknesses / risks

- Enterprise product and pricing *(pricing not public)*.
- Word/Excel-centric output; not git- or Markdown-native.
- No model of funder rubrics, facts, or provenance.

## Verdict rationale

**Hold** as a purchase: the checks we need are small to build and test against the DR-0002 regression cases. The taxonomy itself is worth adopting as-is.

Up: [Proposal management practice](proposal-management-practice.md)
