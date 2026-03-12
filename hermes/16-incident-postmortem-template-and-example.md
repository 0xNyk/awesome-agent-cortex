# Incident Postmortem Template + Example

Use this after any reliability/security/automation incident.

Goal: produce actionable learning, not blame.

## Template

## Incident metadata
- Incident ID:
- Date/time (start/end, timezone):
- Severity: (SEV1/SEV2/SEV3)
- Owner:
- Systems affected: (CLI, gateway, cron, provider, tools)

## Executive summary
- What happened:
- User impact:
- Business/operator impact:
- Current status:

## Timeline (UTC preferred)
- T0:
- T+5m:
- T+15m:
- T+30m:
- Resolution time:

## Detection and response
- How it was detected:
- Who responded:
- What worked well:
- What slowed recovery:

## Root cause analysis
- Primary root cause:
- Contributing factors:
- Why existing safeguards did not prevent it:

## Containment and remediation
- Immediate containment actions:
- Permanent fix:
- Verification performed:

## Preventive actions
- Action 1 (owner/date):
- Action 2 (owner/date):
- Action 3 (owner/date):

## Follow-up artifacts
- Related issue(s):
- Related PR(s):
- Runbook/skill/docs updated:
- Monitoring/alerting changes:

## Lessons learned
- Keep:
- Change:
- Stop doing:

## Example (Hermes gateway outage)

## Incident metadata
- Incident ID: HERMES-2026-03-12-01
- Date/time: 2026-03-12 10:15-11:02 UTC
- Severity: SEV2
- Owner: Ops maintainer
- Systems affected: Telegram gateway on VPS

## Executive summary
- What happened: Telegram bot stopped replying after terminal session closure on headless host.
- User impact: Bot appeared online but produced no responses for 47 minutes.
- Business/operator impact: Scheduled ops prompts were missed.
- Current status: Resolved; gateway now managed under systemd.

## Timeline
- 10:15: first non-response observed in Telegram
- 10:19: confirmed no new replies in logs
- 10:24: found process tied to terminated interactive shell
- 10:32: temporary restart restored replies
- 10:45: systemd unit created and enabled
- 11:02: smoke tests and restart tests passed

## Detection and response
- Detection: user report in ops chat
- Response: operator + maintainer pair
- Worked well: quick repro and narrow failure scope
- Slowed recovery: no prior runbook requiring managed service mode

## Root cause analysis
- Primary root cause: gateway process launched from interactive shell without supervisor
- Contributing factors: missing deployment guardrail/checklist gate
- Safeguard gap: launch checklist did not enforce service manager requirement

## Containment and remediation
- Immediate containment: restarted gateway and paused automation outputs
- Permanent fix: migrated to systemd unit with restart policy
- Verification: `/start`, short prompt, tool-light prompt, process restart test

## Preventive actions
- Add mandatory service-manager check to launch checklist (owner: docs maintainer, due: +1 day)
- Update gateway runbook with explicit anti-pattern note (owner: ops, due: +1 day)
- Add weekly check for gateway process mode (owner: on-call, due: +7 days)

## Follow-up artifacts
- Related issue(s): #1005
- Related PR(s): <fill when merged>
- Runbook updated: 10-gateway-platform-runbooks.md
- Monitoring changes: basic heartbeat check added

## Lessons learned
- Keep: minimal smoke-test sequence after each restart
- Change: only run gateway via managed service mode
- Stop doing: ad-hoc production launches from interactive shells
