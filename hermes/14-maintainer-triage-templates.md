# Hermes Maintainer Triage Templates

Reusable templates for high-signal issue and PR triage.

Purpose:
- reduce queue noise
- improve contributor feedback quality
- speed up merge/close decisions

## Label taxonomy (suggested baseline)

Core labels:
- bug
- enhancement
- docs
- question
- good first issue

Priority labels:
- priority:P0
- priority:P1
- priority:P2

Area labels:
- area:gateway
- area:providers
- area:tools
- area:skills
- area:memory
- area:setup
- area:docs

Lifecycle labels:
- needs-triage
- needs-repro
- needs-tests
- blocked
- duplicate
- wontfix

## Issue triage checklist

1) Reproducibility
- is there a clear repro path?
- environment/version included?

2) Blast radius
- user-facing breakage or edge case?
- affects gateway/automation/safety?

3) Scope clarity
- expected vs actual behavior explicit?
- acceptance criteria identifiable?

4) Actionability
- can contributor start immediately?
- does issue need maintainer clarification first?

## Issue comment template: request repro details

```text
Thanks for reporting this.

To move this forward quickly, please add:
1) exact Hermes version (`hermes --version`)
2) OS/runtime context
3) minimal reproducible steps
4) expected vs actual output
5) relevant logs/errors (redact secrets)

Once posted, we can confirm scope and label priority.
```

## Issue comment template: confirmed + accepted

```text
Confirmed — we can reproduce this behavior.

Scope accepted:
- root symptom: <summary>
- expected behavior: <summary>
- impact: <summary>

Marked for implementation with labels:
- <labels>

If you want to work on it, comment and we can assign.
```

## Issue comment template: duplicate closure

```text
Closing as duplicate of #<id> to keep discussion in one thread.

Please continue on #<id> where repro details and implementation tracking are centralized.
```

## Issue comment template: not planned

```text
Thanks for the suggestion.

We’re closing this as not planned for now due to:
- maintenance cost vs current roadmap priority
- limited impact relative to active reliability work

If constraints change, we can reopen with a concrete implementation proposal.
```

## PR review checklist (maintainer)

1) Scope discipline
- does PR solve one issue cleanly?
- unrelated changes removed?

2) Validation
- regression tests included for bugfixes?
- docs updated for behavior changes?

3) Safety
- no secret leakage
- no unsafe defaults introduced

4) Operability
- clear failure modes/errors
- works in headless/gateway contexts if relevant

5) Merge readiness
- CI green
- review comments resolved
- commit history acceptable (squash if needed)

## PR comment template: changes requested

```text
Thanks for the contribution — direction is good.

Requested before merge:
1) add/update regression test for <case>
2) tighten scope by removing <files/changes>
3) update docs/help text for user-visible behavior

After these are in, we can re-review quickly.
```

## PR comment template: approved with follow-ups

```text
Approved for merge.

Follow-up items (separate issue/PR):
1) <item>
2) <item>

Great improvement — thank you.
```

## Closure reason guide

Use these reasons consistently:
- completed: fix merged and released
- duplicate: tracked elsewhere
- not planned: valid idea but out of scope/priority
- cannot reproduce: insufficient repro after follow-up window

## Weekly triage cadence template

```text
Weekly Hermes triage:
- New issues reviewed: <n>
- Confirmed bugs: <n>
- Duplicates closed: <n>
- PRs reviewed: <n>
- Merged: <n>
- Blocked (needs info/tests): <n>

Top risk themes this week:
1) <theme>
2) <theme>

Actions for next week:
1) <action>
2) <action>
```

## CLI snippets for triage operations

```bash
# open issues
gh issue list -R NousResearch/hermes-agent --state open --limit 100

# open PRs
gh pr list -R NousResearch/hermes-agent --state open --limit 100

# bugs only
gh issue list -R NousResearch/hermes-agent --state open --label bug --limit 100

# issues needing triage
gh issue list -R NousResearch/hermes-agent --state open --label needs-triage --limit 100
```
