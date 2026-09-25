---
title: Automated essay scoring (ELLIPSE analytic traits, PERSUADE discourse elements)
slug: m-aes-ellipse
level: 3
parent: index.md
related: [holistic-metrics.md, m-grammar-error-density.md, m-readability-sophistication.md, ../llm-evaluation/rubric-judging.md]
tags: [aes, essay-scoring, ellipse, persuade, feedback-prize, discourse-elements]
status: draft
updated: 2026-09-25
kind: technique
verdict: assess
fit: [M4, M7]
license: ELLIPSE and PERSUADE corpora CC BY-NC-SA 4.0; KevSun/Engessay_grading_ML model card says MIT (trained on NC data); Kaggle solution code MIT
maturity: emerging
inspectability: low
sources:
  - title: scrosseye/ELLIPSE-Corpus (≈6,500 ELL essays, grades 8–12; holistic + cohesion, syntax, vocabulary, phraseology, grammar, conventions; CC BY-NC-SA 4.0)
    url: https://github.com/scrosseye/ELLIPSE-Corpus
    accessed: 2026-09-25
  - title: Crossley et al. (2023/24), The ELLIPSE Corpus (Int. J. Learner Corpus Research)
    url: https://benjamins.com/catalog/ijlcr.22026.cro
    accessed: 2026-09-25
  - title: KevSun/Engessay_grading_ML (RoBERTa, six ELLIPSE traits, 1–5; reported QWK 0.85)
    url: https://huggingface.co/KevSun/Engessay_grading_ML
    accessed: 2026-09-25
  - title: Sun & Wang (2024), Automatic Essay Multi-dimensional Scoring with Fine-tuning and Multiple Regression (arXiv 2406.01198)
    url: https://arxiv.org/abs/2406.01198
    accessed: 2026-09-25
  - title: Feedback Prize – English Language Learning, 1st-place solution (MIT; 71-model ensemble)
    url: https://github.com/rohitsingh02/kaggle-feedback-english-language-learning-1st-place-solution
    accessed: 2026-09-25
  - title: scrosseye/PERSUADE_corpus (25k+ argumentative essays; Lead, Position, Claim, Counterclaim, Rebuttal, Evidence, Concluding Summary; CC BY-NC-SA 4.0)
    url: https://github.com/scrosseye/PERSUADE_corpus
    accessed: 2026-09-25
  - title: Crossley et al. (2022), PERSUADE corpus 1.0 (Assessing Writing)
    url: https://www.sciencedirect.com/science/article/pii/S1075293522000630
    accessed: 2026-09-25
  - title: Li & Ng (2024), Automated Essay Scoring, Recent Successes and Future Directions (IJCAI survey)
    url: https://www.ijcai.org/proceedings/2024/0897.pdf
    accessed: 2026-09-25
---

# Automated essay scoring (ELLIPSE, PERSUADE)

> **TL;DR** **Assess.** ELLIPSE-trained scorers give six analytic traits (cohesion, syntax, vocabulary, phraseology, grammar, conventions) and do separate *broken* or *childlike* prose from competent prose. On professional grant text they **hit a ceiling**, and in our probe they rated fluent "AI slop" as highly as the firm's best paragraphs. Use a trait scorer only as a **floor detector** ("is something badly wrong here?"). Borrow the **trait vocabulary** and the PERSUADE discourse-element idea for Claude's rubric. The data licenses are non-commercial.

## What it is

- **ELLIPSE** (Crossley et al.): about 6,500 essays by English-language learners in grades 8–12, double-scored 1–5 for overall proficiency and six analytic traits. It underlies Kaggle's *Feedback Prize – English Language Learning* (2022), where top solutions were DeBERTa-v3-large ensembles (winning MCRMSE ≈ 0.43, *unverified*; the 1st-place solution used 71 models).
- **Pretrained model:** `KevSun/Engessay_grading_ML` (RoBERTa, about 125M parameters) outputs the six traits and reports QWK 0.85. The model card says MIT, but the model is trained on CC BY-NC-SA data, so its license status is **ambiguous**.
- **PERSUADE** (25k+ argumentative essays, grades 6–12): token spans labelled Lead, Position, Claim, Counterclaim, Rebuttal, Evidence, Concluding Summary. Used by *Feedback Prize – Evaluating Student Writing* (top accuracy ≈ 75%). Winning models are on Kaggle. We found no maintained HF checkpoint *(searched 2026-09-25)*.

## Probe on the pilot (KevSun model, raw trait outputs, 2026-09-25)

| Sample | cohesion | syntax | vocab | phraseology | grammar | conventions |
|---|---|---|---|---|---|---|
| Pilot narratives (4 paragraphs), range | 4.05–4.36 | 4.04–4.35 | 4.23–4.53 | 4.28–4.46 | 4.31–4.49 | 4.08–4.46 |
| Firm boilerplate | 4.31 | 4.32 | 4.43 | 4.40 | 4.49 | 4.42 |
| Synthetic "AI slop" | 4.33 | 4.36 | **4.53** | 4.33 | 4.37 | 4.47 |
| Synthetic 4th-grade | 3.36 | 3.59 | 3.51 | 3.68 | 4.08 | 3.75 |
| Synthetic ungrammatical | **2.94** | **2.75** | **2.83** | **2.57** | **2.25** | **3.03** |

Findings: the scorer separates the two floor cases by 1–2 points. All professional text is compressed into 4.0–4.5, and the slop scores at the top. The lowest pilot paragraph (4.05 cohesion) contains the known "one of the primary recreational facility" defect, but that gap is within noise. **AES measures L2 proficiency, not proposal quality.**

## Transferability

AES models are known to be prompt- and population-specific. Cross-prompt generalization is an open research problem (IJCAI 2024 survey). Professional, jargon-heavy, adult prose is far outside grade 8–12 learner essays. Expect ceiling effects and rewards for fluency over substance.

## Granularity and reliability

Document-level (512 tokens), with no spans. Running it per paragraph gives coarse localization. A 250-word answer is inside the training length range (ELLIPSE essays are of similar length). It runs on CPU in about 1 s per paragraph.

## How it would fit

- **M7 floor check:** flag paragraphs whose grammar/syntax traits fall below the reference corpus's 5th percentile. This happens with pasted partner text, OCR, or a botched LLM compression.
- **Rubric vocabulary:** give Claude the six ELLIPSE traits and the PERSUADE element types as named dimensions ("Claim without Evidence", "no Concluding Summary"). Claude does the segmenting, with quoted spans ([rubric-judging](../llm-evaluation/rubric-judging.md)).

## Weaknesses / risks

- NC-licensed training data; opaque neural scores; demographic bias concerns in AES.
- Rewards fluent slop, so on its own it can never support "this is good".

## Verdict rationale

A real signal only at the bottom of the scale. Worth a trial slot as a floor detector if the license question is resolved. Otherwise, re-derive the traits through the grammar-density and readability metrics we already compute.

Parent: [Prose signals](index.md) · Up: [Holistic metrics](holistic-metrics.md)
