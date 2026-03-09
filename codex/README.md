# Codex CLI -- Starter Configs

Curated starter configurations for [OpenAI Codex CLI](https://github.com/openai/codex), the open-source CLI coding agent from OpenAI. Codex CLI runs locally on your machine and connects to OpenAI models (or other providers) to assist with coding tasks directly from your terminal.

## What is Codex CLI?

Codex CLI is an open-source, locally-running coding agent that lives in your terminal. It can read your codebase, propose changes, execute commands, and iterate -- all under your supervision. It is not a cloud service; it runs on your machine and calls model APIs as needed.

Source: <https://github.com/openai/codex>

## Contents

| File | Purpose | Where to put it |
|------|---------|-----------------|
| `AGENTS.md` | Project-level instructions template | Copy to your project root |
| `codex.json` | Codex CLI settings | Copy to your project root or `~/.codex/` |
| `global-instructions.md` | Global instructions (all projects) | Copy to `~/.codex/instructions.md` |

## How to Use

### 1. Project instructions (`AGENTS.md`)

Codex CLI reads an `AGENTS.md` file from your project root at the start of every session. This is the equivalent of `CLAUDE.md` for Claude Code or `.github/copilot-instructions.md` for Copilot.

```bash
cp codex/AGENTS.md /path/to/your/project/AGENTS.md
```

Open it and fill in the placeholder sections with your project-specific details.

### 2. Settings (`codex.json`)

The `codex.json` file controls Codex CLI behavior. Place it in your project root for per-project settings.

```bash
cp codex/codex.json /path/to/your/project/codex.json
```

#### Configuration fields

| Field | Description | Default |
|-------|-------------|---------|
| `model` | Which model to use for generation | `o4-mini` |
| `approval_mode` | How Codex asks for permission (see below) | `suggest` |
| `providers` | Provider configuration (e.g., OpenAI, custom endpoints) | OpenAI |
| `history.persistence` | Where to store conversation history (`global` or `project`) | `global` |
| `history.max_entries` | Maximum number of history entries to retain | `1000` |
| `notify` | Whether to send desktop notifications on completion | `true` |

#### Approval modes

Codex CLI has three approval modes that control how much autonomy the agent has:

- **`suggest`** -- Always asks before making any changes. The safest mode; recommended for getting started.
- **`auto-edit`** -- Automatically approves file edits but asks before running commands. Good for trusted projects where you want faster iteration on code changes.
- **`full-auto`** -- Automatically approves everything, including shell commands. Use with caution and only in sandboxed environments.

### 3. Global instructions (`global-instructions.md`)

These instructions apply to every project on your machine. Copy them to your Codex config directory:

```bash
mkdir -p ~/.codex
cp codex/global-instructions.md ~/.codex/instructions.md
```

## Tips

- Start with `suggest` mode until you are comfortable with how Codex CLI operates.
- Keep `AGENTS.md` concise. The model reads it every session, so avoid bloat.
- Use `AGENTS.md` files in subdirectories for module-specific instructions -- Codex CLI reads them hierarchically.
- Combine project-level `AGENTS.md` with global `~/.codex/instructions.md` for a layered instruction system.
