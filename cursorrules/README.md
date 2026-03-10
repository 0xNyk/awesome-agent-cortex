# Cursor IDE Starter Configs

Curated starter configurations for [Cursor IDE](https://cursor.com). Drop these into your project and customize to fit your stack.

## What is this?

This folder contains opinionated but framework-agnostic configuration files for Cursor IDE's AI features. The goal is to give you a solid starting point so Cursor's AI assistant follows consistent conventions from day one.

## How to use

1. **Copy `.cursorrules` into your project root.** This is the main rules file that Cursor reads automatically. Open it and fill in the `Project Context` and `Tech Stack` sections for your project.

2. **Copy the `rules/` folder into `.cursor/rules/` in your project.** These are granular rule files (`.mdc` format) that Cursor applies based on file globs. You can enable, disable, or modify individual rules without touching the main `.cursorrules` file.

```
your-project/
  .cursorrules              <-- from this folder
  .cursor/
    rules/
      general.mdc           <-- from rules/
      testing.mdc
      security.mdc
      git.mdc
```

3. **Customize.** These are starting points, not gospel. Remove what does not apply, add what your team cares about.

## Contents

| File | Purpose |
|------|---------|
| `.cursorrules` | Root-level rules file. Defines project context, tech stack, code style, error handling, security, and testing conventions. |
| `rules/general.mdc` | General coding conventions applied to all files. |
| `rules/testing.mdc` | Testing patterns and conventions, scoped to test files. |
| `rules/security.mdc` | Security rules scoped to source code files. |
| `rules/git.mdc` | Git workflow and commit conventions. |

## Inspiration and credits

- [awesome-cursorrules](https://github.com/PatrickJS/awesome-cursorrules) -- community-curated collection of `.cursorrules` files
- [cursor.directory](https://cursor.directory) -- searchable directory of Cursor rules
