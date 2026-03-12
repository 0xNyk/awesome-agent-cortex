# New Maintainer: First 14 Days Plan (Live Queue Aligned)

Goal: become reliably useful in review + triage + high-impact fixes within two weeks.

This plan is aligned to current open Hermes issue/PR patterns.
Refresh queue daily because it moves fast.

## Operating principles

1) Reliability-first over novelty
2) Small scoped PRs with tests
3) Fast review turnaround
4) Triage quality is part of maintainership

## Queue focus buckets (current)

Bucket A: hot reliability bugs
- #1011 custom provider delegation
- #1005 Telegram gateway lifecycle on headless hosts
- #1002 terminal env leak to subprocesses
- #989 DeepSeek multi-tool parse reliability
- #987 gateway sessions NULL model

Bucket B: setup/operator friction
- #905 setup wizard non-interactive hang
- #961 doctor Honcho false-unavailable
- #878 cron dependency false-negative
- #913/#850 Docker/VPS deployment experience

Bucket C: ecosystem and safety quality
- #1006 skills guard policy behavior
- #982 provider OAuth expansion requests
- #966 provider addition requests

## Day-by-day plan

## Day 1
- pull latest main, run tests locally
- map top 10 open issues by severity + reproducibility
- post one high-signal triage summary comment (if appropriate)

## Day 2
- review open PRs linked to Bucket A issues
- leave actionable review comments on 1-2 PRs
- pick one unblocked reliability issue to own

## Day 3
- implement smallest viable fix on owned issue
- include regression test + clear PR narrative

## Day 4
- respond to review feedback quickly
- help verify another contributor PR (cross-testing)

## Day 5
- close loop on first merged/ready PR
- update docs/runbook if behavior changed

## Day 6
- pick one setup/operator issue from Bucket B
- focus on diagnostics/error-message quality + headless behavior

## Day 7
- ship second scoped PR
- run a mini triage sweep: dedupe or clarify 3-5 issues

## Day 8
- review queue drift and reprioritize
- pick one issue where you can unblock others with tests/docs

## Day 9
- contribute one maintainership artifact:
  - triage template
  - review checklist
  - runbook patch

## Day 10
- help land at least one non-self PR via review and validation
- propose closure on stale/duplicate items with evidence

## Day 11
- pick one safety/skills/memory quality item (Bucket C)
- ensure behavior/docs/help text are aligned

## Day 12
- ship third scoped PR or substantial review batch
- summarize impact in one status update comment

## Day 13
- perform reliability audit on recent merges
- file follow-up issues with crisp repro where needed

## Day 14
- publish 2-week maintainer readiness summary:
  - merged PRs
  - reviewed PRs
  - triaged issues
  - reliability wins
  - next 30-day focus

## Daily command block

```bash
gh issue list -R NousResearch/hermes-agent --state open --limit 50
gh issue list -R NousResearch/hermes-agent --state open --label bug --limit 50
gh pr list -R NousResearch/hermes-agent --state open --limit 50
```

## PR acceptance checklist for yourself

- issue-linked and scope-clean
- regression test included
- docs/help updated if user-visible
- no unrelated formatting/refactor churn
- easy-to-review commit history

## 14-day success criteria

You are on-track for maintainer trust if by day 14 you have:
- 2-3 high-signal merged PRs (or merge-ready with strong review feedback)
- consistent review participation on others’ PRs
- measurable triage improvements (dedupe/closure/label hygiene)
- at least one runbook/checklist/process improvement artifact

## Anti-patterns to avoid

- large multi-feature PRs early
- claiming ownership without reproducing issue
- merging docs promises without implementation follow-through
- ignoring queue triage while only shipping personal roadmap work
