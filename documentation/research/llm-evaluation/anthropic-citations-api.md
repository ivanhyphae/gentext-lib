---
title: Anthropic Citations API
slug: anthropic-citations-api
level: 3
parent: index.md
related: [claim-verification.md, claude-structured-outputs.md, ../provenance/span-anchoring.md]
tags: [claude, citations, grounding, fact-checking]
status: draft
updated: 2026-09-25
kind: service
verdict: adopt
fit: [M3, M7]
license: proprietary API
maturity: mature
inspectability: high
sources:
  - title: "Claude docs: Citations"
    url: https://platform.claude.com/docs/en/build-with-claude/citations
    accessed: 2026-09-25
  - title: "Introducing Citations on the Anthropic API"
    url: https://claude.com/blog/introducing-citations-api
    accessed: 2026-09-25
---

# Anthropic Citations API

> **TL;DR** Attach source documents with `citations: {enabled: true}`. Claude's answer comes back split into text blocks, each with citations pointing at exact spans of the sources, and the pointers are guaranteed valid. **Adopt** it for the support-check step of claim verification. It **cannot be combined with structured outputs** in the same request, so run it as a separate call.

## What it is

A Messages API feature, generally available on the Claude API, AWS, Bedrock, Google Cloud, and Foundry ([docs](https://platform.claude.com/docs/en/build-with-claude/citations)).
- Documents can be plain text, PDF, or "custom content". Custom content lets *us* define the chunking. It is useful for registry entries: one fact, one block.
- Citation location types are `char_location` (text), `page_location` (PDF), and `content_block_location` (custom content). `search_result` blocks can also carry citations.
- The docs state that citations "are guaranteed to contain valid pointers to the provided documents". `cited_text` "does not count toward output tokens" and is not counted as input when passed back.

## Why it matters for adapt-rfp

The verifier's claim "fact F-0123 supports this sentence" has to be checkable without trusting the verifier. With Citations, the proof is a character range in the fact text returned by the API. It is not a quote the model could have paraphrased or invented. That is the same standoff-pointer idea as [span anchoring](../provenance/span-anchoring.md), applied to sources rather than drafts.

## How it would fit

- In [claim verification](claim-verification.md) step 3, send each candidate fact (or source excerpt from the manifest) as a custom-content document titled with its fact id. The prompt is: "For claim C, state whether the documents support, contradict, or do not address it; cite."
- Parse the text blocks into the verdict and the citations. If "supported" comes with no citation, downgrade it to `needs-human`.
- **Incompatibility**: "Citations cannot be used together with structured outputs". Enabling both returns a 400 ([docs](https://platform.claude.com/docs/en/build-with-claude/citations)). Either parse the lightly structured text verdict ourselves, or use two calls: a cited check, then a structured summariser that receives the citations as input.
- Can also run *in reverse* over the draft: send the draft as a document and ask the skeptic to cite the spans it objects to. The API guarantees the pointers, which gives the same guarantee our quote validator provides. The trade-off is again losing strict JSON.

## Strengths

- Pointer-exact, API-guaranteed grounding. This is the strongest inspectability primitive on offer.
- Cheap: cited text is free on output.
- Works with prompt caching, since the registry documents are a stable prefix.

## Weaknesses / risks

- Mutually exclusive with structured outputs, which adds a call and some parsing.
- Only proves that a span was *cited*, not that it *entails* the claim. Entailment judgement is still the model's, so keep the gold-set checks.
- Vendor-specific. The fallback is our own quote-verbatim check, which provides the same guarantee with more code.

## Verdict rationale

**Adopt** for the verification call. It removes a whole class of "the judge misquoted the source" failures at no extra cost.

Parent: [LLM evaluation](index.md)
