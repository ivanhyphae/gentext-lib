# 0001. Record architecture decisions

- Status: Accepted
- Date: 2026-09-25
- Deciders: Ivan Heitmann; Claude (drafting)

## Context
`adapt-rfp` is being designed collaboratively by humans and LLM agents across many sessions. Agents lose context between sessions, and human colleagues will join later. The README leaves the implementation plan "TBD in collaboration with llm agent and human colleagues".

## Decision
Keep lightweight, numbered decision records in `documentation/decision-record/`. Use the template and process in that folder's `README.md`. Records start as *Proposed* and become *Accepted* only after a human agrees. Superseded records stay in place.

## Consequences
- Agents can rebuild the design rationale by reading the index and the relevant records. `AGENTS.md` points them here.
- There is a small overhead per decision. We accept it.

## Alternatives considered
- Decisions in README only: loses the reasoning and the history.
- Decisions in Claude Docs / Notion: harder for coding agents to read, and they drift from the code. Those surfaces can still be used for discussion, with outcomes landing here.

## Revisions
