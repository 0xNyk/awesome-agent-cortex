# Contributing to Awesome Agent Cortex

This is a curated directory, so not every submission will be accepted. A useful pull request makes one resource easier to evaluate without adding promotional noise.

## Adding an entry

### Format

```markdown
- [Project Name](https://github.com/user/repo) - Concise description of what it does.
```

### Rules

1. **One entry per pull request.** Batch PRs take longer to review.
2. **Description** starts with a capital letter and ends with a period.
3. **No marketing language.** Describe verifiable capabilities instead of unsupported hype.
4. **No trailing slashes** on URLs.
5. **Drop unnecessary articles** (A, An, The) at the start of descriptions.
6. **Alphabetical order** within each section.
7. **Working links only.** Dead links will be removed.
8. The project should be **actively maintained** (commit within the last 12 months).
9. The project should have **meaningful documentation** (at minimum a README).

### What we look for

- Genuine usefulness to agent builders
- Active maintenance and community
- Clear documentation
- Distinct value that is not a thin wrapper around another listed project

## Awesome Score rubric

To keep reviews consistent, we score candidate entries from 1 (weak) to 5
(strong) across five dimensions:

1. **Maintenance**
   - Recency of commits/releases, issue responsiveness, non-archived status.
2. **Documentation quality**
   - Clear README/docs, setup steps, examples, and API usage guidance.
3. **Production readiness**
   - Stability signals (tests/CI, real users, operational guidance).
4. **Unique value**
   - Adds capability or coverage beyond existing list entries.
5. **Security posture**
   - Reasonable security controls/disclosures for its category.

### Suggested acceptance baseline

- Recommended: average score >= 3.5/5
- Strongly preferred: no individual dimension below 3

In PR descriptions, include a short rubric line, e.g.:

`Awesome Score: Maintenance 4, Docs 5, Production 4, Unique 4, Security 3`

### What we reject

- Abandoned or archived projects
- Projects with no documentation
- Duplicate entries
- Self-promotion without substance
- Entries that do not fit any existing section

## Intentional cross-listings

Some resources are intentionally listed in multiple sections when they provide
strong value across distinct workflows (for example: Prompt + Evaluation, or
Coding Agent + CLI Tool).

Rules for cross-listing:

1. Only cross-list when the overlap is meaningful to users.
2. Keep the description aligned to each section's context (same project, but
   section-relevant phrasing is okay).
3. In PRs, explicitly call out intentional cross-listings in the description so
   reviewers do not remove them as accidental duplicates.
4. Avoid excessive repetition. If a project appears in more than two sections,
   justify why.

## Suggesting a new section

Open an issue first to discuss whether a new section is warranted. New sections
should have at least 5 qualifying entries before being added.

## Reporting issues

- Open an issue or pull request to fix a broken link.
- Open an issue or pull request to update an outdated description.
- Open an issue when a project appears unmaintained so the listing can be reviewed.

## Code of conduct

This project follows the [Contributor Covenant](CODE_OF_CONDUCT.md). By
participating, you agree to abide by its terms.

## Contribution integrity

AI-assisted contributions follow the same standard as any other pull request. The contributor remains responsible for accuracy, licensing, working links, provenance, and understanding every submitted change.

Do not include credentials, personal data, private deployment details, unrelated local paths, or generated claims that cannot be verified.
