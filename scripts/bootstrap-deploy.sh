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

if [ ! -d "$APP_DIR" ]; then
  echo "[bootstrap] ERROR: $APP_DIR not found. Aborting."
  exit 1
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
