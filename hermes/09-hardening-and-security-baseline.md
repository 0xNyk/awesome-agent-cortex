# Hermes Hardening and Security Baseline

Baseline controls for running Hermes in persistent/local/VPS environments.

## Threat model (practical)

Assume all of the following are possible:
- accidental secret exposure in logs or committed files
- unintended shell/tool execution from overly broad prompts
- gateway abuse via unauthorized chats/users
- config drift that weakens safety posture over time

Goal: reduce blast radius, not pretend zero risk.

## Baseline controls (minimum)

1) Principle of least privilege
- run Hermes with a non-root user
- limit filesystem scope to explicit working directories
- avoid broad sudo access in automation flows

2) Secret hygiene
- keep API keys in `~/.hermes/.env` or platform secret manager
- never commit secrets to repo
- rotate tokens after incident or suspected leakage

3) Approval and guardrails
- keep approval policy enabled for risky terminal actions
- require explicit user confirmation for destructive operations
- prefer recommendation-only mode for memory cleanup before deletions

4) Dependency trust
- pin critical dependencies where possible
- update intentionally, not ad hoc
- run diagnostics after upgrades

5) Auditability
- keep issue/PR links for operational fixes
- preserve incident notes with minimal repro and remediation
- convert repeated incidents into skills/runbooks

## Environment hardening profile

## A) Local workstation
- use dedicated shell profile for Hermes env vars
- ensure shell history does not leak secrets
- separate personal and operator repos where possible

## B) VPS / headless
- systemd service with restart policy
- strict file permissions on config/log dirs
- network exposure minimized (no unnecessary ports)
- keep gateway tokens in environment, not plaintext scripts

## C) Isolated executor host
- short-lived workers when possible
- restricted outbound network policy
- ephemeral temp dirs and cleanup after job completion

## Messaging/gateway hardening

1) Restrict allowed chat/user IDs
2) Verify delivery targets before enabling automated cron output
3) Set `MESSAGING_CWD` to a safe explicit directory
4) Restart gateway after config/token changes
5) Monitor for repeated failed auth/command attempts

## Incident response playbook (security-relevant)

1) Contain
- pause cron jobs and gateway if active abuse suspected
- revoke/rotate potentially exposed credentials

2) Assess
- identify affected providers, tools, and repos
- collect exact timestamps and command evidence

3) Eradicate
- patch root cause with smallest safe change
- remove leaked artifacts/history where needed

4) Recover
- restore services gradually (CLI first, gateway second, cron last)
- monitor for recurrence across one full workflow cycle

5) Learn
- add/update runbook and skill guardrails
- document permanent control changes

## Verification checklist

Run after setup or major changes:

```bash
hermes doctor
hermes model
hermes tools
```

Then validate:
- no secrets in tracked files
- gateway accepts only intended chats
- one representative automation run succeeds with expected approvals

## Security anti-patterns to avoid

- running production Hermes as root
- broad wildcard execution prompts with no approval gate
- committing `.env` files or credentials in markdown examples
- enabling messaging automation before authorization scoping is verified
- skipping post-upgrade diagnostics
