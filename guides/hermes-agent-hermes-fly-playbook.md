# Hermes Agent + hermes-fly Playbook

A practical operator guide for using NousResearch/hermes-agent and alexfazio/hermes-fly effectively.

## 1) What to use each project for

- Hermes Agent (`NousResearch/hermes-agent`): the agent runtime itself (CLI + messaging gateway + tools + memory + delegation + MCP).
- hermes-fly (`alexfazio/hermes-fly`): deployment and operations wrapper for running Hermes Agent on Fly.io.

Think of it as:
- Hermes Agent = the brain/runtime
- hermes-fly = hosted deployment and ops rails

## 2) Hermes Agent: high-value capabilities to lean on

- Broad native tool ecosystem: terminal/process, browser, web, vision, TTS, memory/session recall, delegation, execute_code, cron, MCP.
- Multi-backend execution environments for safer or more portable runs (local/docker/ssh/modal/daytona, etc.).
- Persistent memory and session search for long-horizon workflows.
- Delegation for reasoning-heavy branches and parallel sub-work.
- `execute_code` for multi-step mechanical tool orchestration with lower context bloat.

## 3) Hermes Agent best practices and tricks

1. Use persistent project guidance files
- Keep AGENTS.md / SOUL.md / repo rules up to date.
- Hermes loads these at session start, which dramatically improves consistency.

2. Separate “thinking” from “plumbing”
- Use delegate_task for reasoning-heavy or parallelizable subtasks.
- Use execute_code for repetitive tool-call pipelines.

3. Query session memory with OR-heavy searches
- Prefer queries like `term1 OR term2 OR term3`.
- This avoids narrow matching and improves recall hit-rate.

4. Compress before context collapse
- Use `/compress` proactively on long sessions.
- Keep active objectives in concise todos to survive compression.

5. Use safer execution backends for untrusted work
- Prefer docker/daytona/modal-style isolation when handling unknown code.
- Do not run risky scripts directly in local backend unless necessary.

6. Treat optional tools as optional
- Some tool modules require extras/API keys and may be unavailable until configured.
- Verify tool availability early in workflows that depend on them.

## 4) hermes-fly best practices and tricks

1. Treat preflight checks as mandatory signal
- Let the deploy wizard run full prereq/auth/network validation.
- Fix warnings first rather than pushing through and debugging later.

2. Use per-app targeting for multi-env ops
- Use `-a <app>` to avoid operating on wrong deployment.
- Keep one app per environment (dev/staging/prod pattern).

3. Prefer deterministic CI behavior
- Use `--no-auto-install` (or env equivalent) in CI.
- Preinstall dependencies in CI images for reproducibility.

4. If health checks fail after deploy, debug in place
- hermes-fly preserves resources in some post-deploy failure paths.
- Use `logs` + `doctor` before re-deploying to avoid losing evidence.

5. Keep names collision-safe
- Generated names are practical; custom names should be checked for global Fly uniqueness.

6. Install `jq` for better model/provider UX
- Without `jq`, model selection may fall back to less dynamic behavior.

## 5) Known caveats to account for

Hermes Agent caveats:
- Some docs note native Windows limitations; WSL2 is commonly recommended.
- Dangerous command approval behavior differs by backend; isolation posture matters.
- Certain features are dependency-gated (extras/modules/API keys).

hermes-fly caveats:
- Messaging docs/commands may drift from implementation over time (verify current CLI behavior).
- macOS/Linux-focused; Linux auto-install assumptions are strongest for apt-based distros.
- Secrets handling model differs between local metadata and runtime env materialization on host.

## 6) Recommended production operating model

1. Local design + test
- Build and validate workflow in local Hermes first.

2. Harden prompts/instructions
- Add explicit constraints, fallback behavior, and validation gates.

3. Stage on Fly
- Deploy with hermes-fly to staging app.
- Run smoke tests, then longer multi-step regression scenarios.

4. Production rollout
- Promote same config shape to prod app.
- Monitor logs and maintain rollback path.

5. Continuous improvement loop
- Capture failure examples.
- Update playbooks/skills/prompts.
- Re-test with baseline comparisons.

## 7) Suggested awesome-list short descriptions

- Hermes Agent: Open-source autonomous AI agent runtime with extensive tool integrations, persistent memory, delegation, MCP support, and multi-environment execution backends.
- hermes-fly: Fly.io deployment and operations CLI for Hermes Agent, with preflight validation and practical deploy/status/logs/doctor/destroy workflows.
