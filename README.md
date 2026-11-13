# 🧠 AI Prompt Engineering Hub

A structured collection of advanced system prompts, long-context XML templates, reasoning workflows, and validation scripts for Google Gemini and ChatGPT.

Use Gemini for source analysis, solution design, substantial programming, tests, and programming fixes. Use ChatGPT for artifact retrieval, focused checks, repository organization, and GitHub delivery. Google Drive holds shared sources, versioned outputs, and handoff status. The templates are starting points to adapt and review for your own tasks.

## Repository structure

```text
ai-prompt-engineering-hub/
├── README.md
├── .gitignore
├── gemini-prompts/
│   └── long-context-analyzer.md
├── chatgpt-prompts/
│   ├── chain-of-thought-architect.md
│   ├── python-code-review.md
│   └── arduino-delivery-review.md
├── workflows/
│   └── gemini-to-chatgpt-pipeline.md
└── scripts/
    └── prompt_validator.py
```

## Templates and workflow

| File | Purpose |
| --- | --- |
| [Long-context analyzer](gemini-prompts/long-context-analyzer.md) | Extract five core concepts from attached documents, with page or section references. |
| [Technical architect](chatgpt-prompts/chain-of-thought-architect.md) | Organize technical requirements, constraints, trade-offs, and implementation output. |
| [Python code review](chatgpt-prompts/python-code-review.md) | Review the validator and explain evidence-backed findings in Iraqi Arabic for a beginner. |
| [Gemini → ChatGPT pipeline](workflows/gemini-to-chatgpt-pipeline.md) | Follow a manual document-extraction, refinement, and version-control workflow. |
| [Prompt validator](scripts/prompt_validator.py) | Check Markdown files for paired `<role>` and `<task>` tags. |

## Quick start

```bash
git clone https://github.com/mohammed2345353/ai-prompt-engineering-hub.git
cd ai-prompt-engineering-hub
```

1. Open a template in `gemini-prompts/` or `chatgpt-prompts/`.
2. Copy its XML-style instruction block into the relevant AI application.
3. Replace bracketed placeholders and attach any source documents required by the task.
4. Review the result and verify cited passages against the original sources.

For the combined workflow, follow [Gemini → ChatGPT pipeline](workflows/gemini-to-chatgpt-pipeline.md). It describes manual steps; this repository does not connect to either service or make API calls.

## Run the validator

Requires **Python 3.6 or later**. Only Python's standard library is used; no package installation or API keys are needed.

Run from the repository root:

```bash
python scripts/prompt_validator.py gemini-prompts/long-context-analyzer.md
python scripts/prompt_validator.py chatgpt-prompts/chain-of-thought-architect.md
python scripts/prompt_validator.py chatgpt-prompts/python-code-review.md
```

On Windows, `py` can be used instead of `python` when the Python launcher is installed.

| Exit code | Meaning |
| --- | --- |
| `0` | Both required paired tags were found. |
| `1` | An argument is missing, the file does not exist, or a required paired tag is missing. |

The validator uses regular expressions to check for `<role>...</role>` and `<task>...</task>`. It does **not** parse XML, validate nesting, check placeholders, or assess prompt quality. A `[PASS]` result only confirms those tag pairs are present. Workflow documents and this README are not prompt templates and need not pass this check.

## Practical limitations

- Prompt instructions cannot guarantee factual accuracy or eliminate hallucinations. Check source references and generated code independently.
- XML-style tags organize instructions; they do not enforce model behavior or reveal a model's private reasoning. Ask for concise explanations, assumptions, trade-offs, and verifiable results.
- The templates have no model-specific API dependencies. Available features and behavior depend on the AI application and model you use.
- Keep credentials and confidential source documents out of public commits. `.gitignore` excludes common local secrets and temporary files, but does not inspect file contents.

## Applied workflow: Arduino energy monitor

See [the Arduino example](examples/arduino-energy/README.md): Gemini owns
substantial programming and programming fixes; ChatGPT retrieves the files,
runs focused checks and handles GitHub delivery. Google Drive holds the
shared sources, versioned artifacts and handoff status.

The example includes [Gemini's programming assignment](gemini-prompts/arduino-heavy-build.md)
and [ChatGPT's delivery assignment](chatgpt-prompts/arduino-delivery-review.md).
It does not yet include finished Arduino firmware or a Gemini-generated build.

## Contributing

Keep prompt templates in the appropriate model folder and multi-model procedures in `workflows/`. Explain each template's use case, document placeholders, and run the validator on changed templates before proposing a pull request. Include an example of the intended output when useful.

## License

No license has been selected for this repository. Public availability alone does not grant an open-source license; contact the repository owner about reuse permissions.
