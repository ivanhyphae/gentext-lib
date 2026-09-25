---
title: Grant-writing AI assistants
slug: grant-writing-ai-assistants
level: 3
parent: content-library-governance.md
related: [funder-ai-policies.md, ai-native-rfp-tools.md, color-team-review.md]
tags: [grant-ai, saas, funder-discovery, drafting, mock-review]
status: draft
updated: 2026-09-25
kind: product
verdict: hold
fit: [M5, M6, M7]
license: proprietary SaaS
maturity: emerging
inspectability: low
sources:
  - title: Instrumentl, Apply capability page
    url: https://www.instrumentl.com/capability/apply
    accessed: 2026-09-25
  - title: Instrumentl Help Center, Apply + Advisor (search summary)
    url: https://help.instrumentl.com/en/articles/9903781-instrumentl-apply-ai-powered-grant-applications
    accessed: 2026-09-25
  - title: Grantable home page
    url: https://grantable.co/
    accessed: 2026-09-25
  - title: Granted AI home page
    url: https://grantedai.com/
    accessed: 2026-09-25
  - title: Grantboost home page (search summary)
    url: https://www.grantboost.io/
    accessed: 2026-09-25
  - title: OpenGrants, AI for Grant Writing in 2026 playbook (search summary)
    url: https://opengrants.io/ai-for-grant-writing-2026-playbook/
    accessed: 2026-09-25
  - title: Candid blog, Candid search launch (search summary)
    url: https://candid.org/blogs/candid-search-fully-launched-new-features-help-funders-fundraisers-work-smarter/
    accessed: 2026-09-25
  - title: eseckel/ai-for-grant-writing (curated list, ~4.2k stars)
    url: https://github.com/eseckel/ai-for-grant-writing
    accessed: 2026-09-25
---

# Grant-writing AI assistants

> **TL;DR** Grant-specific AI tools (Instrumentl Apply, Grantable, Grantboost, Granted AI, OpenGrants, Fundwriter, Candid's AI features) are strong at **funder discovery** and **RFP-to-outline**, and some offer **mock review**. None publish a fact registry, provenance, or content governance. Their "org memory" is RAG over past proposals, which reproduces generic prose and stale facts. **Hold** as a core. Borrow the RFP-outline and multi-perspective review ideas.

## Who does what (vendor claims, 2026-09-25)

| Tool | Main strengths (claimed) | Pricing (public) |
|---|---|---|
| **Instrumentl Apply + Advisor** | Upload an RFP → priorities, eligibility, attachments, narrative expectations; "Smart Section Builder" outline; drafts from your past proposals; suggestions from 990 funder data | Higher plans only *(unverified tiers)* |
| **Grantable** | "Library that never forgets" of proposals and data; 990 funder search and fit scoring; inline suggestions "before reviewers do"; "AI drafts, humans decide" | Free / $50 / $150 per month |
| **Granted AI** | Grant database (claims 85k+ grants); "Granted Review Board": independent multi-perspective critique, deliberation, consensus | From $29/month |
| **Grantboost** | Drafts that "sound like your team" from past proposals | *(unverified)* |
| **OpenGrants** | Grant database; RFP analysis extracting mandatory requirements, rubrics, eligibility; access to human grant writers | *(unverified)* |
| **Fundwriter.ai** | Templates for LOIs, introductions, one-page proposals | *(unverified)* |
| **Candid (Foundation Directory)** | Funder data and natural-language search; AI-drafted LOIs "to fact-check carefully" | Subscription |

Most comparison articles are published by these vendors (Granted, Grantable, Grantboost each rank themselves first). Treat rankings as marketing.

## What they do well

- **Solicitation → structured outline.** Instrumentl and OpenGrants both advertise requirement, rubric, and eligibility extraction, which is our M5. That confirms the need but not the quality.
- **Voice from past work.** Retrieval from your own proposals, not generic text, is the common pitch against "sounding like AI".
- **Mock review.** Granted's multi-reviewer "board" with deliberation is the closest commercial analogue to our red-team pass. Community prompt lists (e.g., `ai-for-grant-writing`) include reviewer-concern prompts.

## Where they're weak

- **No auditable provenance.** No public tool maps sentences to sources or keeps a fact registry with validity dates. Candid tells users to fact-check AI-drafted LOIs, which puts verification on the writer.
- **Generic prose risk.** A 2026 PNAS study found LLM-signal NIH proposals less semantically distinctive (see [funder AI policies](funder-ai-policies.md)). Tools that optimize for "funder alignment" by echoing funder language make this worse.
- **Context leakage and staleness.** Undifferentiated past-proposal memory will happily reuse "for Fresno County" text or old statistics.
- **Partner/contractor role not modeled.** These tools assume the nonprofit applicant is the author. Hyphae writes as partner or contractor, in several voices (DR-0002 §9).
- **Confidentiality.** Uploading partner-authored and pre-decisional material to a third-party store conflicts with DR-0004.

## How it would fit

- Not in the core. Optional, outside adapt-rfp: Instrumentl or Candid for *finding* opportunities.
- **Borrow**: an Instrumentl-style section builder as the output of M5 (`outline` generated from the compliance matrix); a Granted-style multi-persona red team in M7 (e.g., "program officer", "community reviewer", "technical reviewer"), each scoring independently before reconciliation.

## Verdict rationale

**Hold**: low inspectability, no provenance, confidentiality risk, and a nonprofit-applicant framing that doesn't fit a partner firm. The feature list is still a useful checklist of what users expect.

Up: [Content library governance](content-library-governance.md)
