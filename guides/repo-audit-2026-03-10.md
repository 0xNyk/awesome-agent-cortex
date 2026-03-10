# Repository Audit - awesome-agent-cortex (2026-03-10)

Scope:
- Content quality and structure review of README curation
- Link-health sampling across listed resources
- Alignment with contribution standards
- Incorporation opportunities from Anthropic's skill-building guide

## Executive summary

Strengths:
- Broad, high-signal landscape coverage (frameworks -> infra -> payments -> trading -> observability)
- Strong unique positioning around sovereign/on-chain agent stack + memory
- Clear contribution rules and quality bar
- Useful bundled Claude starter configs under `claude/`

Main gaps found:
- A few stale links (notably MCP and selected ecosystem repos)
- Some duplicate entries across sections (intentional in some places, but worth labeling)
- Missing dedicated section for skill engineering methodology
- No in-repo distilled operator guide for skill design/testing/distribution

## Data-backed findings

Automated scan snapshot:
- Sections scanned: 15
- Curated entries: 161
- Duplicate names detected: 3
- Duplicate URLs detected: 5
- Potentially broken/blocked links detected: 12

Notes:
- Some failures were likely anti-bot/geo/rate-limit effects (403/429), not true dead links.
- Confirmed hard 404s were prioritized for correction.

## Fixes applied in this pass

1) Added a new section in README:
- `Skill Engineering and Playbooks`

2) Added high-value resources:
- Anthropic complete guide PDF
- In-repo playbook distilled from the PDF
- In-repo quickstart checklist
- Official `anthropics/skills` repository

3) Repaired verified stale links:
- MCP CLI -> MCP Inspector (`modelcontextprotocol/inspector`)
- Playwright MCP -> `microsoft/playwright-mcp`
- Obsidian graph query repo -> `azuma520/obsidian-graph-query`

## Recommended next cleanup pass

- Validate Solana infra links with 404 history (e.g., ARC/Jupiter entries) and replace with currently maintained canonical sources.
- Annotate intentional duplicates where they span categories (e.g., Promptfoo in prompt + eval), so contributors do not remove by mistake.
- Add a lightweight periodic link check workflow (weekly scheduled GitHub Action) with allowlist for known 403/429 domains.

## Strategic recommendation

Turn the new skill-engineering docs into a living track:
- Add revision log sections
- Collect real-world edge cases from users
- Publish short pattern packs (sequential workflow, multi-MCP coordination, iterative QA loop)

This will keep the repo differentiated as both a discovery list and an implementation knowledge base.
