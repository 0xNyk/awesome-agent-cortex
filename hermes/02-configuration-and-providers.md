# Hermes Configuration and Providers

## Config files and runtime state

Hermes user state lives in `~/.hermes/`:
- `config.yaml` (runtime settings)
- `.env` (API keys/secrets)
- `state.db` (session DB with search)
- `skills/` (active skills)
- `memories/` (persistent memory files)
- `sessions/`, `cron/`, `logs/` (ops state)

## Model/provider routing

Upstream supports provider switching without code changes.
Common options in example config:
- `auto`
- `nous-api`
- `openrouter`
- `nous`
- `zai`
- `kimi-coding`
- `minimax`
- `minimax-cn`

Typical flow:

```bash
hermes model
```

Then confirm or edit values in `~/.hermes/config.yaml`.

## Terminal backend choices

From upstream example config, terminal backends include:
- local
- ssh
- docker
- singularity
(and in project docs/codebase: modal/daytona support is also present)

Use backend choice based on risk and reproducibility:
- local: fastest for personal/dev use
- ssh/containerized backends: better isolation and reproducibility

## Environment variables

Use `~/.hermes/.env` for keys.
Do not hardcode keys in tracked files.

High-signal env groups from upstream templates/docs:
- model/provider keys (OPENROUTER, GLM, MINIMAX, etc.)
- web/browser tool keys
- messaging platform tokens
- runtime settings (timeouts, working dirs)

## Security posture baseline

- keep secrets only in `.env`
- prefer isolated backend for untrusted repos/commands
- keep dangerous command approval enabled
- run `hermes doctor` after any major config change
