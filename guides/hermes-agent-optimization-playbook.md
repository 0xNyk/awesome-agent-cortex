# Hermes Agent Optimization Playbook

Operator patterns for improving Hermes Agent quality, speed, and reliability in real workflows.

## 1) Context architecture

Use persistent files intentionally:
- AGENTS.md for project rules/process
- SOUL.md for persona/tone consistency
- memory store for durable environment and user preferences

Tips:
- Keep AGENTS.md concise and testable.
- Move bulky references into docs and point to them.
- Use `/compress` before long tool-heavy phases.

## 2) Delegation vs execute_code

Use `delegate_task` for:
- reasoning-heavy analysis
- parallel independent subtasks
- context-heavy investigations where only summary is needed

Use `execute_code` for:
- mechanical multi-call tool loops
- filtering/reducing large outputs
- conditional branching with deterministic script logic

Rule of thumb:
- cognitive split -> delegate
- mechanical split -> execute_code

## 3) Memory hygiene

Write memory only when durable:
- user preferences
- environment facts
- resolved tricky workflows likely to recur

Avoid memory bloat:
- skip transient logs/dumps
- consolidate when usage gets high
- prefer session_search for historical recall

## 4) Tool-use optimization

- Prefer direct tool calls for simple operations.
- Batch independent checks in parallel where possible.
- Keep terminal for shell-native work only (build/test/git/process).
- Use file/search tools instead of shell grep/cat equivalents.

## 5) Security and isolation

- For risky code paths, prefer isolated backends (container/remote) over local execution.
- Require explicit approval for destructive operations.
- Minimize toolset exposure for delegated subtasks.
- Keep secrets out of prompts and repo files.

## 6) Reliability loops

Use a repeatable loop:
1. Plan via todo list
2. Execute smallest safe step
3. Verify with objective checks
4. Update plan state
5. Summarize and persist only key learnings

For long-running work:
- checkpoint with concise summaries
- re-anchor goal/constraints every few iterations

## 7) Performance checklist

- [ ] AGENTS.md scoped and current
- [ ] Prompt/context minimized to relevant files
- [ ] Correct split between delegate_task and execute_code
- [ ] Memory writes are durable and concise
- [ ] Verification step after each material change
- [ ] Clear stop criteria and rollback plan

## 8) Common failure modes

- Too much context loaded too early
- Delegating tasks without enough context payload
- Using execute_code for tasks needing semantic judgment
- Over-saving memory and hitting store limits

Fixes:
- progressive context loading
- richer delegation briefs (paths/errors/success criteria)
- mode-correct tool choice
- memory consolidation discipline

## 9) Canonical references

- Hermes docs root: https://github.com/NousResearch/hermes-agent/tree/main/website/docs
- Tips: https://github.com/NousResearch/hermes-agent/blob/main/website/docs/guides/tips.md
- Context files: https://github.com/NousResearch/hermes-agent/blob/main/website/docs/user-guide/features/context-files.md
- Delegation: https://github.com/NousResearch/hermes-agent/blob/main/website/docs/user-guide/features/delegation.md
- Code execution: https://github.com/NousResearch/hermes-agent/blob/main/website/docs/user-guide/features/code-execution.md
- Memory: https://github.com/NousResearch/hermes-agent/blob/main/website/docs/user-guide/features/memory.md
