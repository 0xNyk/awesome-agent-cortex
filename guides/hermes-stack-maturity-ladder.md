# Hermes Stack Maturity Ladder (L1 -> L3)

Use this to assess how production-ready your Hermes setup is and what to improve next.

## Level 1 — Hobby / Solo Exploration

Typical profile:
- One user, ad-hoc tasks, minimal guardrails
- Mostly local runs
- Limited repeatability

Minimum setup:
- Hermes installed and usable from CLI
- Basic provider/API key configuration
- Project has a lightweight AGENTS.md

Common risks:
- Prompt drift and inconsistent behavior
- No rollback discipline
- Secrets/config sprawl

Upgrade path to L2:
- Introduce a standard quickstart/runbook
- Track tasks with explicit plans/todos
- Add basic deployment + health checks

## Level 2 — Team / Shared Workflow

Typical profile:
- Multiple users/projects
- Repeated workflows and playbooks
- Some hosted usage (e.g., Fly)

Minimum setup:
- Standardized project guidance files (AGENTS.md, conventions)
- Shared recipes for local + hosted operations
- Basic observability loop (logs, doctor checks, recurring review)
- Branch protection and PR norms for repo changes

Recommended controls:
- One deployment per environment (dev/staging/prod)
- Documented fallback behavior for tool/API failures
- Session hygiene (`/compress`, concise objectives, planned tasks)

Common risks:
- Drift between docs and real operations
- Environment mismatch across teammates
- Missing post-deploy verification

Upgrade path to L3:
- Formalize security posture and least-privilege defaults
- Add deterministic CI/CD path
- Add regression suites for critical workflows

## Level 3 — Production / Reliable Operations

Typical profile:
- Customer-facing or mission-critical workloads
- Predictable SLO-minded operations
- Continuous improvement loop from incidents/failures

Minimum setup:
- Hardened execution backends for risky workloads
- Strong secrets management and rotation process
- CI-backed deployment with reproducible config
- Structured incident response + rollback playbook
- Baseline comparisons for quality/cost/performance over time

Operational excellence checklist:
- Explicit change management for prompts/skills/playbooks
- Golden-path regression tasks run after major updates
- Failure taxonomy with remediation ownership
- Measured success metrics (quality, latency, cost, error rates)

Common risks:
- Over-complex tool surface without governance
- Hidden dependency failures in optional modules
- Runaway token/tool cost without instrumentation

## Fast self-assessment rubric

Score each 0-2 (0=no, 1=partial, 2=strong):
- Repeatability (same input -> similar output quality)
- Safety controls (isolation, approvals, least privilege)
- Observability (logs, diagnostics, known failure patterns)
- Deployment discipline (versioned, tested, rollback-ready)
- Cost/performance control (tracked and improved)

Interpretation:
- 0-3: L1
- 4-7: L2
- 8-10: L3

## Recommended next action by level

- L1: Adopt quickstart recipes + project AGENTS.md baseline.
- L2: Standardize deployment and diagnostics; add lightweight regression checks.
- L3: Optimize for reliability economics (quality x latency x cost) with continuous audits.

## Companion docs

- [Hermes Stack Quickstart Recipes](hermes-stack-quickstart-recipes.md)
- [Hermes Agent + hermes-fly Best Practices](hermes-agent-hermes-fly-playbook.md)
