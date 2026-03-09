# Global Instructions

> Copy this file to `~/.codex/instructions.md` to apply these rules to all projects.
> These are universal defaults -- override them per-project in each repo's `AGENTS.md`.

## Code Quality

- Follow existing code patterns and conventions in each project
- Write clean, readable code with descriptive names
- Keep functions small and focused on a single responsibility
- Use early returns to reduce nesting
- Remove unused imports and dead code
- Prefer composition over inheritance
- Avoid premature abstraction -- solve the current problem, not hypothetical future ones

## Security

- Never commit secrets, API keys, or credentials
- Never commit .env files or credential stores
- Validate and sanitize all external inputs
- Use parameterized queries for database operations
- Use environment variables for sensitive configuration
- Prefer allowlists over blocklists for access control

## Git Workflow

- Use conventional commits: type(scope): description
  - feat: new feature
  - fix: bug fix
  - docs: documentation only
  - test: adding or updating tests
  - refactor: code change that neither fixes a bug nor adds a feature
  - chore: maintenance tasks
- One logical change per commit
- Write descriptive commit messages explaining why, not what
- Never force-push shared branches
- Keep commits small and reviewable

## Testing

- Write tests for new functionality
- Test behavior, not implementation details
- Include edge cases and error conditions
- Ensure tests are deterministic -- no flaky tests
- Use descriptive test names that explain the scenario and expected outcome

## Communication

- Be concise and direct
- Explain your reasoning for non-obvious changes
- Ask clarifying questions rather than guessing
- When proposing multiple approaches, state the tradeoffs clearly
