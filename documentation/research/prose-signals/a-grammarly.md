---
title: Grammarly (Superhuman) APIs and Authorship
slug: a-grammarly
level: 3
parent: index.md
related: [commercial-apis.md, a-ai-detection-apis.md, ../provenance/index.md, ../provenance/crdt-attribution.md]
tags: [grammarly, writing-score, ai-detection, authorship, enterprise]
status: draft
updated: 2026-09-25
kind: service
verdict: hold
fit: [M4, M7]
license: proprietary
maturity: mature
inspectability: low
sources:
  - title: Grammarly API documentation, introduction (Analytics, License Management, Writing Score, AI Detection beta, Plagiarism beta)
    url: https://developer.grammarly.com/
    accessed: 2026-09-25
  - title: Grammarly, Writing Score API reference
    url: https://developer.grammarly.com/writing-score-api.html
    accessed: 2026-09-25
  - title: Grammarly, AI Detection API (Beta) reference
    url: https://developer.grammarly.com/ai-detection-api.html
    accessed: 2026-09-25
  - title: Grammarly Support, Receive OAuth 2.0 credentials (Enterprise and EDU admins; via search summary)
    url: https://support.grammarly.com/hc/en-us/articles/31625547341965-Receive-OAuth-2-0-credentials
    accessed: 2026-09-25
  - title: Grammarly, Custom APIs marketing page (Tone Analysis and Certified Readability Score "coming soon")
    url: https://www.grammarly.com/apis
    accessed: 2026-09-25
  - title: TechCrunch, Grammarly to shut down the Text Editor SDK in January (2023-07-13)
    url: https://techcrunch.com/2023/07/13/grammarly-to-shut-down-the-text-editor-sdk-in-january/
    accessed: 2026-09-25
  - title: TechCrunch, Grammarly rebrands to Superhuman (2025-10-29)
    url: https://techcrunch.com/2025/10/29/grammarly-rebrands-to-superhuman-launches-a-new-ai-assistant
    accessed: 2026-09-25
  - title: Superhuman, agent-specific attribution in Grammarly Authorship (2026-03-10, updated 2026-06-23)
    url: https://www.grammarly.com/blog/company/superhuman-authorship-docs/
    accessed: 2026-09-25
  - title: SiliconANGLE, Grammarly parent Superhuman buys AI detector GPTZero (2026-06-24)
    url: https://siliconangle.com/2026/06/24/grammarly-parent-superhuman-buys-ai-detector-gptzero/
    accessed: 2026-09-25
---

# Grammarly (Superhuman) APIs and Authorship

> **TL;DR** **Hold.** The Grammarly for Developers Text Editor SDK was **discontinued on 2024-01-10** and nothing has replaced it for developers. What exists in 2026 is a set of **Enterprise/EDU-admin REST APIs**. The Writing Score API returns four category scores plus an overall score, with **no span-level suggestions**. The AI Detection and Plagiarism APIs are in beta. That is too coarse for Claude to correct against, and Hyphae is too small for the gate. Authorship is the interesting part, as a *provenance precedent* rather than something we would integrate.

## Status (verified 2026-09-25)

- **SDK gone.** Grammarly announced in July 2023 that it would shut the Text Editor SDK on 2024-01-10, to refocus on its core product and AI features.
- **Corporate.** Grammarly Inc. rebranded to **Superhuman** in Oct 2025. The company now includes Grammarly, Coda and the Superhuman mail client. On 2026-06-24 it bought **GPTZero**, which it frames as an "authenticity layer" alongside its own detector.
- **APIs.** The developer portal lists Analytics, License Management, Writing Score, AI Detection (beta) and Plagiarism Detection (beta). The marketing page also lists Tone Analysis and "Certified Readability Score" as *coming soon*.
- **Access.** OAuth 2.0 client credentials are created in the Admin panel. Grammarly's support docs say these are available to admins with **Enterprise and EDU institution-wide licences**. Third-party pricing guides put Enterprise at roughly 150+ seats, quote-based *(unverified)*.

## Signal

| API | Returns | Granularity |
|---|---|---|
| Writing Score | `general_score`, `engagement`, `correctness`, `delivery`, `clarity`. The score starts at 100 and is reduced by weighted suggestions | Document |
| AI Detection (beta) | `average_confidence`, `ai_generated_percentage` | Document |
| Plagiarism (beta) | originality result | Document |

The ergonomics are asynchronous: POST a filename, get back `score_request_id` and a pre-signed upload URL, PUT the file within 120 s, then poll with GET. It accepts .doc/.docx/.odt/.txt/.rtf, ≤4 MB, ≤100k characters, and ≥30 words. **Retention:** the document is kept no longer than 24 h, and the score stays retrievable for 30 days. Rate limits for AI detection are 10 POST/s and 50 GET/s.

## Authorship (provenance angle)

Grammarly Authorship records which parts of a document were **typed, AI-generated or AI-edited**. Since March 2026 it also records *which agent* was used (e.g. Proofreader, Citation Finder). It runs in Grammarly Docs, Google Docs, Word and Canvas. It is a process-tracking model: it observes the editor, it does not infer from the text. That is the same bet as our DR-0008 span provenance, and it confirms that detection-after-the-fact is the weaker approach. We found **no Authorship API or export format** documented. Treat it as a precedent for [provenance](../provenance/index.md), not a dependency.

## How it would fit

At most, a document-level `L7.grammarly.writing_score` finding in an M7 report, if Hyphae ever had Enterprise. It cannot feed span-level correction.

## Strengths

- Recognisable, trusted score, and short retention of uploaded files.

## Weaknesses / risks

- No spans, no rule ids, opaque weighting, so it isn't inspectable.
- Enterprise-admin gate. Beta endpoints. The product direction follows Superhuman's agent strategy, not developers.

## Verdict rationale

Hold. Revisit only if the "Certified Readability Score" or Tone APIs ship with span output *and* self-serve access.

Parent: [Prose signals](index.md) · Comparison: [commercial-apis](commercial-apis.md)
