---
title: Judge reliability and bias
slug: judge-reliability
level: 2
parent: index.md
related: [rubric-judging.md, pairwise-comparison.md, panel-simulation.md, adversarial-review-pass.md, inspect-ai.md]
tags: [llm-as-judge, bias, calibration, reliability, grant-review]
status: draft
updated: 2026-09-25
---

# Judge reliability and bias

> **TL;DR** LLM judges agree with humans often enough to be useful and diverge in systematic ways. They favour the first position, longer text, their own family's output, and confident-sounding cues. On grant review they compress scores and inflate them in zero-shot. The fixes are cheap and structural: checklist items over holistic numbers, evidence before verdict, position swaps, fixed length, a separate judge context, few-shot anchors, and a small human gold set measured with Cohen's kappa. Trust an item only once it passes calibration.

## Known failure modes

| Bias | Evidence | Mitigation in adapt-rfp |
|---|---|---|
| **Position** | Zheng et al. named position, verbosity, and self-enhancement bias while finding GPT-4 reached >80% agreement with humans ([2306.05685](https://arxiv.org/abs/2306.05685)). Wang et al. showed GPT-4 favours the first candidate and proposed *balanced position calibration* (score both orders) and *multiple evidence calibration* (evidence before rating) ([2305.17926](https://arxiv.org/abs/2305.17926)). | Pairwise only with both orders; ties when orders disagree ([pairwise-comparison](pairwise-comparison.md)) |
| **Verbosity** | Judges favour longer responses ([2306.05685](https://arxiv.org/abs/2306.05685)). Verbosity and confidence cues shift both verdicts and explanations ([2605.23970](https://arxiv.org/abs/2605.23970)). | Word limits fixed by M5; compare at equal length; booster counts reported deterministically |
| **Self-preference** | LLMs recognise and favour their own generations, and self-recognition correlates with bias ([2404.13076](https://arxiv.org/abs/2404.13076)). Under *rubric* grading, judges were >50% more likely to wrongly mark a failed rubric item "satisfied" for their own family's output. Ensembling reduced but did not remove the effect ([2604.06996](https://arxiv.org/abs/2604.06996)). | Judge ≠ drafter context and prompt; different Claude tier; periodic non-Claude spot check; human gold set is final |
| **Leniency / gullibility** | Judges are "more lenient than strict" and can be fooled by stock replies. Percent agreement hides disagreement that Cohen's kappa exposes ([2406.12624](https://arxiv.org/abs/2406.12624)). | Report kappa per checklist item; include decoys |
| **Rationalisation** | Explanations drift with non-evidential cues. *Proof-before-preference* ordering improves invariance ([2605.23970](https://arxiv.org/abs/2605.23970)). | Quote-then-status-then-band schema order |
| **Numeric rating** | UK AISI discourages asking a model to "numerically rate outputs" because of "known accuracy and bias issues" ([AISI standard](https://ukgovernmentbeis.github.io/as-evaluation-standard/)). | Binary/ternary items; points derived from band, shown as a range |
| **Criteria drift** | People refine criteria *by* grading outputs, so the criteria can't be fixed in advance ([EvalGen, 2404.12272](https://arxiv.org/abs/2404.12272)). | Version the M5 checklist; expect edits after the first 10 labelled drafts |

## What grant-review studies say (2026)

- **Score compression and optimism.** On seed-grant applications, zero-shot LLM reviewers scored higher than humans, used a 49–59% narrower spread, and matched funding decisions at or below chance. Few-shot examples gave the closest means. Adding "strict" instructions over-corrected to about 10.7 points low on a 100-point scale ([Frontiers in Education, 2026](https://www.frontiersin.org/journals/education/articles/10.3389/feduc.2026.1856134/full)). The lesson is to calibrate with examples, not adjectives.
- **Section-by-section beats persona councils.** On EPSRC proposals with controlled perturbations, section-by-section analysis beat both single-pass review and a "Council of Personas" ensemble. Alignment problems were caught, clarity problems were "largely missed", and feedback leaned toward "compliance checking over holistic assessment" ([arXiv 2603.08281](https://arxiv.org/abs/2603.08281)). The lesson: run personas per question and per checklist item, and don't expect the LLM to judge clarity well. Keep readability in M4 and human review.
- **Coarse alignment, fine divergence.** Frontier models separated accept from reject on ICLR papers but not oral from poster ([arXiv 2608.03659](https://arxiv.org/abs/2608.03659)). The lesson: trust band-level signals (High, Medium, Low) more than point-level ones.

## Calibration protocol (proposal)

1. **Gold set, about 20 answers**, for HR Q1 first, then the other questions:
   - existing pilot pre-app answers, long and SHORTENED;
   - 2–3 **generic decoys** (fluent, on-topic, placeless);
   - 2–3 **perturbed** variants (voices removed, place swapped, boosters added);
   - once they exist, human-edited finals.
2. **Two humans** label each checklist item `met / partial / absent` with quotes, blind to the LLM output.
3. Run the judge **k = 3 times** per answer in [Inspect AI](inspect-ai.md). Record per-item Cohen's kappa against humans, self-consistency across runs, the invalid-quote rate, and whether decoys and perturbations move the scores in the expected direction.
4. **Trust rule**, a heuristic of ours rather than a published threshold: an item's LLM status is shown to users only when its kappa with the humans is at least 0.6 and at least equal to the human–human kappa minus 0.15. Otherwise the item is reported as "LLM opinion, uncalibrated".
5. Re-run whenever the prompt, model, or rubric version changes. Prompt hashes are stored in each run record.

## Judge configuration defaults

- Fresh context per role. The drafter's conversation is never reused.
- Evidence-first schema order (quote, status, band, points), enforced by [structured outputs](claude-structured-outputs.md).
- Two or three few-shot anchors per band, drawn from the gold set. Adjectives like "be harsh" are avoided.
- Hold effort and thinking settings stable per run. Changing them invalidates the cache and shifts behaviour ([claude-caching-batch-thinking](claude-caching-batch-thinking.md)).
- Anthropic's own guidance: it is "generally best practice to use a different model to evaluate than the model used to generate the evaluated output" ([Claude docs: define success criteria and build evaluations](https://platform.claude.com/docs/en/test-and-evaluate/develop-tests)). With Claude as the primary model, we approximate this with a different tier and prompt, plus the spot checks above.

## Sources (all accessed 2026-09-25)

- Zheng et al., Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena. https://arxiv.org/abs/2306.05685
- Wang et al., Large Language Models are not Fair Evaluators. https://arxiv.org/abs/2305.17926
- Panickssery, Bowman, Feng, LLM Evaluators Recognize and Favor Their Own Generations. https://arxiv.org/abs/2404.13076
- Pombal, Rei, Martins, Self-Preference Bias in Rubric-Based Evaluation of LLMs. https://arxiv.org/abs/2604.06996
- Thakur et al., Judging the Judges. https://arxiv.org/abs/2406.12624
- Tapwal, Kumar, Maple, Faithful or Fabricated? https://arxiv.org/abs/2605.23970
- Shankar et al., Who Validates the Validators? https://arxiv.org/abs/2404.12272
- UK AISI, Autonomous Systems Evaluation Standard. https://ukgovernmentbeis.github.io/as-evaluation-standard/
- Evaluating LLMs as grant reviewers (Frontiers in Education, 2026). https://www.frontiersin.org/journals/education/articles/10.3389/feduc.2026.1856134/full
- Thorne et al., structured perturbations. https://arxiv.org/abs/2603.08281
- Camelo-Guerrero, Diaz-Rodriguez, How Closely Do LLM Reviews Align with Human Peer Review? https://arxiv.org/abs/2608.03659

Parent: [LLM evaluation](index.md)
