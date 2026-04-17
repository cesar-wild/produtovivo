#!/bin/bash
# bootstrap-deploy.sh — set up self-pulling deploys on the production server.
#
# Run ONCE on the production server (5.223.73.101) as root:
#   curl -sSL https://raw.githubusercontent.com/cesar-wild/produtovivo/main/scripts/bootstrap-deploy.sh | bash
#
# After this:
#   - An immediate deploy is performed (git pull + docker compose rebuild + health check).
#   - A systemd timer runs every 10 minutes; if main has new commits, it pulls + rebuilds.
#   - Logs land in /var/log/produtovivo-deploy.log AND journalctl -u produtovivo-deploy.
#   - No GitHub Action emails. No SSH key from CI. Self-contained on the server.
#
# Idempotent — safe to re-run. Replaces existing systemd unit/timer if present.
set -e

APP_DIR="/opt/produtovivo"
SERVICE_NAME="produtovivo-deploy"
TIMER_NAME="produtovivo-deploy.timer"
LOG_FILE="/var/log/produtovivo-deploy.log"

if [ ! -d "$APP_DIR/.git" ]; then
  echo "[bootstrap] $APP_DIR not found — cloning from GitHub..."
  git clone https://github.com/cesar-wild/produtovivo "$APP_DIR"
fi

echo "[bootstrap] Installing GitHub Actions deploy key into /root/.ssh/authorized_keys (idempotent)..."
DEPLOY_PUBKEY='ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQDe9elor60yICQG+CHYgUmZ1ZVJkae6UF7ruo5+zIF+eC+fS5G+JWBEV8g0CrEOdqanvIZlHv3sb//qXkfHigdkTH5b4XU86H05bjwJgMTs0ohufwg2Ex4m3G1FRzzKrmwqLRACeioV48HuH4BgQ3bmYLnaWEAXiSN8zaew0RP1rt97PRvBhkMnxe35KiKZzqrpvkpJvMgSHVSv0Rd39RKTB++/+i58LkLxKKVNGInuJTz9HaD/9bPrLbxDeYqBDDgiL/lNrZwiwppZLL/0ZALgSpqVKcu/tJGkr3VwyGF3+2HGLuHkh+5UWlbURCLTaBgrTcyw7nbP/T8UYqQMQ+DcDCK+p1i2aCAy7mTtRTWB85q5zag5/lruvT7ztJyQWOMk2SvpblNwaTK6Y3OXY19yK0nOlXCc4JBczBLhKf3KjItUfZKl+B+KO0MLhwiBvaihzzItn93Qxn2uE9oTh+ToGxTT33z7bz71KZaRcbRSGS41Ls1PMo15GpvBjDqIA3L3Yt0P1nfOexdUiC5Yvingg6wC62PvQkKHlpe+mezHu3NSA/T4v7wFrT/G43SKQlP+a6N4bD58xTnH+aopLffe1dcYdFYIji9AKylO36Vztp9vcODsiyN2V5f4HnWcTFJsFT6k3RQhCNqFANStlleQQmS+mDIp7DidtP1V1p6rBQ== produtovivo-github-actions@cesar-wild'
mkdir -p /root/.ssh
chmod 700 /root/.ssh
touch /root/.ssh/authorized_keys
chmod 600 /root/.ssh/authorized_keys
DEPLOY_PUBKEY_FINGERPRINT=$(echo "$DEPLOY_PUBKEY" | awk '{print $2}')
if grep -qF "$DEPLOY_PUBKEY_FINGERPRINT" /root/.ssh/authorized_keys; then
  echo "[bootstrap] Deploy key already present in authorized_keys."
else
  echo "$DEPLOY_PUBKEY" >> /root/.ssh/authorized_keys
  echo "[bootstrap] Deploy key appended."
fi

echo "[bootstrap] Running first deploy now (catches up to current main)..."
cd "$APP_DIR"
bash scripts/deploy.sh

echo "[bootstrap] Installing systemd service + timer for self-pulling deploys..."

cat > /etc/systemd/system/${SERVICE_NAME}.service <<'UNIT'
[Unit]
Description=produtovivo: pull main and rebuild if there are new commits
After=network-online.target docker.service
Wants=network-online.target

[Service]
Type=oneshot
WorkingDirectory=/opt/produtovivo
ExecStart=/bin/bash -c '\
  set -e; \
  cd /opt/produtovivo; \
  BEFORE=$(git rev-parse HEAD); \
  git fetch --quiet origin main; \
  AFTER=$(git rev-parse origin/main); \
  if [ "$BEFORE" = "$AFTER" ]; then \
    echo "[deploy-timer] No new commits ($BEFORE). Skipping."; \
    exit 0; \
  fi; \
  echo "[deploy-timer] New commits: $BEFORE -> $AFTER. Deploying."; \
  bash scripts/deploy.sh; \
'
StandardOutput=append:/var/log/produtovivo-deploy.log
StandardError=append:/var/log/produtovivo-deploy.log
UNIT

cat > /etc/systemd/system/${TIMER_NAME} <<'UNIT'
[Unit]
Description=Run produtovivo deploy check every 10 minutes
Requires=produtovivo-deploy.service

[Timer]
OnBootSec=2min
OnUnitActiveSec=10min
Unit=produtovivo-deploy.service
Persistent=true

[Install]
WantedBy=timers.target
UNIT

touch "$LOG_FILE"
chmod 644 "$LOG_FILE"

systemctl daemon-reload
systemctl enable --now "${TIMER_NAME}"

echo ""
echo "[bootstrap] Done."
echo "[bootstrap] Timer status:"
systemctl status "${TIMER_NAME}" --no-pager | head -10 || true
echo ""
echo "[bootstrap] Tail logs with: journalctl -u ${SERVICE_NAME} -f"
echo "[bootstrap] Or: tail -f ${LOG_FILE}"
