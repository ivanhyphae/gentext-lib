# 0013. Rename the project to adapt-rfp

- Status: Accepted (2026-09-25)
- Date: 2026-09-25
- Deciders: Ivan Heitmann; Claude (drafting)

## Context
The repo was `gentext-lib`, with a CLI and package called `gentext`. The maintainer felt the name should say what the thing is and does. "gentext" reads as a text generator, which is the part the project deliberately keeps narrow. The core function is **converting existing material into new material that meets a solicitation's standard**. Rejected candidates: `proposal-library` (names the store, not the job), `proposal-pipeline` ("pipeline" means an opportunity tracker in business development), `adaptive-reuse` (sounds like an environmental engineering project), `proposal-tailor`/`recast`/`refit`.

## Decision
- Repo **`adapt-rfp`**, Python package **`adapt_rfp`** (`src/adapt_rfp/`), CLI **`adapt-rfp`**.
- It intentionally sits alongside Hyphae's **AdaptOS** brand, as a product family.
- The README's one-line description ("Adapt Hyphae's existing proposal writing to the standard a new solicitation sets…") heads off the reading "adapt *the* RFP". "RFP" is used loosely to cover NOFAs, grant applications and qualifications.

## Consequences
- Every in-repo reference was updated in one commit, including decision records and research pages, so docs match the code. Commit messages before this record still say `gentext`.
- The maintainer renames the GitHub repository (GitHub redirects the old URL) and updates the cloud environment. Renaming the local folder is optional.

## Revisions
