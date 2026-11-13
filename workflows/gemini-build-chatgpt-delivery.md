# Gemini builds; ChatGPT validates and delivers

## Ownership

| Party | Work |
| --- | --- |
| Gemini | Analyze sources, design the solution, write substantial code and tests, document the build, and fix programming failures. |
| ChatGPT | Prepare a concise brief, retrieve delivered files, run focused checks, organize the repository, and handle GitHub delivery. |
| Google Drive | Keep shared sources, handoff files, versioned outputs, and delivery status. |
| User | Confirm hardware, approve unresolved design choices, and run physical tests. |

ChatGPT does not rewrite Gemini's implementation merely to produce a second
version. It returns a short failure report to Gemini when code needs changes.
Passing a compilation check does not prove that the circuit works.

## Handoff files in Drive

1. `00_WORKFLOW.md`: this agreement.
2. `01_PROJECT_BRIEF.md`: confirmed facts, constraints, and open questions.
3. `02_GEMINI_BUILD_REQUEST.md`: the programming assignment.
4. `03_HANDOFF_STATUS.json`: current owner and artifact status.
5. `04_SOURCE_INDEX.md`: links to the actual sources, kept in Drive.

Gemini delivers a versioned ZIP and a manifest listing the generated files,
dependencies, build command, tests actually run, and unresolved questions.
Use a new version for revised deliveries; retain prior versions.

If Gemini cannot read Drive, attach the brief and sources or paste their
contents. If it cannot write Drive, it must provide a downloadable artifact
and say that it has not saved it. ChatGPT or the user can then save the bytes
to the same Drive folder. No assistant should claim a save it did not perform.

## Status transitions

`READY_FOR_GEMINI` -> `GEMINI_DELIVERED` -> `CHATGPT_CHECKING`
-> `FIXES_REQUESTED` or `READY_FOR_GITHUB` -> `GITHUB_DELIVERED`.

Set `GEMINI_DELIVERED` only after an actual artifact is available. Record the
exact Drive file ID/version and checksum before checks. ChatGPT records the
checks it ran and their results. Missing hardware remains an explicit limit.

ChatGPT handles GitHub branches, commits and pull requests. Gemini does not
push, merge, change sharing, or replace the repository. Keep personal source
documents, private Drive links, credentials, and device logs out of public
commits. Public examples contain only the project brief and reusable prompts.

This is a coordinated workflow, not an automatic connection between accounts.
