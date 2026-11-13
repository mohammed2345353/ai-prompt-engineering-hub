# Arduino energy monitor workflow example

This example applies the prompt library to the user's Arduino UNO R3 project.
It is a programming brief and delivery workflow; it contains no finished firmware.

| Responsibility | Owner |
| --- | --- |
| Substantial programming, design, tests and programming fixes | Gemini |
| Focused checks, files and GitHub delivery | ChatGPT |
| Shared sources, artifacts and status | Google Drive |

Use [the shared workflow](../../workflows/gemini-build-chatgpt-delivery.md),
[the project brief](project-brief.md),
[Gemini's assignment](../../gemini-prompts/arduino-heavy-build.md), and
[ChatGPT's delivery assignment](../../chatgpt-prompts/arduino-delivery-review.md).

In Drive, these are named `00_WORKFLOW.md`, `01_PROJECT_BRIEF.md`,
`02_GEMINI_BUILD_REQUEST.md`, `03_HANDOFF_STATUS.json`,
`04_SOURCE_INDEX.md`, and `05_CHATGPT_DELIVERY_REQUEST.md`.

Start with Gemini's assignment. Return to ChatGPT only when an actual versioned
artifact or a concise question needs processing. The sensor is not purchased,
so measured energy is not a completed feature. Do not overwrite the brief
with an assistant's proposed parts list.

The live handoff status and private source index live in Drive. Personal links
and generated firmware archives are not duplicated into this example folder.
