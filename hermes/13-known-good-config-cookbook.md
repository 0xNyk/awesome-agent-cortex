# Hermes Known-Good Config Cookbook

Battle-tested configuration recipes for common provider + gateway combinations.

Use these as starting points, then adapt to your environment.
Always run `hermes doctor` after changes.

## Conventions

- Keep secrets in `~/.hermes/.env` (or equivalent secret manager)
- Keep runtime config in Hermes config file/CLI settings
- Use explicit `MESSAGING_CWD`

## Recipe 1: CLI-only, OpenRouter provider (local dev)

Best for:
- daily interactive use
- no messaging gateway

Environment:

```bash
OPENROUTER_API_KEY=replace_me
MESSAGING_CWD=/Users/you/work/hermes
```

Validation:

```bash
hermes doctor
hermes model
hermes
```

Expected outcome:
- clean doctor report
- prompt/response loop works in CLI

## Recipe 2: VPS + Telegram gateway + OpenRouter

Best for:
- personal assistant via Telegram
- headless operation

Environment:

```bash
OPENROUTER_API_KEY=replace_me
TELEGRAM_BOT_TOKEN=replace_me
MESSAGING_CWD=/opt/hermes/workdir
```

Operational settings:
- run gateway under systemd (not interactive shell)
- allowlist intended chat IDs/users

Validation:
1) `/start`
2) one short prompt
3) one tool-light prompt

Expected outcome:
- bot responds consistently after shell disconnect/reboot

## Recipe 3: VPS + Discord gateway + OpenAI-compatible provider

Best for:
- team channel assistant in controlled server

Environment:

```bash
OPENAI_API_KEY=replace_me
DISCORD_BOT_TOKEN=replace_me
MESSAGING_CWD=/opt/hermes/workdir
```

Operational settings:
- bot has only required channel permissions
- privileged intents enabled only if required

Validation:
- bot can read and reply in target test channel
- no permission errors in logs

## Recipe 4: Slack ops channel + gateway alerts

Best for:
- lightweight team operations bot

Environment:

```bash
OPENAI_API_KEY=replace_me
SLACK_BOT_TOKEN=replace_me
MESSAGING_CWD=/opt/hermes/workdir
```

Operational settings:
- minimal scopes
- bot installed to correct workspace
- restrict to private ops channel first

Validation:
- test mention + command/prompt roundtrip
- verify no OAuth scope errors

## Recipe 5: Isolated executor + control-plane split

Best for:
- safer autonomous operations
- strict blast-radius control

Pattern:
- control-plane Hermes handles memory, scheduling, routing
- executor Hermes runs high-risk tool tasks in isolated env

Environment notes:
- control-plane has messaging tokens
- executor has scoped filesystem/network and minimal secrets

Validation:
- end-to-end delegated task completes
- no sensitive cross-environment leakage

## Recipe 6: Docker compose baseline

Best for:
- reproducible deployment
- quick rollback and upgrades

Minimal `.env`:

```bash
OPENROUTER_API_KEY=replace_me
MESSAGING_CWD=/workspace
# optional gateway tokens
# TELEGRAM_BOT_TOKEN=replace_me
```

Validation:

```bash
docker compose ps
docker compose logs --tail=100 hermes
```

Expected outcome:
- container stays healthy
- no repeated auth/provider failures

## Failure pattern map (quick)

Symptom: provider calls fail immediately
- check key presence and active model
- switch to known-good model/provider for isolation

Symptom: gateway online but no replies
- verify token + allowlist + channel permissions
- verify process is still alive (systemd/docker)

Symptom: tool failures only in gateway mode
- verify `MESSAGING_CWD` exists and is writable
- test tool in CLI mode with minimal input

## Promotion checklist (before calling config “known good”)

A config earns known-good status only when:
1) `hermes doctor` is clean
2) 3 smoke prompts pass (basic, tool-light, formatting-sensitive)
3) one restart/reboot test passes
4) one scheduled automation run (if used) passes
5) no secret leakage in logs or tracked files

## Template: local known-good record

Copy into your ops notes per environment:

```text
Profile name:
Host/environment:
Provider/model:
Gateway platform:
MESSAGING_CWD:
Service mode (systemd/docker/manual):
Smoke test date:
Operator:
Notes/failures observed:
```
