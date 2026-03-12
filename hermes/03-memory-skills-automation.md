# Hermes Memory, Skills, and Automation

## Memory model (practical)

Hermes distinguishes:
- user profile memory (preferences/identity-style facts)
- operational memory (environment/project/workflow notes)

Expected behavior in modern Hermes flows:
- save useful long-lived facts proactively
- avoid storing trivial/noisy data
- compact when memory pressure rises
- preserve user approval for destructive memory changes

## Skills lifecycle

Skills are procedural memory.
Typical lifecycle:
1. discover a repeatable workflow from real execution
2. codify it into a skill (clear trigger + step sequence)
3. reuse via skill loading
4. patch skill when drift/failures appear

Good skill qualities:
- exact commands
- constraints + prerequisites
- pitfalls
- verification checklist

## Session recall and continuity

Hermes supports searching past conversation sessions and summarizing the most relevant ones.
Use this before asking users to repeat prior context.

## Scheduled automation

Hermes includes cron-style automation with delivery targets.
Use this for recurring audits, reports, and maintenance routines.

Safe default for automation in open-source/public workflows:
- recommendation-only mode first
- explicit approval gate for destructive actions
- artifact/audit logs for every run

## Suggested operating playbook

- daily: capture high-signal memory + skill candidates
- weekly: memory compaction review + stale-skill check
- monthly: workflow drift review (what changed in tools/repo/docs)
