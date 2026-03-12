# Hermes Deployment Appendix: systemd + docker-compose

Copy/paste deployment patterns for VPS and homelab operators.

Use this appendix with:
- 05-production-profiles.md
- 09-hardening-and-security-baseline.md
- 10-gateway-platform-runbooks.md

## Option A: systemd service (recommended for bare-metal VPS)

## 1) Create service user and directories

```bash
sudo useradd --create-home --shell /bin/bash hermes || true
sudo mkdir -p /opt/hermes
sudo chown -R hermes:hermes /opt/hermes
```

## 2) Install Hermes under service user

```bash
sudo -u hermes -H bash -lc 'python3 -m pip install --user hermes-agent'
sudo -u hermes -H bash -lc 'mkdir -p ~/.hermes'
```

## 3) Add environment file

Create `/etc/hermes/hermes.env`:

```bash
sudo mkdir -p /etc/hermes
sudo tee /etc/hermes/hermes.env >/dev/null <<'EOF'
# Core
HERMES_HOME=/home/hermes/.hermes
MESSAGING_CWD=/opt/hermes/workdir

# Provider example (choose your provider keys)
OPENROUTER_API_KEY=replace_me

# Optional gateway tokens (enable only those you use)
# TELEGRAM_BOT_TOKEN=replace_me
# DISCORD_BOT_TOKEN=replace_me
# SLACK_BOT_TOKEN=replace_me
EOF

sudo chmod 600 /etc/hermes/hermes.env
sudo chown root:root /etc/hermes/hermes.env
sudo -u hermes mkdir -p /opt/hermes/workdir
```

## 4) Create systemd unit

Create `/etc/systemd/system/hermes.service`:

```ini
[Unit]
Description=Hermes Agent
After=network-online.target
Wants=network-online.target

[Service]
Type=simple
User=hermes
Group=hermes
WorkingDirectory=/opt/hermes
EnvironmentFile=/etc/hermes/hermes.env
ExecStart=/home/hermes/.local/bin/hermes
Restart=on-failure
RestartSec=3
NoNewPrivileges=true
PrivateTmp=true
ProtectSystem=full
ProtectHome=false
LimitNOFILE=65535

[Install]
WantedBy=multi-user.target
```

## 5) Enable + verify

```bash
sudo systemctl daemon-reload
sudo systemctl enable --now hermes
sudo systemctl status hermes --no-pager
sudo journalctl -u hermes -n 100 --no-pager
```

## 6) Upgrades

```bash
sudo -u hermes -H bash -lc 'python3 -m pip install --user -U hermes-agent'
sudo systemctl restart hermes
sudo journalctl -u hermes -n 100 --no-pager
```

## Option B: docker-compose (recommended for containerized stacks)

## 1) Project layout

```text
/opt/hermes-stack/
  docker-compose.yml
  .env
  data/
```

## 2) docker-compose.yml

```yaml
services:
  hermes:
    image: ghcr.io/nousresearch/hermes-agent:latest
    container_name: hermes
    restart: unless-stopped
    env_file:
      - .env
    environment:
      - HERMES_HOME=/data/hermes
      - MESSAGING_CWD=/workspace
    volumes:
      - ./data:/data
      - ./workspace:/workspace
    stdin_open: true
    tty: true
```

If you do not have an official image available in your environment, build locally and replace `image` with `build: .` using a project Dockerfile.

## 3) .env template

```bash
OPENROUTER_API_KEY=replace_me
# TELEGRAM_BOT_TOKEN=replace_me
# DISCORD_BOT_TOKEN=replace_me
# SLACK_BOT_TOKEN=replace_me
```

## 4) Bring-up + health checks

```bash
cd /opt/hermes-stack
docker compose pull
docker compose up -d
docker compose ps
docker compose logs --tail=100 hermes
```

## 5) Upgrade flow

```bash
cd /opt/hermes-stack
docker compose pull
docker compose up -d
docker compose logs --tail=100 hermes
```

## Optional: systemd wrapper for docker-compose

Create `/etc/systemd/system/hermes-compose.service`:

```ini
[Unit]
Description=Hermes Agent (docker-compose)
After=docker.service
Requires=docker.service

[Service]
Type=oneshot
WorkingDirectory=/opt/hermes-stack
RemainAfterExit=yes
ExecStart=/usr/bin/docker compose up -d
ExecStop=/usr/bin/docker compose down

[Install]
WantedBy=multi-user.target
```

Then:

```bash
sudo systemctl daemon-reload
sudo systemctl enable --now hermes-compose
sudo systemctl status hermes-compose --no-pager
```

## Backup and restore

Backup:

```bash
tar -czf hermes-backup-$(date +%F).tgz /home/hermes/.hermes /etc/hermes
# or compose mode:
# tar -czf hermes-backup-$(date +%F).tgz /opt/hermes-stack/data /opt/hermes-stack/.env
```

Restore:
1) stop service
2) restore files
3) verify permissions
4) restart and run smoke tests

## Smoke test checklist after deploy

```bash
hermes doctor
hermes model
hermes tools
```

Then run:
- one short prompt
- one tool-light prompt
- one scheduled job dry run (if enabled)

Do not enable broad messaging automation until all smoke checks pass.
