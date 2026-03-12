# Hermes Development and Contribution Notes

## Contributor setup (upstream-aligned)

```bash
git clone --recurse-submodules https://github.com/NousResearch/hermes-agent.git
cd hermes-agent
curl -LsSf https://astral.sh/uv/install.sh | sh
uv venv .venv --python 3.11
source .venv/bin/activate
uv pip install -e ".[all,dev]"
uv pip install -e "./mini-swe-agent"
pytest tests/ -q
```

## Architecture orientation

Core files to understand first:
- `run_agent.py` (agent loop)
- `cli.py` / `hermes_cli/` (CLI commands, setup, config)
- `tools/registry.py` + tool modules (tool registration/dispatch)
- `toolsets.py` (platform tool groupings)
- `gateway/` (messaging runtime)
- `hermes_state.py` (session DB/search)

## Adding a new tool (high-level)

Upstream pattern requires updates in multiple places:
1. add tool module under `tools/`
2. ensure discovery/import path includes the tool
3. map it into a toolset
4. add tests and docs

## Config changes

When adding config/env options in Hermes core, update config schemas/defaults and migration paths, then document env metadata clearly.

## Policy-level caution

Prompt caching and context stability are first-class concerns in Hermes architecture.
Avoid mid-conversation changes that invalidate cache assumptions unless explicitly designed (e.g., compression flow).

## Good first contribution themes

- docs accuracy and broken-link fixes
- optional skill quality upgrades
- diagnostics and doctor improvements
- safer defaults for tool execution backends
- test coverage around edge-case tool behavior
