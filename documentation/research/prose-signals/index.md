---
title: Prose signals — holistic and span-level quality feedback
slug: index
level: 1
parent: ../index.md
children:
  - holistic-metrics.md
  - ai-slop.md
  - span-feedback-schema.md
  - commercial-apis.md
related: [../nlp-quality/index.md, ../llm-evaluation/index.md]
tags: [quality, style, slop, metrics, feedback]
status: draft
updated: 2026-09-25
---

# Prose signals — holistic and span-level quality feedback

> **TL;DR** Claude needs signal on bigger chunks of text ("this is generic", "this is AI slop", "a 4th grader wrote this", "big grammar problems here"). You can't rent it: no API returns it as span-level findings. **Build a signal panel** of three kinds of detector. **Deterministic:** a curated slop lexicon and patterns, shared with the `humanizer` skill. **Statistical:** concreteness, anchor density, grammar density, readability, genericness and voice distance, each reported as a **percentile against Hyphae's own exemplar corpus**, plus the open WQRM writing-quality model. **LLM:** a quote-validated Claude span annotator using research slop taxonomies. All three emit one **[finding record](span-feedback-schema.md)** (quoted span, category, severity, evidence, suggested action) that Claude revises from. Signals are **evidence, never verdicts**: nobody, human or LLM, is reliable at a binary "is this slop?" call, but experts agree on specific spans and edits.

This topic extends the copy-editing checks in [nlp-quality](../nlp-quality/index.md) and feeds the rubric pass in [llm-evaluation](../llm-evaluation/index.md).

## The maintainer's complaints → named symptoms → signals

| Complaint | Symptom (finding category) | Main signals | Read more |
|---|---|---|---|
| "This is generic" | `specificity.generic`, `slop.density` | Concreteness + anchor density (names, numbers, places per 100 words) vs the exemplar corpus; portability / place-swap test; similarity to boilerplate and to an "LLM consensus" answer; Claude annotator | [m-specificity-concreteness](m-specificity-concreteness.md) (adopt), [m-genericness](m-genericness.md) (trial) |
| "This is AI slop" | `slop.*` (cliché, templated structure, purple prose, unnecessary exposition, contrast frames, tricolons…) | Curated lexicon/patterns with a funder-term allowlist; WQRM paragraph score; LAMP/Shaib taxonomy via the Claude span annotator | [ai-slop](ai-slop.md), [s-slop-lexicons](s-slop-lexicons.md), [s-edit-based-rewards-lamp](s-edit-based-rewards-lamp.md), [s-llm-span-annotation](s-llm-span-annotation.md) |
| "A 4th grader wrote this" / "too dense" | `readability.childlike`, `readability.dense` | Readability ensemble + sentence length + lexical sophistication, as percentiles (not raw Flesch) | [m-readability-sophistication](m-readability-sophistication.md) (trial) |
| "Big grammar problems here" | `grammar.*` density per paragraph | LanguageTool counts per 100 words + CoLA-style acceptability per sentence (flag only; **never auto-correct**) | [m-grammar-error-density](m-grammar-error-density.md) (trial) |
| "Doesn't sound like us" | `voice.off` | Burrows' Delta / embedding distance to the firm corpus | [m-voice-distance](m-voice-distance.md) (trial) |

## What the probes on pilot text showed

The probes ran locally on paragraphs from the Ambrose docs plus synthetic controls:
- Every bad control was caught by **at least two** signals.
- The worst sentence by the CoLA grammar classifier was the known "one of the primary recreational facility" defect. LanguageTool missed it again.
- Firm boilerplate scored about the same as the slop sample on **concreteness** (2.71 vs 2.70). Our own boilerplate is part of the problem.
- One narrative paragraph averages 51 words per sentence, and 60% of its sentences closely match method text from other projects.
- **WQRM** scored pilot paragraphs 5.3–8.5. A synthetic slop paragraph scored 4.3, and its concrete rewrite scored 6.7.
- **Misleading signals:** lexical diversity (MTLD) is *highest* for slop; the essay scorers (ELLIPSE) and the CoLA classifier rate slop as well as good text; the public Slop Score word list mostly flagged legit program vocabulary (*resilience*, *stewardship*).
- **Danger:** a Flan-T5 grammar corrector changed facts ("2023–2026" → "2012-2015", "Hyphae has" → "He has"). Correction models must never auto-apply.

## Design rules

1. **Norm everything** against a named reference corpus (Hyphae's best submitted proposals, then funder-winning exemplars when available). Report the percentile, the direction ("low is bad"), a reliability flag (too short, out of domain), and the worst spans. [m-norming-presentation](m-norming-presentation.md) (adopt)
2. **Name symptoms, not scores.** Don't collapse the signals into one composite number.
3. **One finding format** for every detector, a superset of the adversarial-pass and check-catalog reports. LLM findings are witnesses: the validator must find the quote, or the finding is dropped. [span-feedback-schema](span-feedback-schema.md)
4. **Fixes respect provenance and truth:** suggestions carry constraints (`no-new-facts`, `keep-funder-terms`), and "make specific" means pulling a sourced fact from M3 or inserting `[[NEEDS SOURCE]]`.
5. **AI-text detectors stay on hold.** They answer "who wrote it", which provenance already records (DR-0008), and their false-positive rates on edited professional text are poor. [s-ai-detectors](s-ai-detectors.md)

## Buy vs build

Mostly build. No hosted service returns holistic span-level feedback. Grammarly's developer SDK was shut down in 2024, and what remains are Enterprise-only admin APIs with document-level scores. [commercial-apis](commercial-apis.md)
- **Trial:** [Sapling](a-sapling.md) for cheap grammar spans and style-guide checks; [Gemini on Google Cloud](a-google-cloud-nl-vertex.md) as a *different-family* second-opinion judge against Claude's self-preference.
- **Assess:** [LanguageTool API](a-languagetool-api.md), [AI-detection APIs](a-ai-detection-apis.md) (advisory heat map at most).
- **Hold:** [Grammarly](a-grammarly.md), [Writer](a-writer.md), [minor and discontinued tools](a-minor-and-discontinued.md).

## License watch
TAALES, TAACO, TAASSC, LFTK, and the ELLIPSE/PERSUADE corpora are **non-commercial**. The CoLA checkpoint states no license. WQRM is MIT. Pick implementations accordingly.

## How Claude gets this signal (proposed tool surface)
- `gentext signals <draft> --against firm-exemplar` → a findings file (YAML/JSON), sorted by severity. It's exposed as a CLI now and as an MCP tool on Cloud Run later (DR-0009).
- `gentext signals --explain <finding-id>` → the metric's norm, the neighbouring exemplar spans, and the suggestion constraints.
- The revise loop: Claude addresses `major`+ findings, re-runs the signals, and marks each finding `fixed` / `rejected (reason)`. The findings file becomes part of the chunk's provenance.

## Pages
- Level 2: [holistic-metrics](holistic-metrics.md) · [ai-slop](ai-slop.md) · [span-feedback-schema](span-feedback-schema.md) · [commercial-apis](commercial-apis.md)
- Metrics: [m-specificity-concreteness](m-specificity-concreteness.md) · [m-genericness](m-genericness.md) · [m-readability-sophistication](m-readability-sophistication.md) · [m-grammar-error-density](m-grammar-error-density.md) · [m-voice-distance](m-voice-distance.md) · [m-perplexity](m-perplexity.md) · [m-aes-ellipse](m-aes-ellipse.md) · [m-norming-presentation](m-norming-presentation.md)
- Slop and spans: [s-slop-measurement](s-slop-measurement.md) · [s-edit-based-rewards-lamp](s-edit-based-rewards-lamp.md) · [s-slop-lexicons](s-slop-lexicons.md) · [s-llm-span-annotation](s-llm-span-annotation.md) · [s-scarecrow-taxonomy](s-scarecrow-taxonomy.md) · [s-writing-critic-models](s-writing-critic-models.md) · [s-ai-detectors](s-ai-detectors.md)
- APIs: [a-sapling](a-sapling.md) · [a-google-cloud-nl-vertex](a-google-cloud-nl-vertex.md) · [a-languagetool-api](a-languagetool-api.md) · [a-ai-detection-apis](a-ai-detection-apis.md) · [a-grammarly](a-grammarly.md) · [a-writer](a-writer.md) · [a-minor-and-discontinued](a-minor-and-discontinued.md)
