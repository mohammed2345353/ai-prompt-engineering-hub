# 🔄 Multi-Model Pipeline: Gemini + ChatGPT

## Overview
Combine the strengths of **Google Gemini** (massive context window & multimodal ingestion) with **ChatGPT** (structured code refinement & Canvas editing).

## Step-by-Step Workflow
1. **Ingest & Extract (Gemini):** Upload raw PDFs, logs, or transcripts to Gemini using `gemini-prompts/long-context-analyzer.md` to extract clean structured tables and facts.
2. **Architect & Refine (ChatGPT):** Feed the extracted structured summary into ChatGPT using `chatgpt-prompts/chain-of-thought-architect.md` inside **Canvas** to generate clean code or documentation.
3. **Version Control (GitHub):** Commit both the prompt templates and final outputs into your repository.
