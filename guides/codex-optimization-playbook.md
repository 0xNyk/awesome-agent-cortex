# Codex Optimization Playbook

Practical operator guide for running Codex workflows with higher quality, lower latency, and stronger safety.

## 1) Choose the right operating mode

Interactive mode (local dev loops)
- Best for exploratory coding, debugging, and iterative refactors.

Non-interactive mode (`codex exec`)
- Best for CI, deterministic jobs, and repeatable transformations.

Rule:
- If you need reproducibility and machine evaluation, prefer non-interactive mode.

## 2) AGENTS.md strategy (highest leverage)

Use AGENTS.md to remove repeated instructions and stabilize behavior.

Recommended structure:
- Scope and objective
- Tech stack and conventions
- Required checks (lint/test/build order)
- Safety constraints (forbidden ops, secret handling)
- Completion criteria

Hierarchy behavior:
- Subdirectory AGENTS.md should narrow behavior for local components.
- Keep top-level policies concise and universal.

## 3) Instruction contract design

Use explicit, checkable contracts:
- output format/schema
- success criteria
- forbidden changes
- required evidence (tests, logs, diffs)

Bad: "Improve this code."
Good: "Refactor function X for readability without API changes; run tests A/B; provide diff summary and risk notes."

## 4) Speed and cost tuning

- Keep prompts/task scope narrow.
- Minimize irrelevant file context.
- Reuse stable instruction blocks (AGENTS.md + task templates).
- Prefer short iterative passes over one giant pass.
- Use fast mode/model for triage; higher-quality mode for final patch.

## 5) Safety and approvals

Define approval boundaries up front:
- read-only actions: auto-allow
- file writes/tests: allow with policy
- network, destructive ops, credential-sensitive paths: explicit approval

Always enforce:
- no secret exfiltration
- no unsafe shell commands
- no edits to protected files unless explicitly requested

## 6) Quality loop

Recommended loop:
1. Plan
2. Implement small scoped patch
3. Run narrow checks
4. Self-review diff
5. Run full checks if touched shared/core paths
6. Final human review for risky changes

## 7) CI pattern (`codex exec`)

Use codex exec for deterministic gates:
- fixed input prompt/instruction set
- pinned environment/toolchain
- captured logs and outputs as artifacts
- fail build on unmet acceptance criteria

## 8) Eval gates

Track per change set:
- task success
- test pass rate
- latency and token cost
- policy violations

Block release if:
- critical tests fail
- policy/safety checks fail
- regression beyond agreed threshold

## 9) Common failure modes

- Over-broad task scope -> noisy diffs
- Missing AGENTS.md constraints -> inconsistent style/quality
- No explicit acceptance criteria -> ambiguous done state
- No eval gates -> silent regressions

Mitigation: tighter contracts, scoped tasks, and hard CI gates.

## 10) Canonical references

- Codex docs: https://developers.openai.com/codex
- Codex CLI: https://developers.openai.com/codex/cli
- Codex non-interactive: https://developers.openai.com/codex/noninteractive
- AGENTS.md guide: https://developers.openai.com/codex/guides/agents-md
- Eval best practices: https://developers.openai.com/api/docs/guides/evaluation-best-practices
