# Claude Skills Quickstart Checklist

Use this before publish, after publish, and after every major iteration.

## Planning

- [ ] Defined 2-3 concrete use cases
- [ ] Chosen one primary workflow pattern (sequential, multi-MCP, iterative, context-aware, domain-intel)
- [ ] Defined success metrics (trigger, quality, errors, efficiency)

## Structure

- [ ] Folder name is kebab-case
- [ ] `SKILL.md` exists with exact casing
- [ ] Optional folders used correctly (`scripts/`, `references/`, `assets/`)
- [ ] No skill-level `README.md` in skill folder

## Frontmatter

- [ ] `name` present and kebab-case
- [ ] `description` includes WHAT + WHEN
- [ ] Trigger phrases match real user language
- [ ] Negative trigger/scope constraints added if needed
- [ ] No XML angle brackets (`<` `>`) in frontmatter
- [ ] Optional metadata includes `version` and `author`

## Instructions

- [ ] Steps are explicit and ordered
- [ ] Validation gates included
- [ ] Common errors documented with fixes
- [ ] At least 2 realistic examples included
- [ ] Stop criteria defined

## Reliability

- [ ] Critical validations scripted (deterministic) when possible
- [ ] Tool names verified against MCP server docs
- [ ] Fallback path documented for tool/API failures
- [ ] Retries and rollback behavior defined where relevant

## Testing

- [ ] Positive trigger tests pass
- [ ] Paraphrased trigger tests pass
- [ ] Negative trigger tests pass
- [ ] Functional golden-path test passes
- [ ] Edge-case and failure-path tests pass
- [ ] Baseline comparison run (with vs without skill)

## Performance and context

- [ ] `SKILL.md` kept concise (deep docs moved to `references/`)
- [ ] Skill works with other enabled skills (composability)
- [ ] No context bloat from unnecessary inline docs

## Distribution

- [ ] Public repo includes install instructions
- [ ] Examples/screenshots provided
- [ ] MCP docs link to skill and explain combined value
- [ ] Version updated on each significant behavior change

## Post-launch operations

- [ ] Monitor under-triggering signals
- [ ] Monitor over-triggering signals
- [ ] Track API/tool failures
- [ ] Collect user feedback and edge cases
- [ ] Ship iterative improvements
