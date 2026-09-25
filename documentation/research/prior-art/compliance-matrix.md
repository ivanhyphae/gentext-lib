---
title: Compliance matrix
slug: compliance-matrix
level: 3
parent: proposal-management-practice.md
related: [rfp-evaluation-matrix.md, color-team-review.md, visiblethread.md]
tags: [apmp, shipley, compliance-matrix, requirements, shred]
status: draft
updated: 2026-09-25
kind: technique
verdict: adopt
fit: [M5, M7, M8]
license: n/a (practice)
maturity: mature
inspectability: high
sources:
  - title: "Conniff, Shred for Success: The Value of a Compliance Matrix (APMP Western Regional Conference 2023)"
    url: https://apmp-western.org/wp-content/uploads/2023/10/WRC2023-Conniff-Shred-For-Success.pdf
    accessed: 2026-09-25
  - title: APMP Body of Knowledge, Compliance Matrix (members only; cited by Conniff, not read)
    url: https://apmp.helpjuice.com/create-deliverables/compliance-matrix
    accessed: 2026-09-25
  - title: GovEagle, Pink, Red, and Gold Team Reviews playbook
    url: https://www.goveagle.com/blog/pink-red-gold-team-reviews-playbook
    accessed: 2026-09-25
---

# Compliance matrix

> **TL;DR** The standard proposal-management artifact: shred the solicitation into **one row per requirement**, map each to where the response addresses it, and track status through every review. **Adopt** as M5's primary output, with rubric descriptors and "hidden requirements" treated as rows.

## What it is

APMP guidance, as summarized by Conniff (2023): a compliance matrix is "a checklist both for you and for evaluators", it "maps the requirements of the RFP down to the location in the response where the requirement is answered", and it doubles as the writers' plan of action. Build it before writing and keep it current.

## Practice rules (APMP BOK via Conniff)

1. One matrix for every bid, regardless of size or timeline.
2. **Shred line by line**. Every "shall", "must", "should", "will" gets its own row. "Resist the urge to save time by shredding… only by section or paragraph."
3. Follow the customer's numbering, even when it makes the narrative awkward.
4. Use the customer's words and start each item with the action verb.
5. Update it after amendments, Q&A responses, and outline changes.
6. **Hidden requirements**: some are "hidden in narrative explanations… including the evaluation criteria section".
7. Terms: shall = must (mandatory); should = expected goal; will = statement of fact. Ask the funder when usage is unclear.
8. Prep documents before automated shredding: strip headers and footers, and keep table titles with "SEE TABLE IN CUSTOMER DOCUMENT".

## Why it matters for adapt-rfp

DR-0003 already names a compliance matrix as an M5 output. The practice adds rigor:

- **Rubric bands are rows.** For EHCRP Appendix F, each High descriptor's evidence expectation (e.g., community quotes/stories) is a requirement with its own row, not a note on the question.
- **Non-narrative requirements are rows too**: budget % floors, eligibility, attachments, deadlines.
- **Status flows from QA.** Each color-team stage ([color-team review](color-team-review.md)) updates the `status` column.

## How it would fit

Proposed row schema (YAML in `solicitations/<funder>/<program>/<round>/matrix.yaml`):

```yaml
- id: EHCRP-R2-F.HR1.high.voices     # funder numbering + suffix
  source: {doc: guidelines, page: 0, lines: "0-0", quote: "…"}   # illustrative values; quote verbatim, checked
  kind: rubric-evidence              # shall | should | rubric-evidence | constraint | eligibility | attachment | deadline
  modal: must                        # must | should | will | n/a
  question: HR1
  points: null
  owner: ivan
  addressed_in: [draft:HR1#p2]       # filled by M6/M7
  status: gap                        # open | drafted | gap | pass | waived
  notes: ""
```

The `source.quote` field is enforced by a deterministic citation gate (see [rfp-evaluation-matrix](rfp-evaluation-matrix.md)). M8 skill: `compliance-matrix` renders it as a table for humans.

## Strengths

- Well-established. Reviewers and agency partners recognize it.
- Makes gaps visible and assignable; it is inspectable by construction.

## Weaknesses / risks

- Line-by-line shredding of a 17.6k-word NOFA produces many rows. LLM-assisted extraction needs a human check (DR-0003 already requires one).
- Federal FAR vocabulary (Section L/M) does not map one-to-one to state grant guidelines. Keep `kind` generic.

## Verdict rationale

**Adopt**: it is the canonical form of what M5 is meant to produce, and it costs nothing.

Up: [Proposal management practice](proposal-management-practice.md)
