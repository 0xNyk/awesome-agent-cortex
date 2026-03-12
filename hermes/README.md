# Hermes Hub

Practical, repo-local knowledge base for running and contributing to Hermes Agent.

This folder is curated from official sources plus operator-oriented synthesis.
If any guidance here conflicts with upstream docs, treat upstream as canonical.

## What is Hermes Agent?

Hermes Agent is an open-source autonomous AI agent runtime from Nous Research.
Core traits called out by upstream:
- persistent memory + user profile across sessions
- skill system (procedural memory)
- tool-use with terminal/file/web/browser/process orchestration
- subagent delegation and parallel task execution
- multi-platform gateway (CLI + messaging)
- built-in cron scheduling

## Folder map

- [01-quickstart.md](01-quickstart.md)
  - install, first run, day-1 commands
- [02-configuration-and-providers.md](02-configuration-and-providers.md)
  - config model/provider setup, terminal backends, env vars
- [03-memory-skills-automation.md](03-memory-skills-automation.md)
  - memory model, skills lifecycle, cron workflows
- [04-dev-and-contrib.md](04-dev-and-contrib.md)
  - contributor setup and architecture orientation
- [references.md](references.md)
  - upstream links used for this hub

## Scope notes

This hub is intentionally implementation-aware (commands, paths, workflows) and
operator-focused (what to run, what to verify, what to avoid).
