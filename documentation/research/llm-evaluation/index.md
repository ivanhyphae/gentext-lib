---
title: LLM-based evaluation and the adversarial pass
slug: index
level: 1
parent: ../index.md
related: [adversarial-review-pass.md, judge-reliability.md, ../provenance/index.md, ../provenance/span-anchoring.md]
tags: [llm-evaluation, llm-as-judge, adversarial-review, fact-checking, eval-harness, claude]
status: draft
updated: 2026-09-25
---

# LLM-based evaluation and the adversarial pass

> **TL;DR** Treat the LLM judge as a *witness*, not an oracle. It has to quote the draft and cite a rubric line for every finding, and a deterministic validator throws out any finding that doesn't. Run it in this order: deterministic M7 checks, claim verification against the M3 fact registry, a small rubric-anchored reviewer panel scoring checklist items, then a skeptical reviewer and one rebuttal round. Output is a JSON findings file rendered as span comments. The scores are advisory. They get trusted item by item, only after calibration against a small human-labelled gold set that includes deliberately fluent but generic decoys.

## The question

Once M6 has composed a draft (for example, EHCRP *Harm Reduction Q1*, 250 words, 6 points), how can Claude critique it the way the EHCRP interagency panel would, find what's missing or unsupported, and avoid rewarding polished, generic prose? It also has to be reproducible, cheap, and auditable.

The solicitation helps. Appendix F's Medium band for HR Q1 penalises responses that describe vulnerabilities "in broad terms that could apply to many communities rather than this one specifically", and the High band asks for "community voices… quotes or stories". The funder's own rubric is anti-generic, so our judge has to be as well.

## Landscape in one screen

| Need | Technique / tool | Verdict | Card |
|---|---|---|---|
| Score a draft against rubric bands | Analytic rubric judging (G-Eval-style, checklist items, evidence first) | adopt | [rubric-judging](rubric-judging.md) |
| Choose between two variants | Pairwise comparison with position swap | trial | [pairwise-comparison](pairwise-comparison.md) |
| Simulate the funder's panel | Reviewer personas scoring the real rubric | trial | [panel-simulation](panel-simulation.md) |
| Red-team / improve | Skeptical critic → bounded reviser (Self-Refine, Constitutional-style) | trial | [critic-reviser-loop](critic-reviser-loop.md) |
| Argue it out | Multi-agent debate | assess (use "rebuttal-lite" only) | [multi-agent-debate](multi-agent-debate.md) |
| Catch hallucinated or unsupported claims | Atomic claim extraction + verification (FActScore, SAFE, CoVe) against M3 | adopt | [claim-verification](claim-verification.md) |
| Grounded, pointer-exact support spans | Anthropic Citations API | adopt | [anthropic-citations-api](anthropic-citations-api.md) |
| Machine-readable verdicts | Claude structured outputs / strict tool use | adopt | [claude-structured-outputs](claude-structured-outputs.md) |
| Cost and repeatability | Prompt caching, Batch API, adaptive thinking | adopt | [claude-caching-batch-thinking](claude-caching-batch-thinking.md) |
| Harness for calibration runs | Inspect AI (UK AISI) | trial | [inspect-ai](inspect-ai.md) |
| YAML test suites, red-team | promptfoo | assess | [promptfoo](promptfoo.md) |
| Metric library | DeepEval (G-Eval, DAG) | hold | [deepeval](deepeval.md) |

Not carded (all accessed 2026-09-25):
- **Ragas**: Apache-2.0. Its [faithfulness](https://docs.ragas.io/en/stable/concepts/metrics/available_metrics/faithfulness/) metric is our claim-verification ratio. Hold.
- **OpenAI Evals platform**: goes read-only 2026-10-31 and shuts down 2026-11-30 ([OpenAI](https://developers.openai.com/api/docs/guides/evals)). Hold.
- **Prometheus 2**: open evaluator LM ([2405.01535](https://arxiv.org/abs/2405.01535)). Hold, since it would need self-hosting.
- **Langfuse / Braintrust** (tracing): Langfuse is still MIT after [ClickHouse bought it](https://clickhouse.com/blog/clickhouse-acquires-langfuse-open-source-llm-observability), and Braintrust's [autoevals](https://github.com/braintrustdata/autoevals) is MIT. Hold, because JSONL run records are enough for now.

## Recommended pipeline (M7 LLM stage)

```
draft.md + provenance map ─┐
M5 question YAML (bands → checklist items with ids) ─┤
M3 facts referenced by the draft ─┤
deterministic M7 report ─┤
sibling answers (same application) ─┘
        │
 1  claim-verify   atomic claims → registry lookup → Citations-API support check
 2  panel          3 personas × checklist items: met/partial/absent + quote → band → points
 3  skeptic        strongest case for a lower band; each finding = quote + rubric_ref
 4  rebuttal       defender may cite only draft spans or registry facts; adjudicator rules
 5  validate       deterministic: quote occurs verbatim? rubric_ref exists? else drop + log
        │
 findings.jsonl  →  rendered report / Claude Docs comments (anchored like provenance spans)
```

The design is detailed in [adversarial-review-pass](adversarial-review-pass.md). The reasons behind each guard (position, verbosity, self-preference, score compression, rationalisation) are in [judge-reliability](judge-reliability.md).

## Key recommendations

1. **Evidence before verdict.** Decompose each rubric band into binary checklist items in M5, for example `HR-Q1.high.voices: community quotes or stories present`. The judge marks each item and quotes the span before it assigns a band. UK AISI asks evaluators to "restrict your use of model graded scoring to content matching" and warns that numeric rating has "known accuracy and bias issues" ([AISI standard](https://ukgovernmentbeis.github.io/as-evaluation-standard/), accessed 2026-09-25).
2. **Every critique is falsifiable.** Record `{quote.exact, prefix, suffix}` using the same TextQuoteSelector shape as [provenance span anchoring](../provenance/span-anchoring.md), plus a `rubric_ref`. If the quote isn't in the draft, the finding is discarded.
3. **Anti-generic guards**: a place-swap probe, deterministic specificity metrics from M4, generic decoys in the gold set, and perturbation tests. The score must drop when the community quote is removed.
4. **Separate the judge from the drafter.** Use a fresh context, a different prompt, and ideally a different model tier. Occasionally spot-check with a non-Claude judge, because self-preference also shows up under rubric grading ([arXiv 2604.06996](https://arxiv.org/abs/2604.06996), accessed 2026-09-25).
5. **Humans decide.** The LLM pass never auto-edits canonical text and never reports a "predicted score". Recent grant-review studies find that LLM scores compress the range and fail to reproduce human funding decisions ([Frontiers 2026](https://www.frontiersin.org/journals/education/articles/10.3389/feduc.2026.1856134/full); [arXiv 2603.08281](https://arxiv.org/abs/2603.08281), both accessed 2026-09-25).

## Children

- Level 2: [adversarial-review-pass](adversarial-review-pass.md), [judge-reliability](judge-reliability.md)
- Level 3: [rubric-judging](rubric-judging.md), [pairwise-comparison](pairwise-comparison.md), [panel-simulation](panel-simulation.md), [critic-reviser-loop](critic-reviser-loop.md), [multi-agent-debate](multi-agent-debate.md), [claim-verification](claim-verification.md), [anthropic-citations-api](anthropic-citations-api.md), [claude-structured-outputs](claude-structured-outputs.md), [claude-caching-batch-thinking](claude-caching-batch-thinking.md), [inspect-ai](inspect-ai.md), [promptfoo](promptfoo.md), [deepeval](deepeval.md)

Parent: [research index](../index.md)
