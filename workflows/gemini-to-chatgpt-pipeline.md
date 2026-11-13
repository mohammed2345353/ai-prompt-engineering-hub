# Multi-model pipeline: Gemini builds, ChatGPT delivers

The working split keeps substantial programming with Gemini and uses ChatGPT
for execution, checks, file handling, and GitHub delivery. Google Drive is the
shared source and artifact location.

## Steps

1. Prepare the project brief and source index in Google Drive.
2. Gemini reads the sources, designs and implements the solution, writes tests,
   and delivers complete, versioned files plus a manifest.
3. ChatGPT retrieves that exact artifact, runs focused checks, and sends any
   reproducible programming failures back to Gemini.
4. ChatGPT organizes accepted files and handles GitHub branches and delivery.
5. Record the artifact version, checks, commit, links and next owner in Drive.

ChatGPT does not generate a competing full implementation by default.
Never mark a Gemini delivery, Drive save, test, or GitHub upload complete
without the actual artifact or result. This workflow is coordinated through
files; it does not itself connect or automate the accounts.

See [the detailed handoff agreement](gemini-build-chatgpt-delivery.md) and
[the Arduino example](../examples/arduino-energy/README.md).
