# Hermes Operator Checklists

Practical recurring checklists for reliability and quality.

## Daily checklist (10-15 min)

1) Runtime health
- `hermes doctor`
- confirm active provider/model still healthy

2) Automation health
- review recent scheduled job outputs
- verify no silent failures/timeouts

3) Memory hygiene (light)
- capture only high-signal learnings
- avoid noisy/trivial memory writes

4) Security quick pass
- verify no secrets in tracked files
- verify approval policy still enabled

## Weekly checklist (30-45 min)

1) Memory compaction review
- identify stale/redundant memory items
- produce recommendation plan first
- require explicit approval before deletions

2) Skills maintenance
- inspect recently used skills
- patch stale steps/paths/assumptions
- add one new skill from repeated workflows

3) Config drift review
- compare current config against desired baseline
- verify terminal backend and cwd policy

4) Reliability review
- scan recent tool failures
- convert recurring failures into documented runbooks

## Monthly checklist (60-90 min)

1) Dependency/runtime review
- update Hermes and supporting dependencies
- run full diagnostics after upgrade

2) Workflow benchmark
- test representative tasks end-to-end
- document latency, failure patterns, intervention rate

3) Security and privacy review
- rotate sensitive credentials as needed
- review message platform permissions and access

4) Architecture review
- confirm current profile (local/vps/isolated/messaging-first)
- adjust stack split between control-plane and executor agents

## Incident checklist (when things break)

1) Stop automation blast radius
- disable or pause risky cron jobs

2) Collect evidence
- command logs, tool outputs, config snapshot

3) Reproduce minimally
- isolate failing task in smallest possible environment

4) Fix and verify
- implement minimal patch
- rerun target workflow + diagnostics

5) Learn
- write/update skill or runbook so issue becomes non-recurring
