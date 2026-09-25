# 0002. Pilot case: EHCRP Round 2 (Bay Point)

- Status: Accepted (2026-09-25)
- Date: 2026-09-25
- Deciders: Ivan Heitmann; Claude (drafting)

## Context

### What the pilot contains (`projects/EHCRP Round 2/`)

| File | Nature |
|---|---|
| `Round-2-Final-Guidelines.pdf` | The solicitation. ~17.6k words. Program values, two project tiers (Early $0.75–1.2M/30 mo; Advanced $3–4.5M/48 mo), budget floors, eligibility and co-applicant rules, funding-priority points, and **Appendix F scoring criteria**: narrative questions with word limits (300/250/350), point values, and High/Medium/Low rubric descriptors. |
| `Round-2-Pre-Application-Interest-Form.pdf` | Pre-app form questions (a second, smaller solicitation instrument). |
| `Ambrose Memorial Park EHCRP.docx` / `Ambrose Center Park EHCRP.docx` | **Two separate pre-applications, one per site**, written by the lead writer (James) with Ambrose Recreation and Park District (ARPD) as lead applicant. They share most of their content (~15k words each) and differ in the site-specific pre-app answers. They also contain background notes, webinar notes, outreach templates, firm boilerplate, and draft answers. *(Corrected 2026-09-25; see Revisions.)* |
| `2026 URBAN GREENING GRANT PROGRAM CONCEPT PROPOSAL.docx` | A *different* funder's form (CNRA Urban Greening), same community (Bay Point), lead CCRCD. Transit-stop greening + workforce pathways. Checkbox eligibility and long-form answers. |

### What the pilot teaches us

1. **Sources are messy working documents, not finished proposals.** Reusable prose sits next to meeting notes, action items, contact details, and brainstorms. Ingest must segment and classify. It cannot treat a file as one unit.
2. **One solicitation, several parallel applications.** The team often pursues several *permutations* at once: different sites, leads, and partner sets. Here that means Ambrose Center Park and Ambrose Memorial Park (ARPD-led), plus a separate exploratory track with I-ReLab. Shared text is copied across applications and then specialised per site. We need near-duplicate detection, chunk-level lineage (`variant-of`, `shortened-from`, `adapted-for`), and an explicit **application** entity between the solicitation and its answers (DR-0012).
3. **Chunks come in length variants.** The pilot has long and "SHORTENED" versions of Modeling, Monitoring, Community Engagement, Design, and Planting & Stewardship. Word limits (250/300/350) make length-targeted variants a core feature.
4. **Recognizable chunk types** already appear: firm experience / project case (Prescott, Stockton AB 617, LA Depave, Oakland STEP, SW Medical District, AdaptOS, Green Heart), technical capability, local knowledge / network, site description, need statement with data citations, method paragraph, partner-role description, outreach template.
5. **Facts carry provenance, and they repeat.** Census tracts (06013313203, 06013314105), CHAT scores (3.55; 45.41), "21–35 days over 100°F by the 2090s", CCHS 2015 report p.32, Green Heart "13–20% lower hsCRP", dollar amounts ($4,217,818). A fact registry with sources would let QA check every reuse.
6. **Real QC defects exist today:**
   - Acronym collision: UTCI is written as "Universal Thermal Climate Index" in one place and "Urban Thermal Comfort Index" in others.
   - Name errors: "Caribbean South America Hispanic Council/Counsel", "Resource(s) Conservation District".
   - Context leakage: the Local Knowledge boilerplate ends "…positions the firm as a leader… for Fresno County" inside a Bay Point document.
   - Grammar: "one of the primary recreational facility".
   - Unhedged boosters funders may discount: "unprecedented precision", "cutting-edge".
7. **The solicitation is machine-checkable.** Each narrative question has id, prompt, word limit, points, and three rubric bands. Program requirements include budget percentage floors (e.g., Early: demo 25–60%, partners ≥8%, Belonging ≥4%, $25k post-award, indirect ≤15%). Rubric language names evidence types reviewers want, e.g. Harm Reduction Q1 "High" requires *community voices… quotes or stories*. The current drafts contain none, and a gap check would flag that.
8. **Content crosses funders.** Bay Point context, partners (ARPD, CCRCD, Bay Point Garden Club, SOS Richmond), and methods feed both EHCRP and Urban Greening. The library must be funder-neutral, and the solicitation model funder-specific.
9. **Multiple voices and authors.** Firm (Hyphae), partner (I-ReLab / Dr. kj), and lead agency (CCRCD/ARPD) voices are mixed. Chunks need `voice`/`perspective` and `owner` metadata. Some content is the partner's to reuse, not ours.
10. **Sensitivity is uneven.** The files contain emails, phone numbers, internal candid assessments of partners, and pre-decisional strategy. See DR-0004.

## Decision
Use EHCRP Round 2 as the pilot and design fixture. Its success criterion is a vertical slice:

> Ingest the pilot sources → segment and classify into library chunks (firm experience, Bay Point context, methods) → model Appendix F as a requirements set → assemble draft answers for the **Harm Reduction** section, Q1 *Extreme heat in your community* and Q2 *How will this project help?* (250 words each, 12 points together) with provenance → run QA that reports word count, rubric-evidence gaps, glossary/acronym consistency, fact provenance, and context leakage.

The QC defects listed above become the first regression tests: the QA module must catch each of them.

## Consequences
- The full application deadline (2026-10-13) is real, and the slice is meant to **help the actual submission** as a shadow contribution (DR-0007). Output must be paste-ready and must never block the lead writer's process.
- Designing from one funder risks overfitting. The Urban Greening concept proposal is the built-in second case to test funder-neutrality.

## Alternatives considered
- Start from a clean, finished past proposal: easier to parse, but it hides the real mess (forks, notes, variants) the system must handle.

## Why Harm Reduction first
- It uses the content the pilot has most of, and most messily: Bay Point site context, need statements, and cited data (CCHS 2015, Cal-Adapt, CHAT, census tracts). The fact registry and provenance get exercised immediately.
- Its rubric names a gap the drafts actually have. "High" requires *community voices… quotes or stories* and data integrated with lived experience. QA finding that gap is real, actionable help for the lead writer.
- Q2 depends on Q1 (pathways from infrastructure to the harms named in Q1), which tests cross-answer consistency.
- Next candidate: **Partnership Q2** (*partnership readiness*), which leans on firm-experience boilerplate and tests library reuse and context-leakage checks.

## Open questions
- Do other past proposals (the "Past Proposals" heading in the working doc is empty) exist to widen the corpus early?

## Revisions
- 2026-09-25 (maintainer correction): The two Ambrose DOCX files are **not a fork of the I-ReLab working doc**. They are the lead writer's two successfully submitted pre-applications, one per site, prepared with ARPD (Lori). The Drive doc "Hyphae + I-ReLab EHCRP" is a separate, earlier exploratory track. If I-ReLab takes part, it will assist the ARPD applications. The maintainer can supply the Google Doc links for the two ARPD applications.
- 2026-09-25: Accepted. The maintainer confirmed that this is real help for the live application, and that the agent chooses the pilot topic. Target set to Harm Reduction Q1+Q2.
