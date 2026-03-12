# Hermes Gateway Platform Runbooks

Operator runbooks for Telegram, Discord, Slack, and WhatsApp style deployments.

Use this file for day-1 bring-up and day-2 incident handling.

## Universal gateway preflight

Before platform-specific setup, confirm:

1) Core health
```bash
hermes doctor
```

2) Runtime policy
- explicit `MESSAGING_CWD`
- known-good provider/model
- approval policy compatible with remote execution risk

3) Access control
- allowlist intended chat/user/channel IDs
- disable broad public access

4) Recovery readiness
- know how to restart process cleanly
- keep minimal smoke test prompts ready

## Telegram runbook

## Bring-up
1) create bot token via BotFather
2) set token in environment/config
3) configure allowed chats/users
4) start gateway process
5) send `/start` and a simple prompt smoke test

## Common failure modes
- `/start` crashes due to config object mismatch
- gateway appears idle when process dies after shell exit
- wrong chat ID leads to silent non-response

## Fast checks
- verify gateway process still running
- verify token value and chat allowlist
- restart process after config edits

## Discord runbook

## Bring-up
1) create bot app and token
2) grant only required intents and channel scopes
3) invite bot to target server/channel
4) set token and channel filters
5) run smoke prompt in a private/test channel

## Common failure modes
- missing privileged intents
- wrong channel permissions
- bot online but blocked from reading/sending messages

## Fast checks
- confirm bot role permissions
- confirm channel-specific permission overrides
- test in isolated test channel before prod channels

## Slack runbook

## Bring-up
1) create Slack app + bot token
2) grant required scopes for message read/write
3) install app to workspace
4) configure allowed channel list
5) run smoke prompt in a private ops channel

## Common failure modes
- insufficient OAuth scopes
- app installed in wrong workspace
- event subscription mismatch

## Fast checks
- revalidate scopes and reinstall app after scope changes
- verify channel membership for bot user
- inspect event delivery logs in Slack app dashboard

## WhatsApp runbook

Exact workflow depends on gateway adapter/provider.

## Bring-up
1) provision provider credentials/webhook settings
2) configure allowed numbers/groups
3) start gateway and run direct-message smoke test
4) validate media/text round-trip behavior

## Common failure modes
- webhook verification mismatch
- provider auth expiration
- message template/policy rejection

## Fast checks
- verify webhook endpoint + signing config
- renew credentials/tokens
- test with simplest text payload first

## Headless/server reliability pattern

For all platforms on VPS/headless hosts:
- run gateway as managed service (systemd/supervisor)
- enable restart-on-failure
- separate logs per platform
- never rely on an interactive terminal staying open

## Day-2 operations

Daily:
- check process alive + recent message success
- verify no auth/token warnings

Weekly:
- rotate tokens where policy requires
- review access lists and remove stale chats/channels

Incident:
1) pause automation outputs
2) isolate failing platform adapter
3) validate credentials and permissions
4) restore with smoke test before reopening full traffic

## Minimal smoke test script (manual)

For each platform after deploy/restart:
1) `/start`
2) one short prompt
3) one tool-light prompt
4) one response with expected formatting

If any step fails, stop rollout and triage before enabling scheduled message delivery.
