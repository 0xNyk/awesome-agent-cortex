# Claude Code Starter Configs

Curated starter configurations for [Claude Code](https://docs.anthropic.com/en/docs/claude-code), extracted and adapted from battle-tested community sources. These templates give you a solid foundation for configuring Claude Code in any project.

## Primary Source

These configs are adapted from [everything-claude-code](https://github.com/affaan-m/ECC), a comprehensive collection of Claude Code configurations, patterns, and best practices contributed by the community.

## How to Use

1. **Copy what you need** from this folder into your project
2. Place `CLAUDE.md` in your project root (or `.claude/CLAUDE.md`)
3. Place `AGENTS.md` in your project root for agent orchestration guidance
4. Drop rule files into `.claude/rules/`
5. Drop hook scripts into `.claude/hooks/`
6. Drop skill files into `.claude/skills/`

Customize each file for your specific project -- the templates include placeholder sections marked for you to fill in.

## Contents

### `CLAUDE.md` - Project Memory Template

The primary configuration file for Claude Code. This is where you define your project's tech stack, architecture, key commands, coding conventions, and development guidelines. Claude Code reads this file at the start of every session to understand your project context.

### `AGENTS.md` - Agent Orchestration Guide

A guide for structuring multi-agent workflows with Claude Code. Defines core principles (TDD, security-first, plan-before-execute), orchestration patterns for delegating work to subagents, and a set of universally applicable agent definitions (Planner, Reviewer, Security Reviewer, Doc Updater).

### `rules/` - Drop-in Rule Files

Modular rule files for `.claude/rules/`. Each file targets a specific concern (e.g., git conventions, testing requirements, security policies). Rules are automatically loaded by Claude Code when present in the `.claude/rules/` directory.

### `hooks/` - Event-Driven Automation

Hook scripts that run in response to Claude Code events (e.g., pre-commit checks, post-edit validation). These automate repetitive quality gates without manual intervention.

### `skills/` - Slash-Command Skills

Custom skill files that extend Claude Code with project-specific slash commands. Skills encapsulate common workflows (e.g., `/deploy`, `/review`, `/migrate`) into reusable, invocable actions.
