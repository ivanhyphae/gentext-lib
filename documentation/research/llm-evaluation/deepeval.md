---
title: DeepEval
slug: deepeval
level: 3
parent: index.md
related: [rubric-judging.md, inspect-ai.md, promptfoo.md, claim-verification.md]
tags: [eval-harness, python, metrics, g-eval, pytest]
status: draft
updated: 2026-09-25
kind: library
verdict: hold
fit: [M7]
license: Apache-2.0
maturity: mature
inspectability: medium
sources:
  - title: DeepEval metrics introduction
    url: https://deepeval.com/docs/metrics-introduction
    accessed: 2026-09-25
  - title: DeepEval Anthropic integration
    url: https://deepeval.com/integrations/models/anthropic
    accessed: 2026-09-25
  - title: deepeval on PyPI
    url: https://pypi.org/project/deepeval/
    accessed: 2026-09-25
---

# DeepEval

> **TL;DR** A pytest-style Python library from Confident AI (Apache-2.0) with ready-made LLM-as-judge metrics. Two are relevant: **G-Eval**, custom criteria with chain-of-thought scoring, and **DAG**, a decision-tree judge that gives deterministic scores for objective criteria. It supports Claude as the judge. **Hold**: the DAG idea is worth borrowing, but the library's opaque metric prompts and 0–1 scores work against our quote-and-rubric-id contract.

## What it is

- **Metrics**: G-Eval (subjective custom criteria), DAG (a graph of yes/no judge nodes with deterministic scoring), plus RAG metrics (faithfulness and others), hallucination, and bias ([docs](https://deepeval.com/docs/metrics-introduction)).
- Runs as unit tests (`assert_test`), so it slots into CI.
- Model-agnostic, including Anthropic ([integration](https://deepeval.com/integrations/models/anthropic)).
- Apache-2.0. The optional Confident AI cloud handles dashboards.

## Why it matters for adapt-rfp

The **DAG metric** is a close cousin of our checklist design. Each rubric item becomes a node with a narrow yes/no question, and the band is computed from the pattern of answers rather than asked for. That makes scoring more deterministic and explainable. We can implement the same idea directly: M5 checklist items → per-item statuses → a band computed by a rule in Python.

## How it would fit (if adopted)

- `tests/qa_llm/test_hr_q1.py`, using DeepEval test cases over gold answers with custom metrics that wrap our judge.
- In practice most of the value would come from the pytest ergonomics, which we could get without the dependency.

## Strengths

- Mature, popular, Python-native, pytest-friendly.
- DAG-style structure is a good pattern for rule-computed bands.
- Many ready metrics for fast baselines.

## Weaknesses / risks

- Metric prompts are library internals. A score change after an upgrade is hard to explain, which lowers inspectability.
- 0–1 scores and "reason" strings don't enforce our quote + `rubric_ref` contract.
- Overlaps with Inspect (logging and repeats) and with our own validator.
- There is a pull toward the vendor cloud for dashboards.

## Verdict rationale

**Hold** the library and **borrow the DAG pattern**: compute the band from item statuses with a rule stored beside the rubric in M5 YAML. Reconsider if we later need many off-the-shelf metrics quickly.

Parent: [LLM evaluation](index.md)
