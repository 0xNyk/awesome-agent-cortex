<!--
  AGENTS.md -- Starter Template for OpenAI Codex CLI

  This is a generic template. Customize every section below for your project.
  Place this file in your project root so Codex CLI reads it at session start.

  Sections marked with [brackets] are placeholders -- replace them with your
  project-specific details.

  Reference: https://github.com/openai/codex
-->

# Project Instructions

> These instructions are read by Codex CLI at the start of every session.

## Project Overview

[Brief description of your project -- what it does, who it is for, and its current stage.]

## Tech Stack

[List your languages, frameworks, databases, and key dependencies.]

- Language: [e.g., TypeScript, Python, Rust]
- Framework: [e.g., Next.js, FastAPI, Axum]
- Database: [e.g., PostgreSQL, SQLite, none]
- Package manager: [e.g., pnpm, uv, cargo]

## Architecture

[Describe your project structure and key patterns.]

```
[project-root]/
  src/          -- [source code]
  tests/        -- [test files]
  docs/         -- [documentation]
  ...
```

## Key Commands

[List common dev commands. Replace placeholders with your actual commands.]

- Build: `[your build command]`
- Test: `[your test command]`
- Lint: `[your lint command]`
- Format: `[your format command]`
- Dev server: `[your dev command]`
- Type check: `[your type check command]`

## Development Guidelines

- Follow existing code patterns and conventions
- Write tests for all new functionality
- Use conventional commits (feat:, fix:, docs:, test:, refactor:, chore:)
- Never commit secrets, credentials, or .env files
- Prefer editing existing files over creating new ones
- Make minimal, focused changes -- do not refactor unrelated code
- Delete dead code rather than commenting it out

## Code Style

[Language-specific style rules. Examples:]

- [Use 2-space indentation for TypeScript, 4-space for Python]
- [Prefer named exports over default exports]
- [Use descriptive variable names -- no single-letter names except loop counters]
- [Formatting tool: prettier / black / rustfmt]
- [Linting tool: eslint / ruff / clippy]

## Testing Strategy

[Describe your testing approach.]

- [Unit tests for business logic]
- [Integration tests for API endpoints]
- [Minimum coverage requirement: X%]
- [Test runner: jest / pytest / cargo test]
- [Test naming convention: describe what is being tested and the expected outcome]

## Important Files

[List key files and their purposes.]

- `[path/to/config]` -- [configuration file for X]
- `[path/to/entry]` -- [application entry point]
- `[path/to/schema]` -- [database schema / API schema]

## Common Pitfalls

[Known gotchas or things to watch out for.]

- [e.g., Environment variables must be prefixed with NEXT_PUBLIC_ to be available client-side]
- [e.g., Database migrations must be run before tests]
- [e.g., The CI pipeline runs on Node 20 -- do not use Node 22 features]
