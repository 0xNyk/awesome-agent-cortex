# Hermes Runtime Comparison Matrix

High-level operator comparison for commonly used agent runtimes.
Purpose: quick routing and stack selection, not absolute ranking.

## Scope

Compared stacks:
- Hermes Agent
- Claude Code
- OpenAI Codex CLI
- OpenHands
- Goose

## Matrix (operator view)

| Dimension | Hermes Agent | Claude Code | Codex CLI | OpenHands | Goose |
|---|---|---|---|---|---|
| Primary mode | General autonomous agent runtime | Coding-focused CLI agent | Coding-focused CLI agent | SWE automation platform | Dev-agent CLI/runtime |
| Built-in persistent memory model | Yes (memory + user profile) | Limited/session-oriented memory files | Limited/session-oriented | Platform/task oriented | Varies by setup |
| Skill/procedural memory system | Yes (first-class skills lifecycle) | Prompt/memory workflows | Prompt/workflow patterns | Repo task workflows | Tool/workflow oriented |
| Multi-platform messaging gateway | Yes | No | No | Not primary focus | Not primary focus |
| Built-in cron/scheduling | Yes | No | No | External orchestration | External orchestration |
| Subagent delegation | Yes | Pattern-based | Pattern-based | Multi-agent task patterns | Pattern-based |
| Tool extensibility breadth | Broad (toolsets + MCP + terminal/file/web/browser/etc.) | Strong coding/tool loop | Strong coding/tool loop | Strong for SWE automation | Strong for dev workflows |
| Best-fit use case | Always-on personal/company operator agent | Interactive code tasks in repo | Interactive code tasks in repo | End-to-end software task execution | Terminal-native dev automation |

## Decision heuristics

Choose Hermes when you need:
- one runtime spanning CLI + messaging + automation
- durable memory and reusable procedural skills
- scheduled autonomous operations with delivery targets

Choose coding-first stacks when you mainly need:
- direct repo-centric code generation/refactor/debug loops
- minimal non-coding orchestration requirements

## Hybrid pattern that works well

- Hermes as control plane (memory, scheduling, multi-channel interface)
- coding-focused agents as specialized executors per task

This gives you broad operational continuity plus high-velocity code execution.

## Caveat

Feature sets evolve rapidly. Re-check official docs before committing to long-term architecture decisions.
