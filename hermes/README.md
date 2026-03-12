# Hermes Hub

Practical, repo-local knowledge base for running and contributing to Hermes Agent.

This folder is curated from official sources plus operator-oriented synthesis.
If any guidance here conflicts with upstream docs, treat upstream as canonical.

## What is Hermes Agent?

Hermes Agent is an open-source autonomous AI agent runtime from Nous Research.
Core traits called out by upstream:
- persistent memory + user profile across sessions
- skill system (procedural memory)
- tool-use with terminal/file/web/browser/process orchestration
- subagent delegation and parallel task execution
- multi-platform gateway (CLI + messaging)
- built-in cron scheduling

## Folder map

- [01-quickstart.md](01-quickstart.md)
  - install, first run, day-1 commands
- [02-configuration-and-providers.md](02-configuration-and-providers.md)
  - config model/provider setup, terminal backends, env vars
- [03-memory-skills-automation.md](03-memory-skills-automation.md)
  - memory model, skills lifecycle, cron workflows
- [04-dev-and-contrib.md](04-dev-and-contrib.md)
  - contributor setup and architecture orientation
- [05-production-profiles.md](05-production-profiles.md)
  - copy/paste deployment profiles (local, VPS, isolated, messaging-first)
- [06-runtime-comparison-matrix.md](06-runtime-comparison-matrix.md)
  - operator-level comparison of Hermes and common alternatives
- [07-operator-checklists.md](07-operator-checklists.md)
  - daily/weekly/monthly/incident operational checklists
- [08-troubleshooting-decision-tree.md](08-troubleshooting-decision-tree.md)
  - fast failure triage path for install, auth, tools, gateway, and memory/skills
- [09-hardening-and-security-baseline.md](09-hardening-and-security-baseline.md)
  - minimum security controls and incident response baseline for persistent operations
- [10-gateway-platform-runbooks.md](10-gateway-platform-runbooks.md)
  - platform-specific bring-up/troubleshooting runbooks for Telegram/Discord/Slack/WhatsApp
- [11-contribution-roadmap.md](11-contribution-roadmap.md)
  - high-impact issue/PR targeting plan for contributor-to-maintainer growth
- [12-systemd-and-docker-compose-appendix.md](12-systemd-and-docker-compose-appendix.md)
  - copy/paste deployment recipes for systemd and docker-compose operations
- [13-known-good-config-cookbook.md](13-known-good-config-cookbook.md)
  - battle-tested provider/gateway config recipes with promotion checklist
- [14-maintainer-triage-templates.md](14-maintainer-triage-templates.md)
  - reusable issue/PR triage templates, label taxonomy, and review checklists
- [15-operator-launch-checklist-one-page.md](15-operator-launch-checklist-one-page.md)
  - printable go/no-go launch checklist for day-0 and first-24h operations
- [16-incident-postmortem-template-and-example.md](16-incident-postmortem-template-and-example.md)
  - blame-free postmortem template plus filled gateway outage example
- [17-new-maintainer-first-14-days-plan.md](17-new-maintainer-first-14-days-plan.md)
  - practical 14-day maintainer ramp plan aligned to active Hermes queue patterns
- [references.md](references.md)
  - upstream links used for this hub

## Scope notes

This hub is intentionally implementation-aware (commands, paths, workflows) and
operator-focused (what to run, what to verify, what to avoid).
