# Hermes Stack Quickstart Recipes

Copy/paste-oriented recipes for running Hermes Agent and hermes-fly in common setups.

## 1) Local development (fast start)

Goal: get a local Hermes CLI session running quickly.

```bash
# Install Hermes Agent
curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash

# Start interactive agent
hermes
```

Tips:
- Keep a project-level `AGENTS.md` for persistent instructions.
- Add API keys/provider config before tool-heavy workflows.

## 2) Local development (project-aware)

Goal: run Hermes in a repo with stable behavior across sessions.

```bash
cd /path/to/your/repo

# Optional but recommended project guidance file
cat > AGENTS.md <<'EOF'
# Project Rules
- Use concise commit messages
- Run tests before finalizing
- Prefer minimal focused edits
EOF

hermes
```

Tips:
- Use `/compress` when sessions get long.
- Use `todo` planning for multi-step tasks.

## 3) Hosted deployment on Fly.io (hermes-fly)

Goal: deploy a managed Hermes instance quickly.

```bash
# Install hermes-fly
curl -fsSL https://raw.githubusercontent.com/alexfazio/hermes-fly/main/scripts/install.sh | bash

# Interactive deploy
hermes-fly deploy

# Inspect deployment
hermes-fly status
hermes-fly logs
```

Tips:
- Keep one app per environment (dev/staging/prod).
- Use `-a <app>` when operating multiple apps.

## 4) Production hardening recipe

Goal: safer runtime posture and more predictable operations.

Checklist:
- Prefer isolated execution backends for untrusted code paths.
- Enforce branch protections and CI checks in repos Hermes touches.
- Keep secrets in platform secret manager (not committed files).
- Add explicit validation gates in prompts/skills/playbooks.
- Monitor logs + run health checks after every deploy.

Minimal ops loop:

```bash
hermes-fly status
hermes-fly doctor
hermes-fly logs
```

## 5) CI/non-interactive deployment pattern

Goal: reproducible deployment behavior in CI.

```bash
# Ensure dependencies are preinstalled in CI image
# then run deploy without auto-install side effects
hermes-fly deploy --no-auto-install
```

Tips:
- Pin versions for repeatability.
- Run smoke checks immediately post-deploy.

## 6) Secure-mode workflow for risky tasks

Goal: reduce risk when running unknown scripts/code.

Pattern:
1. Route risky execution to isolated backend.
2. Minimize granted tools/permissions.
3. Validate outputs before applying changes.
4. Keep rollback path (git clean branch, backups, snapshots).

## 7) Performance workflow (cost + latency)

Goal: reduce token/tool overhead while keeping quality.

Pattern:
- Delegate reasoning-heavy subtasks (`delegate_task`).
- Use `execute_code` for mechanical tool pipelines.
- Keep instructions compact; move deep references to separate docs.
- Use OR-style session search queries for better recall hit-rate.

## 8) Day-2 operations runbook

Daily/weekly checks:
- Validate provider/API key health.
- Review failed runs and recurring errors.
- Update playbooks from real failure examples.
- Re-run core golden-path tasks after any major config change.

## 9) Troubleshooting quick map

- Deploy failed early: rerun with preflight fixes first.
- Deploy succeeded, service unhealthy: inspect logs + doctor before destroy/redeploy.
- Tool unavailable: verify extras/dependencies and credentials.
- Session quality degraded: compress, prune noise, restart with tighter task plan.

## 10) Recommended companion docs

- [Hermes Agent + hermes-fly Best Practices](hermes-agent-hermes-fly-playbook.md)
- Hermes Agent repo: https://github.com/NousResearch/hermes-agent
- hermes-fly repo: https://github.com/alexfazio/hermes-fly
