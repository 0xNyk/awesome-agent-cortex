# Claude Skill Engineering Playbook

A practical, implementation-first distillation of Anthropic's "The Complete Guide to Building Skills for Claude" plus battle-tested operator notes.

## 1) Skill architecture in one minute

A skill is a folder with:

- `SKILL.md` (required)
- `scripts/` (optional, deterministic helpers)
- `references/` (optional, deep docs loaded on demand)
- `assets/` (optional, templates/fonts/icons)

Core model:

1. Frontmatter in `SKILL.md` decides triggering.
2. Body of `SKILL.md` guides execution.
3. Linked files are fetched only when needed.

This progressive disclosure is the biggest quality + token efficiency lever.

## 2) Hard requirements and guardrails

- File must be exactly `SKILL.md` (case-sensitive)
- Skill folder must be kebab-case (e.g. `sprint-planner`)
- No skill-level `README.md` inside the skill folder
- Frontmatter must include `name` and `description`
- `description` should be under 1024 chars and include:
  - what the skill does
  - when to use it (trigger phrasing)
- Avoid XML brackets (`<` / `>`) in frontmatter
- Avoid reserved names using `claude` or `anthropic`

## 3) Frontmatter template patterns

Minimal:

```yaml
---
name: sprint-planner
description: Plans and executes sprint setup in Linear. Use when users ask to plan a sprint, create sprint tasks, prioritize backlog, or create Linear tickets.
---
```

Expanded:

```yaml
---
name: sprint-planner
description: Plans and executes sprint setup in Linear. Use for sprint planning, backlog grooming, velocity-based prioritization, and ticket creation.
license: MIT
compatibility: Requires Linear MCP server connection and permission to create issues.
allowed-tools: "Bash(python:*) WebFetch"
metadata:
  author: your-team
  version: 1.0.0
  mcp-server: linear
  category: workflow-automation
  tags: [sprint, planning, linear]
---
```

## 4) Trigger engineering (most important)

Description formula:

`[What it does] + [When to use it] + [Concrete phrases users say]`

Good trigger tactics:

- Include realistic user language, not internal jargon
- Include file-type cues if relevant (`.fig`, `.csv`, `.pdf`)
- Add scope constraints for precision
- Add negative triggers to reduce over-triggering

Example with negative scope:

```yaml
description: Advanced CSV statistical modeling for regression and clustering. Use when users request predictive analysis, feature significance, or model diagnostics. Do NOT use for simple charting or exploratory summaries.
```

Quick debug trick:

Ask Claude: `When would you use the [skill-name] skill?`

If the answer is vague, your description is vague.

## 5) Instruction design that actually executes reliably

Recommended SKILL.md body shape:

1. Purpose
2. Preconditions
3. Numbered workflow (explicit step order)
4. Validation gates after each major step
5. Error handling and recovery
6. Examples
7. Stop/finish criteria

Use explicit, checkable instructions:

Bad: `Validate inputs before creating the project.`

Good:

- Verify project name is non-empty
- Verify at least one assignee exists
- Verify start date is not in the past
- Only then call `create_project`

For critical checks, prefer scripts over natural language:

- `scripts/validate_inputs.py`
- deterministic checks
- fewer model-interpretation failures

## 6) Five high-value workflow patterns

1. Sequential orchestration
- Use when ordering/dependencies matter.
- Include rollback instructions per stage.

2. Multi-MCP coordination
- Split into phases by system (e.g., Figma -> Drive -> Linear -> Slack).
- Pass artifacts explicitly between phases.

3. Iterative refinement loops
- Draft -> validate -> fix -> revalidate
- Define clear stop criteria to avoid endless loops.

4. Context-aware tool selection
- Decision tree chooses tools by file type, size, collaboration mode, etc.
- Explain tool choice to user.

5. Domain-intelligence wrappers
- Embed compliance/governance checks before action.
- Persist auditable decisions.

## 7) Testing and evaluation rubric

Run 3 classes of tests:

1) Trigger tests
- should-trigger prompts (obvious + paraphrased)
- should-not-trigger prompts (irrelevant requests)

2) Functional tests
- happy path
- edge cases
- tool/API failures
- retries + graceful degradation

3) Baseline comparison (with vs without skill)
- task completion time
- clarifying turns
- failed tool calls
- token usage

Practical target heuristics:

- ~90% trigger reliability on intended prompts
- 0 failed API/tool calls on golden path
- materially fewer user corrections vs baseline

## 8) Distribution strategy

Current practical flow:

- host skill in public GitHub repo (human-facing README at repo level)
- provide install instructions for Claude.ai / Claude Code
- include screenshots and real examples
- link skill docs from your MCP integration docs

For API products:

- manage/list via `/v1/skills`
- pass skills in `container.skills`
- version in console + metadata

## 9) Troubleshooting playbook

Upload fails:

- "Could not find SKILL.md" -> wrong filename/case
- "Invalid frontmatter" -> malformed YAML delimiters/quotes
- "Invalid skill name" -> not kebab-case

Doesn't trigger:

- description too generic
- missing realistic trigger phrasing
- no file/task cues

Triggers too often:

- add negative triggers
- tighten scope and domain

Skill loads but fails execution:

- MCP not connected/auth expired
- wrong tool names/casing
- instructions too ambiguous or buried

Large-context degradation:

- keep `SKILL.md` lean (move deep docs to `references/`)
- avoid enabling too many skills at once
- prefer modular skill packs

## 10) Anti-patterns to avoid

- Generic descriptions (`helps with projects`)
- Monolithic SKILL.md with huge inline reference dumps
- No examples of expected user requests
- No error handling or recovery path
- No explicit validation gates
- No iteration plan after observing failures

## 11) 30-minute build workflow

1. Define 2-3 concrete use cases.
2. Write frontmatter (trigger-focused).
3. Draft minimal stepwise instructions.
4. Add one deterministic validation script.
5. Add 6-10 trigger tests (positive + negative).
6. Run one baseline comparison.
7. Tighten description + edge-case handling.
8. Publish with install quickstart and examples.

## 12) Copy/paste starter skeleton

```md
---
name: your-skill-name
description: [What it does]. Use when users ask to [trigger 1], [trigger 2], or [trigger 3].
license: MIT
metadata:
  author: your-team
  version: 0.1.0
---

# Your Skill Name

## Purpose
[Outcome the skill achieves]

## Preconditions
- [Connection/auth/dependency checks]

## Workflow
1. [Step 1]
2. [Step 2]
3. [Step 3]

## Validation Gates
- [Check A]
- [Check B]

## Common Errors and Fixes
- Error: [message]
  - Cause: [cause]
  - Fix: [resolution]

## Examples
- User: "[real prompt phrase]"
  - Action: [what should happen]

## Completion Criteria
- [What must be true before final response]
```
