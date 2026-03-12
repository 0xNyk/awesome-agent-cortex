# Hermes Production Profiles

Copy/paste deployment profiles for common operating modes.

Assumptions:
- Hermes installed and on PATH
- `~/.hermes/config.yaml` and `~/.hermes/.env` exist
- API/provider credentials already set

## Profile A: Local Dev (fastest feedback)

Use when:
- you are iterating on prompts/skills/workflows
- low isolation risk (trusted repos and commands)

Suggested settings:
- terminal backend: local
- cwd: current project
- shorter timeout for tight loops

Baseline steps:

```bash
hermes model
hermes tools
hermes config set terminal.backend local
hermes
```

Operational notes:
- best ergonomics and speed
- least isolation; avoid unknown scripts/repos

## Profile B: VPS Operator (24/7 remote agent)

Use when:
- you want always-on automation
- you need durable remote sessions + gateway access

Suggested settings:
- run Hermes on a dedicated VM user
- systemd/tmux for process continuity
- cron jobs for recurring maintenance and reports

Baseline flow:

```bash
hermes setup
hermes gateway
hermes doctor
```

Operational notes:
- enable least-privilege Linux user
- route secrets via environment file only
- back up `~/.hermes/` regularly

## Profile C: Isolated Execution (higher safety)

Use when:
- untrusted repos or risky command surfaces
- regulated workflows requiring stronger boundaries

Suggested settings:
- terminal backend: docker/ssh/singularity
- explicit workspace root restrictions
- conservative toolset selection

Baseline flow:

```bash
hermes config set terminal.backend docker
hermes tools
hermes doctor
```

Operational notes:
- slower than local, but safer
- validate mounted paths and writable scope

## Profile D: Messaging-First Ops (chat-native control plane)

Use when:
- operating mostly from Telegram/Discord/Slack/etc.
- asynchronous command-and-control workflows

Suggested settings:
- gateway enabled and monitored
- clear MESSAGING_CWD policy
- notification and alert routing defined

Baseline flow:

```bash
hermes gateway
```

Operational notes:
- treat messaging channels as production interfaces
- apply strict access controls and chat authorization rules

## Security baseline for all profiles

- never commit `.env`
- keep dangerous-command approval on
- run `hermes doctor` after config changes
- keep weekly memory/skill hygiene review cadence
- log automation outputs to durable artifacts when possible
