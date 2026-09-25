---
title: Inspect AI (UK AISI)
slug: inspect-ai
level: 3
parent: index.md
related: [promptfoo.md, deepeval.md, judge-reliability.md, claude-caching-batch-thinking.md]
tags: [eval-harness, python, calibration, logging]
status: draft
updated: 2026-09-25
kind: library
verdict: trial
fit: [M7]
license: MIT
maturity: mature
inspectability: high
sources:
  - title: Inspect AI documentation
    url: https://inspect.aisi.org.uk/
    accessed: 2026-09-25
  - title: UKGovernmentBEIS/inspect_ai (GitHub)
    url: https://github.com/UKGovernmentBEIS/inspect_ai
    accessed: 2026-09-25
  - title: UK AISI Autonomous Systems Evaluation Standard
    url: https://ukgovernmentbeis.github.io/as-evaluation-standard/
    accessed: 2026-09-25
---

# Inspect AI (UK AISI)

> **TL;DR** A Python eval framework from the UK AI Security Institute, MIT-licensed. Tasks are built from datasets, solvers, and scorers, and every run writes a structured log with a browser viewer (`inspect view`). It supports Anthropic models and batch mode. **Trial** it as the *calibration harness* that runs judge prompts against the human-labelled gold set. The production review pass stays a plain module in M7.

## What it is

- **Abstractions**: `Task` = dataset (samples with input and target) + solver (how the model responds) + scorer (how the response is graded). There are built-in model-graded scorers (`model_graded_qa`, `model_graded_fact`), custom scorers, and multiple scorers per task ([docs](https://inspect.aisi.org.uk/)).
- **Logs**: structured eval logs, readable programmatically or as data frames, and viewable in a local web UI.
- **Models**: provider-agnostic. Anthropic via `pip install anthropic` and `ANTHROPIC_API_KEY`. There is a documented "Batch Mode".
- **License**: MIT ([GitHub](https://github.com/UKGovernmentBEIS/inspect_ai)). Maintained by UK AISI with Meridian Labs.
- **House guidance**: AISI's evaluation standard asks users to restrict model-graded scoring to content matching against ground truth ([standard](https://ukgovernmentbeis.github.io/as-evaluation-standard/)). That supports our checklist design.

## Why it matters for adapt-rfp

The calibration loop in [judge-reliability](judge-reliability.md) runs roughly 20 gold answers × personas × k runs × prompt variants, and computes per-item agreement with the humans. Someone has to own datasets, repeats, logs, and comparisons across prompt versions. Inspect does that in Python (our language per DR-0006), keeps logs as files, and gives a free viewer for walking through transcripts. That is the inspectability we want.

## How it would fit

- `evals/judge_calibration.py` (planned):
  - dataset = gold answers + human item labels from the repo;
  - solver = our actual M7 judge function, wrapped, so the harness tests production code rather than a copy;
  - scorer = per-item agreement (and kappa computed over the log afterwards).
- `evals/perturbations.py`: generate the decoys and perturbations, then assert direction of change (e.g. removing voices lowers `voices`).
- Logs go to a derived directory, never committed (DR-0005). A summary table *is* committed with each prompt-version change.
- Runs from the CLI, so a Claude Code session can launch a calibration run and read the results.

## Strengths

- Serious, maintained, government-backed. It is widely used for frontier evals.
- File-based logs and a viewer give high inspectability with no SaaS.
- Code-first Python composes with our Pydantic schemas and Anthropic SDK.
- Epochs and repeats, plus multiple scorers, map directly onto k-run self-consistency.

## Weaknesses / risks

- Heavier than we need for the production pass, and built for benchmark-style tasks.
- The learning curve is modest but real for non-engineers. The viewer mitigates it.
- The fit of batch mode with our caching layout is *(unverified)* until tried.

## Verdict rationale

**Trial** for calibration and regression only. If it proves awkward, a 150-line pytest-plus-JSONL runner is the fallback. Either way the gold set and scorers stay ours.

Parent: [LLM evaluation](index.md)
