# 0008. Authorship is first-class provenance, at chunk level and optionally at span level

- Status: Proposed (schema pending research: `documentation/research/provenance/`)
- Date: 2026-09-25
- Deciders: Ivan Heitmann; Claude (drafting)

## Context
The maintainer: *partner text is often incorporated into final proposals and reused without distinction, but who wrote text chunks will be essential provenance, especially as AI generates text. Metadata may need to store this and other dimensions over specific strings, which may be a can of worms.*

Pilot evidence: one working doc mixes Hyphae boilerplate, I-ReLab (partner) strategy prose, CCRCD/ARPD agency text, and text of unknown origin. Once composed and edited, authorship becomes invisible.

## Decision (proposed)
1. **Chunk level (mandatory):** every chunk and every variant records `authors[]`, each an agent with `kind` (person | org | ai), `id`, and `role` (wrote | adapted | edited | approved | generated). For AI: model id, date, and the input chunk/fact ids. Plus `owner` (the org with reuse rights) and `derived_from`.
2. **Span level (optional, sidecar):** when a variant mixes authors, or an AI adapted part of a human text, a standoff sidecar records spans (anchored by text quote + context, not by offsets alone) with their own authors and fact references. Deterministic tools maintain the sidecar, never hand edits.
3. **Don't block on perfection.** Unknown authorship is recorded as `unknown`, never guessed.
4. Final schema shape will follow the provenance research (PROV-O vocabulary, Web Annotation-style selectors) and will be fixed in a follow-up DR.

## Consequences
- AI-generated text is always distinguishable in the library, even when final proposals don't distinguish it.
- Span-level tracking adds tooling cost. It stays optional until the pilot shows it's needed.

## Open questions
- Which other "dimensions over strings" matter beyond authorship: fact assertions, sensitivity, funder-specific adaptation, approval state?
- How to handle text whose author is a partner org but whose drafter was Hyphae staff?

## Revisions
