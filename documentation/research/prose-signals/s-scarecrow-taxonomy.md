---
title: Span-level error taxonomies (Scarecrow, FRANK, MQM)
slug: s-scarecrow-taxonomy
level: 3
parent: index.md
related: [span-feedback-schema.md, s-llm-span-annotation.md, s-slop-measurement.md, s-edit-based-rewards-lamp.md, ../llm-evaluation/claim-verification.md]
tags: [taxonomy, span-annotation, error-typology, mqm, severity, factuality]
status: draft
updated: 2026-09-25
kind: standard
verdict: adopt
fit: [M7]
license: papers open access; Scarecrow repo license not found; FRANK repo (license unverified); MQM framework CC BY 4.0 (unverified)
maturity: mature
inspectability: high
sources:
  - title: Dou et al. Is GPT-3 Text Indistinguishable from Human Text? Scarecrow, A Framework for Scrutinizing Machine Text (ACL 2022)
    url: https://aclanthology.org/2022.acl-long.501/
    accessed: 2026-09-25
  - title: Scarecrow project page
    url: https://yao-dou.github.io/scarecrow/
    accessed: 2026-09-25
  - title: Pagnoni et al. Understanding Factuality in Abstractive Summarization with FRANK (NAACL 2021)
    url: https://aclanthology.org/2021.naacl-main.383/
    accessed: 2026-09-25
  - title: Kocmi and Federmann. GEMBA-MQM, Detecting Translation Quality Error Spans with GPT-4 (arXiv 2310.13988)
    url: https://arxiv.org/pdf/2310.13988
    accessed: 2026-09-25
---

# Span-level error taxonomies (Scarecrow, FRANK, MQM)

> **TL;DR** **Adopt the design pattern, not any one list.** Three mature traditions agree on how a span finding should look. **Scarecrow** gives ten error types for open-ended machine text, each with a *severity 1–3*, an explanation and an optional *antecedent span*. **FRANK** gives a factual-error typology (entity, predicate, circumstance, coreference, discourse link, out-of-article). **MQM** from translation QA gives *minor / major / critical* severity with weights 1 / 5 / 25 and a penalty per word. We take Scarecrow's record shape, FRANK's fact sub-types, and MQM's severity weights. Proposal-specific categories come from LAMP, Shaib and M5.

## Scarecrow (Dou et al., ACL 2022)

Crowd annotation over GPT-2, Grover and GPT-3 text: 1,300 paragraphs, 13k annotations, about 41k spans. Categories:

- **Language errors**: Grammar & usage, Redundant, Off-prompt, Self-contradiction, Incoherent
- **Factual errors**: Technical jargon, Needs Google, Bad math, Commonsense, Encyclopedic

Each span carries a **category, a severity (1–3), a free-text explanation, and an antecedent span** where relevant: the earlier text that a contradiction or redundancy points back to. The antecedent is the piece we most want. "Said twice" and "contradicts paragraph 2" are only actionable with both anchors. The paper's motivation still holds: as models improve, errors shift from syntax to semantic and discourse failures.

## FRANK (Pagnoni et al., NAACL 2021)

A typology of factual errors grounded in frame semantics and discourse, used for 2,250 annotated summaries:

- **Semantic frame**: predicate, entity, circumstance (time, place, manner)
- **Discourse**: coreference, discourse link
- **Content verifiability**: out-of-article (not supported by the source), grammatical

For gentext, "article" means the M3 fact registry and the library chunk the claim came from. FRANK's sub-types make [claim-verification](../llm-evaluation/claim-verification.md) findings more precise. "Wrong entity" (a partner name) needs a different fix from "wrong circumstance" (a date) or "out-of-source" (`[[NEEDS SOURCE]]`).

## MQM (translation QA)

Multidimensional Quality Metrics annotates error spans with a category from a hierarchical tree (accuracy, fluency, terminology, style, locale…) and a **severity**: minor, major or critical. The common weights are **1 / 5 / 25**, and a segment score is the weighted sum, often per 100 words. **GEMBA-MQM** showed that GPT-4 can produce MQM spans few-shot with high *system-level* accuracy. Later work notes that the predicted spans themselves align poorly with human spans. That fits the finding in [s-slop-measurement](s-slop-measurement.md) and argues for validation and calibration.

MQM's *terminology* and *locale* branches map cleanly onto our glossary and context-leakage checks ([check catalog](../nlp-quality/check-catalog.md)).

## What we take

| Element | From | Use in [span-feedback schema](span-feedback-schema.md) |
|---|---|---|
| category + severity + explanation per span | Scarecrow | core fields |
| `antecedent` anchor | Scarecrow | `related_anchor` for redundancy, contradiction, inconsistency |
| fact sub-types | FRANK | `fact.entity`, `fact.circumstance`, `fact.out-of-source`… |
| severity scale + weights, per-100-word penalty | MQM | `severity` enum; paragraph "burden" roll-up (advisory) |
| hierarchical category tree | MQM | dotted category ids (`slop.cliche`, `style.structure`) |
| off-prompt | Scarecrow | `relevance.off-prompt`, checked against the M5 prompt |

## Weaknesses / risks

- None of these was built for persuasive professional prose. Style categories must come from LAMP and Shaib, and genericness from M5 rubric language.
- Crowd severity is noisy. Define severity by *consequence* (see schema), not by annoyance.
- We could not confirm licenses for the Scarecrow or FRANK code and data. We borrow only the categories, which are ideas, not data.

## Verdict rationale

These are stable, well-cited designs that converge on one record shape. Adopting it costs nothing, and it makes our findings interoperable with existing annotation tools such as factgenie ([LLM span annotation](s-llm-span-annotation.md)).

Parent: [Prose signals](index.md) · Up: [Span-feedback schema](span-feedback-schema.md)
