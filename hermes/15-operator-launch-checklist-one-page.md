# Hermes Operator Launch Checklist (One Page)

Use this as a go/no-go checklist before opening Hermes to real usage.

Target time: 20-30 minutes.

## 1) Preflight

- [ ] Host is stable (local/VPS/container) and time sync is correct
- [ ] Hermes installed and executable
- [ ] Working directory exists and is writable
- [ ] Non-root runtime user configured for persistent deployments

Quick checks:

```bash
hermes --version
hermes doctor
```

## 2) Secrets and config

- [ ] Provider API key(s) set in secure env location
- [ ] No secrets in git-tracked files
- [ ] `MESSAGING_CWD` explicitly set
- [ ] Active model/provider selected and tested

Quick checks:

```bash
hermes model
hermes tools
```

## 3) Safety baseline

- [ ] Approval policy enabled for risky operations
- [ ] Destructive actions require explicit confirmation
- [ ] Access scope limited to intended paths/channels
- [ ] No wildcard/high-risk automation enabled yet

## 4) Gateway (if enabled)

- [ ] Platform token valid
- [ ] Chat/channel/user allowlist configured
- [ ] Gateway process managed by systemd/supervisor/docker (not ad-hoc shell)
- [ ] `/start` + simple prompt pass in test channel

## 5) Automation (if enabled)

- [ ] Existing cronjobs reviewed (`list_cronjobs`)
- [ ] No high-risk jobs enabled before smoke tests
- [ ] Delivery targets verified (origin/local/platform)
- [ ] One low-risk scheduled task executed successfully

## 6) Smoke tests

Run all 4 before launch:

- [ ] basic prompt response
- [ ] tool-light task response
- [ ] formatting-sensitive response (markdown/code block)
- [ ] restart/recovery test (process restart then prompt succeeds)

## 7) Observability and recovery

- [ ] You know where logs live and how to read them
- [ ] Restart command documented
- [ ] Backup path documented for Hermes state/config
- [ ] Incident owner/on-call contact defined (even if just you)

## 8) Launch gate

You are launch-ready only if:

- [ ] doctor clean (or known warnings documented)
- [ ] smoke tests 4/4 green
- [ ] gateway auth scope verified (if used)
- [ ] rollback plan documented

## 9) First 24h post-launch checks

- [ ] check logs after first real interactions
- [ ] check failure rate and unexpected tool calls
- [ ] validate no secret leakage
- [ ] capture one improvement item in runbook

If any critical check fails, pause rollout and use 08-troubleshooting-decision-tree.md.
