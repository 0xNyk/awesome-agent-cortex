# Hermes Troubleshooting Decision Tree

Use this when Hermes behavior degrades or fails.

## Step 0: classify the failure

A) Startup / install failure
B) Model/provider/auth failure
C) Tool invocation failure
D) Gateway/messaging failure
E) Memory/skill behavior quality failure

Route to the branch below.

## A) Startup / install failure

1. Is `hermes` command available?
- no -> verify PATH includes `~/.local/bin`, reload shell rc
- yes -> continue

2. Run:

```bash
hermes doctor
```

3. If Python/env mismatch suspected:
- re-run setup flow
- confirm virtual env and dependency install status

## B) Model/provider/auth failure

1. Check selected provider/model:

```bash
hermes model
```

2. Validate key presence in `~/.hermes/.env`
3. Retry simple prompt in CLI
4. If still failing:
- switch temporarily to known-good provider/model
- run `hermes doctor`

## C) Tool invocation failure

1. Check whether tool is enabled:

```bash
hermes tools
```

2. Confirm prerequisite env vars for that tool
3. Reproduce with a minimal safe input
4. If terminal-related:
- verify backend/cwd configuration
- test backend with simple command

## D) Gateway/messaging failure

1. Confirm gateway process is running
2. Verify platform tokens and chat authorization config
3. Validate `MESSAGING_CWD` and permissions
4. Restart gateway after config changes

## E) Memory/skill quality failure

1. Memory too noisy or stale?
- run compaction review (recommendation-only first)

2. Skill failing repeatedly?
- patch exact failing step
- add verification command into skill body

3. Re-test on one representative workflow before broad rollout

## Escalation criteria

Escalate to deeper debug when any condition is true:
- failure persists across two clean reproductions
- failure impacts scheduled automation or production messaging
- failure might involve secret leakage or unsafe command execution

Escalation workflow:
1. collect minimal reproducible case
2. capture exact command/output evidence
3. open issue or patch with precise steps and expected vs actual
