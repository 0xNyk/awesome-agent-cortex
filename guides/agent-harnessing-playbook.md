# Agent Harnessing Playbook

A practical guide for building agent harnesses that actually improve reliability before release.

## 1) What "harnessing" should mean

A harness is not just a benchmark script.
It is a repeatable system for:
- scenario generation
- execution control
- scoring and diagnostics
- regression gating
- release decisioning

If it cannot block a bad release, it is not a complete harness.

## 2) Harness architecture

Core components:
1. Task set
- golden-path tasks
- edge cases
- adversarial/failure tasks

2. Runtime wrapper
- deterministic run config (model, tools, timeouts, retries)
- structured logs of prompts, tool calls, outputs, and failures

3. Scoring layer
- task success
- policy adherence
- grounding/citation checks
- latency/token/cost metrics

4. Reporting layer
- per-task diagnostics
- trend comparison vs baseline
- release gate pass/fail summary

## 3) Benchmark strategy

Use multiple benchmark classes:

- Domain benchmark: SWE-bench / MLE-bench / AgentBench style
- Environment benchmark: BrowserGym / WebArena / OSWorld style
- Internal task benchmark: your real production workflows

Rule of thumb:
- External benchmarks = comparability
- Internal benchmarks = business relevance
You need both.

## 4) Minimum metric set

Track at least:
- Success rate
- Critical error rate
- Policy/safety violation rate
- Tool failure rate
- Median and P95 latency
- Median and P95 token cost

Always trend metrics by version and compare against prior stable baseline.

## 5) Regression gates

Define non-negotiable release gates:

Example:
- success_rate >= previous - 1.5%
- critical_errors == 0 on golden tasks
- policy_violations == 0 on safety suite
- p95_latency <= previous + 10%
- p95_cost <= previous + 15%

If any gate fails, release blocks.

## 6) Scenario design checklist

For each task suite include:
- happy path
- malformed input
- partial/missing context
- conflicting instructions
- tool timeout/error responses
- stale memory/conflicting memory
- long-context distractors
- multi-turn correction loops

Avoid overfitting to synthetic toy prompts only.

## 7) Orchestration harness best practices

- Pin model/tool versions during evaluation windows.
- Keep deterministic run settings where possible.
- Cap retries and log each retry cause.
- Separate planner quality from executor quality in diagnostics.
- Include rollback tests for multi-step workflows.

## 8) Browser/computer-use harness tips

- Use environment resets between runs.
- Validate state transitions, not just final text output.
- Record action traces/screenshots for debugging.
- Distinguish UI-change brittleness from reasoning failures.

## 9) Failure taxonomy (use this in reports)

Label failures consistently:
- retrieval_failure
- instruction_conflict
- tool_call_error
- tool_result_misinterpretation
- memory_staleness
- unsafe_action
- budget_exceeded
- unknown

This lets teams prioritize systematic fixes rather than random prompt tweaks.

## 10) Release readiness ladder

L1: ad-hoc manual checks only
L2: repeatable benchmark runs with historical comparisons
L3: automated gates in CI/CD + incident feedback loop into harness tasks

Goal: reach L3 for production systems.

## 11) Recommended resources

- SWE-bench: https://github.com/SWE-bench/SWE-bench
- MLE-bench: https://github.com/openai/mle-bench
- Inspect AI: https://github.com/UKGovernmentBEIS/inspect_ai
- AgentBench: https://github.com/THUDM/AgentBench
- AgentEvals: https://github.com/langchain-ai/agentevals
- BrowserGym: https://github.com/ServiceNow/BrowserGym
- WebArena: https://github.com/web-arena-x/webarena
- WorkArena: https://github.com/ServiceNow/WorkArena
- OSWorld: https://github.com/xlang-ai/OSWorld
- Tau-Bench: https://github.com/sierra-research/tau-bench
