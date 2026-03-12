# Hermes Contribution Roadmap (High-Impact)

A practical roadmap to move from contributor to trusted maintainer in Hermes Agent.

Snapshot basis: current open issues/PR flow in `NousResearch/hermes-agent`.
Re-check before starting implementation because queue moves fast.

## North-star outcomes

1) Reliability: fewer production regressions in gateway/tools/providers
2) Operability: smoother VPS/headless deployment and diagnostics
3) Contributor velocity: issues map cleanly to merge-ready PRs

## Contribution lanes

## Lane A: Reliability bugfixes (fastest trust builder)

Target issue themes:
- provider/delegation correctness
  - #1011 custom provider delegation failure
- tool parsing/execution correctness
  - #989 DeepSeek multi-tool parsing
  - #1002 terminal env leakage to subprocesses
- gateway stability
  - #973 `/start` GatewayConfig mismatch
  - #1005 Telegram stops responding on terminal close

Why this lane is high impact:
- direct user-facing breakages
- easy to verify with focused regression tests
- maintainers prioritize reliable core loops

Definition of done:
- minimal patch + regression test
- repro in issue body, fix proof in PR body
- no unrelated refactors

## Lane B: Operator experience and deployment hardening

Target issue themes:
- doctor/setup friction
  - #878 cron dependency false-negative
  - #905 setup wizard hangs in non-interactive SSH
  - #961 Honcho availability false report
- deployment support
  - #913 VPS/docker support
  - #850 full docker deployment

Why this lane matters:
- removes adoption friction
- high leverage for all new users

Definition of done:
- clear failure message quality improvements
- docs/runbook updates with exact commands
- compatibility tests for headless/non-interactive paths

## Lane C: Skills/memory UX and ecosystem quality

Target issue themes:
- skills metadata/source correctness
  - #861 skills source labeling
- skills safety policy behavior
  - #1006 official/builtin skills blocked unexpectedly
- extension/provider requests
  - #966 Kimi Coding provider
  - #982 OAuth/provider expansion ideas

Why this lane matters:
- preserves trust in Hermes differentiators (memory + skills)
- improves extensibility without breaking safety defaults

Definition of done:
- explicit UX semantics in CLI output/help text
- docs + tests aligned with user mental model

## Suggested 30-day execution plan

Week 1:
- pick 1 bug from Lane A
- ship fix + tests + clean PR narrative

Week 2:
- pick 1 issue from Lane B (doctor/setup/headless)
- ship user-visible diagnostics improvement

Week 3:
- pick 1 issue from Lane C
- ensure docs and tests cover edge cases

Week 4:
- triage pass: comment on stale/duplicate issues, propose merges/closures
- submit one cross-cutting refactor only if prior reliability work is merged

## PR quality bar (what maintainers reward)

- tight scope, no drive-by changes
- issue-linked PR body with repro/fix/verification sections
- tests proving regression is fixed
- operator-facing docs when behavior changes
- responsive review iteration (<24h turnaround preferred)

## Triage strategy for high-signal contribution

When issue queue is noisy:
1) prioritize reproducible bugs over vague feature ideas
2) prioritize issues with clear blast radius (gateway, provider, tools)
3) prioritize items with near-ready PRs that need review/testing help
4) de-duplicate near-identical feature requests before implementing

## Quick commands for live queue refresh

```bash
gh issue list -R NousResearch/hermes-agent --state open --limit 50
gh pr list -R NousResearch/hermes-agent --state open --limit 50
```

For detailed targeting:

```bash
gh issue list -R NousResearch/hermes-agent --state open --label bug --limit 50
gh pr list -R NousResearch/hermes-agent --state open --search "fix" --limit 50
```

## Personal positioning (maintainer ramp)

To accelerate trust:
- own one subsystem consistently (example: gateway/OpenClaw UI path)
- become the person who closes reliability regressions quickly
- follow up merges with docs/tests improvements, not just code drops
- help triage and review others, not only submit your own PRs

Consistency over volume wins.
