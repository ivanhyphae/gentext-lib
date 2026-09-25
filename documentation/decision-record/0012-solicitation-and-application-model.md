# 0012. Solicitation model with explicit applications (permutations)

- Status: Accepted (2026-09-25, provisional: "ok for now, let's see how it goes")
- Date: 2026-09-25
- Deciders: Ivan Heitmann; Claude (drafting)

## Context
- DR-0003 M5 models a solicitation as questions + constraints. The maintainer: *when a solicitation comes along we are often working in parallel on multiple possible applications with different permutations of partners.* For EHCRP R2 there are two ARPD-led pre-applications (Ambrose Center Park, Ambrose Memorial Park), plus an exploratory I-ReLab track.
- The **actual form** can differ from the guidelines. The Full Application Form's Harm Reduction Q2 adds "expected harm reduction outcomes", which Appendix F doesn't have.
- The DR-0011 funnel needs a machine-readable **needs list** to score documents against.

## Decision (proposed)
```
solicitations/<funder>/<program>/<round>/
  solicitation.yaml     # deadlines, award ranges, tiers, eligibility, budget constraints, source asset ids
  questions.yaml        # per question: id, verbatim prompt (from the FORM; guideline variant noted), word limit,
                        #   points, rubric bands (verbatim), evidence expectations (extracted), tier applicability
  applications/
    <app-id>.yaml       # one per permutation: site, tier, lead applicant, co-applicants/partners, Hyphae role,
                        #   status (exploring | pre-app-submitted | full-app | submitted | awarded | declined),
                        #   links to working docs (inventory ids), per-question answer status
    <app-id>/answers/<question-id>.md   # drafts for this application (Claude Docs round-trips, DR-0007)
```
- **Questions belong to the solicitation. Answers belong to an application.** Shared text between applications is expressed as library chunks with `adapted-for: <app-id>` lineage, not copy-paste.
- Every question and rubric line cites its source asset and page (`ehcrp-r2-full-application-form`, `ehcrp-r2-guidelines` Appendix F). Where they differ, **the form wins**, and the difference is recorded.
- **Evidence expectations** are extracted once (LLM-assisted, then human-verified) from rubric bands and TA guides. Examples: "community quotes/stories", "measurable harm-reduction metrics with who/how/when", "named partner track record". They drive M7 rubric-coverage checks and DR-0011 relevance scoring.
- First instance: `solicitations/lci/ehcrp/round-2/`, with applications `ambrose-memorial-park` and `ambrose-center-park` (ARPD-led) and `irelab-exploratory` (status `exploring`).

## Consequences
- Checks and drafts are per application: word limits and rubric are shared, site facts and partners differ.
- A cross-application view shows which answers diverge, and where site-specific facts leak into the wrong application. That's context leakage within one solicitation.

## Open questions
- Should the workbook (workplan/budget) constraints be modelled in the pilot, or narrative questions only? Lean: narrative only until after Oct 13.

## Revisions
- 2026-09-25: Accepted provisionally by the maintainer; revisit after the EHCRP application.
- 2026-09-25 (maintainer): guidelines and scoring criteria often live **outside the primary solicitation document** and must still be part of the model. Added:
  - A **`standards:`** list in `solicitation.yaml`: every document that sets the bar (form, FAQ clarifications, guidelines and appendices, checklist, external criteria such as the Meaningful and Direct Benefits Assessment, external tools such as VCP, TA/reviewer guides), each with a `role` and a `precedence` for resolving conflicts. The lower number wins; if equal, the newer document wins. Superseded drafts are listed but never cited.
  - **`requirements.yaml`** for requirements not tied to a narrative question (priority-point criteria, budget shares, Belonging timing, TA-guide expectations), each citing its standard, the questions it applies to, and how M7 can check it.
  - The rule that **standards are not content**. They are never mined for reusable prose; they define what M7 checks against. Prior-round documents are context, not standards.
- 2026-09-25: First instance created: `solicitations/lci/ehcrp/round-2/` with `solicitation.yaml`, `questions.yaml` (verbatim from the Full Application Form, with `guideline_diff` noted for overview and hr-q2), and three applications. Evidence expectations are `status: draft` pending human review.
