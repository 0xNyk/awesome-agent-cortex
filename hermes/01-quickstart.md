# Hermes Quickstart

## 1) Install

Canonical installer:

```bash
curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash
```

Supported: Linux, macOS, WSL2.
Native Windows is not currently supported by upstream (use WSL2).

After install:

```bash
source ~/.bashrc   # or ~/.zshrc
hermes
```

## 2) Day-1 command set

```bash
hermes              # interactive CLI chat
hermes model        # choose provider/model
hermes tools        # enable/disable tools by platform
hermes config set   # set config keys
hermes setup        # full setup wizard
hermes doctor       # diagnostics
hermes update       # upgrade
hermes gateway      # run messaging gateway
```

## 3) Minimal first-session flow

1. Run `hermes setup`
2. Pick provider/model
3. Confirm toolset policy for your environment
4. Run `hermes` and execute one safe tool task (e.g., read/search files)
5. Run `hermes doctor` if anything fails

## 4) Operator sanity checks

- Check config exists: `~/.hermes/config.yaml`
- Check env exists: `~/.hermes/.env`
- Check session DB exists after first run: `~/.hermes/state.db`
- Confirm working directory behavior:
  - CLI uses current directory
  - messaging defaults to `MESSAGING_CWD`

## 5) Fast troubleshooting

- Bad provider auth: verify key in `~/.hermes/.env`
- Missing command after install: reload shell rc, confirm `~/.local/bin` on PATH
- Tool unavailable: check `hermes tools` and provider prerequisites
