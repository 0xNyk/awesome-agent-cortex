# Context Engineering Playbook

A practical guide for designing context pipelines that stay accurate, efficient, and robust over long-running agent workflows.

## 1) Context budget first

Treat tokens like a hard systems budget, not an afterthought.

Use a fixed allocation model per request:
- `B_total = B_system + B_tools + B_history + B_retrieval + B_output`

Rules:
- Reserve output tokens first.
- Keep a hard cap for history and retrieval.
- Fail fast when budget exceeded (do not silently truncate critical constraints).

## 2) Instruction layering

Use explicit precedence:
1. System policy/role (immutable)
2. Task contract (goal, constraints, output schema)
3. Runtime state (retrieval/tool outputs)
4. User message

Guidelines:
- Prefer machine-checkable contracts (JSON schema, strict fields, required citations).
- Add explicit uncertainty behavior:
  - ask clarifying questions when evidence is missing
  - return structured failure mode when confidence is low

## 3) Retrieval context shaping

Quality beats quantity.

Recommended pipeline:
1. Query rewrite (expand entities/acronyms/time ranges)
2. Hybrid retrieval (keyword + vector)
3. Rerank top-k for relevance and diversity
4. Context packing with dedupe and source metadata

Packing tips:
- Include only chunks tied to current subtask.
- Avoid near-duplicates.
- Attach source IDs and timestamps.
- Keep chunk rationale short: "why included".

## 4) Memory architecture

Separate short-term and long-term memory.

Short-term memory:
- current objective
- active plan state
- latest key facts/tool results

Long-term memory:
- stable user preferences
- recurring procedures
- durable project conventions

Write-memory triggers:
- user correction
- repeated preference/fact
- durable environment convention

Memory hygiene:
- use confidence + recency metadata
- decay or expire volatile entries
- provide edit/delete path for incorrect memory

## 5) Anti-drift controls

Long sessions drift unless you actively re-anchor.

Controls:
- Re-anchor every few turns/tool calls:
  - objective
  - constraints
  - done criteria
- Use plan -> execute -> review loops.
- Add pre-finalization check:
  - assumptions
  - missing evidence
  - policy/constraint compliance

## 6) Eval loops

Ship with measurable quality gates.

Track separately:
- task success
- grounding/citation correctness
- instruction adherence
- safety/refusal correctness
- latency, token usage, cost

Best practice:
- Build eval sets from real failure logs.
- Add adversarial and long-context scenarios.
- Run regression gates before deploying prompt/retrieval/memory changes.

## 7) Failure modes and fixes

1. Lost-in-the-middle
- Symptom: critical constraints ignored mid-context.
- Fix: reorder by relevance; repeat high-priority constraints at edges.

2. Retrieval pollution
- Symptom: irrelevant context derails answer.
- Fix: tighter rerank, dedupe, stricter context caps.

3. Instruction conflict
- Symptom: inconsistent behavior across runs.
- Fix: explicit hierarchy and conflict resolution policy.

4. Memory hallucination/staleness
- Symptom: outdated facts reused as truth.
- Fix: timestamps, confidence checks, verify before high-impact actions.

5. Tool-output overtrust
- Symptom: bad downstream actions from malformed tool results.
- Fix: schema validation + guard checks before action.

## 8) Production checklist

- [ ] Hard token budget per route/use case
- [ ] Output reservation and truncation controls
- [ ] Layered instruction contract documented
- [ ] Retrieval pipeline includes rerank + dedupe
- [ ] Source IDs/citations in final outputs
- [ ] Short-term vs long-term memory split
- [ ] Memory write triggers and hygiene policy
- [ ] Drift re-anchoring cadence configured
- [ ] Regression eval suite from real failures
- [ ] Cost/latency/quality telemetry in place

## 9) Canonical references

- Anthropic: Building Effective Agents  
  https://www.anthropic.com/engineering/building-effective-agents
- Anthropic: Contextual Retrieval  
  https://www.anthropic.com/engineering/contextual-retrieval
- OpenAI Prompt Engineering Guide  
  https://platform.openai.com/docs/guides/prompt-engineering
- OpenAI Evals Guide  
  https://platform.openai.com/docs/guides/evals
- OpenAI Cookbook: Getting Started with Evals  
  https://developers.openai.com/cookbook/examples/evaluation/getting_started_with_openai_evals
- RAG (Lewis et al., 2020)  
  https://arxiv.org/abs/2005.11401
- Chain-of-Thought Prompting (Wei et al., 2022)  
  https://arxiv.org/abs/2203.02155
- Lost in the Middle (Liu et al., 2023)  
  https://arxiv.org/abs/2307.03172
