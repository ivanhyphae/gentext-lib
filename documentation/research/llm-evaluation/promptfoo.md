---
title: promptfoo
slug: promptfoo
level: 3
parent: index.md
related: [inspect-ai.md, deepeval.md, pairwise-comparison.md]
tags: [eval-harness, yaml, red-team, cli]
status: draft
updated: 2026-09-25
kind: library
verdict: assess
fit: [M7]
license: MIT
maturity: mature
inspectability: medium
sources:
  - title: "promptfoo: Model-graded metrics"
    url: https://www.promptfoo.dev/docs/configuration/expected-outputs/model-graded/
    accessed: 2026-09-25
  - title: "promptfoo: LLM Rubric"
    url: https://www.promptfoo.dev/docs/configuration/expected-outputs/model-graded/llm-rubric/
    accessed: 2026-09-25
  - title: "Promptfoo is joining OpenAI (promptfoo blog)"
    url: https://www.promptfoo.dev/blog/promptfoo-joining-openai/
    accessed: 2026-09-25
  - title: "OpenAI to acquire Promptfoo"
    url: https://openai.com/index/openai-to-acquire-promptfoo/
    accessed: 2026-09-25
---

# promptfoo

> **TL;DR** A CLI and YAML test runner for prompts. You declare a prompts × providers × test cases matrix with assertions: deterministic, `llm-rubric`, `g-eval`, `factuality`, `select-best`, and more. It has strong red-teaming features. It is MIT and still open source, but OpenAI announced an acquisition in March 2026. **Assess**: good for quick prompt A/B matrices, but it duplicates what our Python pipeline and Inspect already give us.

## What it is

- **Assertions**: deterministic ones (contains, regex, JSON schema, and others) plus model-graded ones. The model-graded set includes `llm-rubric`, `g-eval`, `factuality`, `model-graded-closedqa`, `select-best`, `context-faithfulness`, `answer-relevance`, and `search-rubric` ([docs](https://www.promptfoo.dev/docs/configuration/expected-outputs/model-graded/)).
- **`llm-rubric`** returns `{reason, score 0–1, pass}`. It supports a `threshold`, a custom `rubricPrompt`, and a per-assertion grader `provider` ([docs](https://www.promptfoo.dev/docs/configuration/expected-outputs/model-graded/llm-rubric/)). Anthropic is a supported grader.
- **Red-team module**: automated adversarial probes for jailbreaks and injection. These are aimed at app security, not prose quality.
- **Ownership**: on 2026-03-09 OpenAI announced it would acquire Promptfoo. Both sides say it stays open source under its current license ([OpenAI](https://openai.com/index/openai-to-acquire-promptfoo/); [promptfoo blog](https://www.promptfoo.dev/blog/promptfoo-joining-openai/)).

## Why it matters for gentext

It is the fastest way to answer "which of these three judge prompts best separates the decoy from the real draft?" You write one YAML file, run `promptfoo eval`, and read a side-by-side matrix. It is also a plausible regression suite for our M8 skills.

## How it would fit

- Optional `evals/promptfoo/judge-prompts.yaml`, where test cases are gold answers and assertions are `javascript` or `python` checks on our JSON verdict fields.
- Grader provider pinned to a Claude model, overriding the environment-based default.

## Strengths

- Very low friction, declarative, with a nice matrix viewer. Config diffs cleanly in git.
- Mix of deterministic and model-graded assertions in one place.
- `select-best` gives pairwise-style comparison out of the box ([pairwise-comparison](pairwise-comparison.md)).

## Weaknesses / risks

- Node/TypeScript tooling in a Python repo (DR-0006) adds a second runtime.
- Built-in grader prompts are opaque unless overridden. Its `score 0–1` output is the numeric rating AISI discourages, so we would override it with our own checklist schema anyway.
- Ownership by an LLM vendor that competes with our primary model. The licence is fine today, but the roadmap could tilt toward OpenAI's platform (speculative).

## Verdict rationale

**Assess.** Revisit if prompt-variant sweeps become frequent and the Inspect trial feels heavy. Not needed for the pilot slice.

Parent: [LLM evaluation](index.md)
