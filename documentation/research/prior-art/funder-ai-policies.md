---
title: Funder AI policies and reviewer signals
slug: funder-ai-policies
level: 3
parent: proposal-management-practice.md
related: [color-team-review.md, grant-writing-ai-assistants.md, plain-language-guidelines.md]
tags: [policy, nih, nsf, foundations, ai-disclosure, distinctiveness]
status: draft
updated: 2026-09-25
kind: standard
verdict: adopt
fit: [M4, M5, M6, M7]
license: n/a
maturity: emerging
inspectability: high
sources:
  - title: NIH NOT-OD-25-132, Supporting Fairness and Originality in NIH Research Applications (2025-07-17)
    url: https://www.grants.nih.gov/grants/guide/notice-files/NOT-OD-25-132.html
    accessed: 2026-09-25
  - title: NSF, Notice to the research community on AI (2023-12-14)
    url: https://www.nsf.gov/news/notice-to-the-research-community-on-ai
    accessed: 2026-09-25
  - title: Candid, Will AI soon be reviewing your grant applications? (2025-11-20)
    url: https://candid.org/blogs/will-foundations-soon-use-ai-to-screen-grant-applications/
    accessed: 2026-09-25
  - title: "Phys.org on Qian & Wang, PNAS 2026, doi:10.1073/pnas.2601439123"
    url: https://phys.org/news/2026-08-ai-grant-narrowing-ideas.html
    accessed: 2026-09-25
  - title: Times Higher Education, Research funders 'flooded with AI-assisted applications' (2026-04-27)
    url: https://www.timeshighereducation.com/news/research-funders-flooded-ai-assisted-applications
    accessed: 2026-09-25
---

# Funder AI policies and reviewer signals

> **TL;DR** Funders now write rules about AI-assisted applications (NIH: "substantially developed by AI" is not original; NSF: disclosure encouraged, applicant responsible for accuracy). Evidence suggests AI-assisted proposals are **more uniform**. **Adopt** three responses: an AI-use rule field in every M5 solicitation model, a provenance-derived disclosure, and an M7 **distinctiveness** check.

## What the sources say

**NIH, NOT-OD-25-132 (2025-07-17).** "NIH will not consider applications that are either substantially developed by AI, or contain sections substantially developed by AI, to be original ideas of applicants." NIH "will continue to employ the latest technology in detection of AI-generated content". If AI use is found after award, the notice lists possible referral to the Office of Research Integrity and termination. The same notice caps applications at six per PI per year.

**NSF (2023-12-14).** "Proposers are encouraged to indicate in the project description the extent to which, if any, generative AI technology was used," and proposers "are responsible for the accuracy and authenticity" of AI-assisted content. Reviewers may not upload proposals to non-approved AI tools.

**Foundations (Candid 2025 Foundation Giving Forecast survey).** 1% of surveyed foundations use generative AI to screen applications, 19% are considering it, and 66% plan not to. Respondents stress human oversight.

**Uniformity evidence.** Qian & Wang (PNAS 2026, via Phys.org): NIH proposals with stronger LLM-writing signals received 4 percentage points more funding (as reported) but showed **lower semantic distinctiveness**. NSF showed no significant relationship. The Research on Research Institute (via THE, 2026-04-27) reports application volumes up 57% across 12 funders since 2022, with fewer low-quality applications. It says a link to AI is probable but not established.

**Practitioner claims (weaker evidence).** Grant-writing blogs say program officers flag text that is "generic, overly uniform in tone", with circular outcome language and the funder's own wording paraphrased back ([OpenGrants](https://opengrants.io/ai-for-grant-writing-2026-playbook/), [Professional Grant Writers](https://www.professionalgrantwriter.org/ai-in-grant-writing-what-funders-know-and-how-to-keep-your-proposal-human), accessed 2026-09-25). A widely repeated "62% of reviewers penalized…" statistic could not be traced to a primary source *(unverified; do not cite)*.

## Why it matters for adapt-rfp

- Our target funders (California LCI, CNRA) are not NIH, but federal pass-through money and agency leads may bring similar rules. The rule belongs in the solicitation model, not in our heads.
- adapt-rfp's design is the best defense: text assembled from **Hyphae's own curated prose**, with provenance, human edits, and facts, is demonstrably not "substantially developed by AI". The provenance map is also the evidence behind any disclosure.
- The uniformity finding is a quality risk even where AI is allowed. Reviewers reading dozens of similar applications reward specificity: named places, partners, numbers, and community voices.

## How it would fit

- **M5**: `ai_policy: {rule: prohibited|disclose|silent, text: "<verbatim>", source: …}` per solicitation.
- **M6**: generate an optional disclosure statement from the provenance map (share of sentences from library chunks vs. LLM adaptation vs. new human text). Never claim more human authorship than the log shows.
- **M7 distinctiveness check** (new):
  - *Funder echo*: n-gram and embedding overlap between the draft and the solicitation text. Flag sentences that restate funder language without adding a specific.
  - *Specificity density*: named entities, numbers, and places per 100 words (M4 NER), compared with the rubric's evidence expectations.
  - *Generic-phrase list*: watchwords plus humanizer AI-tells.
- **M7 red team**: include a persona prompt that asks "which sentences could appear in any applicant's proposal?"

## Weaknesses / risks

- Policies change fast (date-sensitive). Re-check them per solicitation.
- AI-detection accuracy is contested. Don't build an "AI detector". Build specificity and provenance.

## Verdict rationale

**Adopt**: modeling the policy costs little, and the distinctiveness check addresses a documented risk.

Up: [Proposal management practice](proposal-management-practice.md)
