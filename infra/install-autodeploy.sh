#!/usr/bin/env bash
# install-autodeploy.sh — Install ProdutoVivo auto-deploy systemd units on the Hetzner host
#
# Run as root on the server:
#   cd /opt/produtovivo && bash infra/install-autodeploy.sh
#
# What this does:
#   1. Installs produtovivo.service     — Docker Compose wrapper (enables `systemctl restart produtovivo`)
#   2. Installs produtovivo-autodeploy.service — one-shot deploy runner
#   3. Installs produtovivo-autodeploy.timer   — fires every 2 minutes
#   4. Marks auto-deploy.sh executable
#   5. Enables + starts the timer
#
# IMPORTANT: Only touches the produtovivo stack. Never touches port 8080.

set -euo pipefail

REPO_DIR="/opt/produtovivo"
SYSTEMD_DIR="/etc/systemd/system"
UNIT_SRC="${REPO_DIR}/infra/systemd"

echo "========================================"
echo " ProdutoVivo — Auto-deploy installer"
echo "========================================"

# Sanity check
if [ "$(id -u)" -ne 0 ]; then
  echo "ERROR: must be run as root"
  exit 1
fi

if [ ! -f "${REPO_DIR}/docker-compose.prod.yml" ]; then
  echo "ERROR: ${REPO_DIR} does not look like the produtovivo repo"
  exit 1
fi

# Make auto-deploy.sh executable
echo "==> Setting permissions on auto-deploy.sh..."
chmod +x "${REPO_DIR}/scripts/auto-deploy.sh"

# Copy unit files
echo "==> Installing systemd unit files..."
cp "${UNIT_SRC}/produtovivo.service"            "${SYSTEMD_DIR}/produtovivo.service"
cp "${UNIT_SRC}/produtovivo-autodeploy.service" "${SYSTEMD_DIR}/produtovivo-autodeploy.service"
cp "${UNIT_SRC}/produtovivo-autodeploy.timer"   "${SYSTEMD_DIR}/produtovivo-autodeploy.timer"

# Reload systemd
echo "==> Reloading systemd daemon..."
systemctl daemon-reload

# Enable and start the produtovivo service (if not already running via Docker directly)
echo "==> Enabling produtovivo.service..."
systemctl enable produtovivo.service

# Only start if not already active (idempotent — don't bounce a live prod unnecessarily)
if ! systemctl is-active --quiet produtovivo.service; then
  echo "==> Starting produtovivo.service (first install)..."
  systemctl start produtovivo.service
else
  echo "==> produtovivo.service already active — skipping start (timer will handle future deploys)"
fi

# Enable and start the timer
echo "==> Enabling and starting produtovivo-autodeploy.timer..."
systemctl enable produtovivo-autodeploy.timer
systemctl start  produtovivo-autodeploy.timer

echo ""
echo "========================================"
echo " Install complete!"
echo ""
echo " Timer status:"
systemctl status produtovivo-autodeploy.timer --no-pager || true
echo ""
echo " Next timer fire:"
systemctl list-timers produtovivo-autodeploy.timer --no-pager || true
echo ""
echo " Tail deploy logs:"
echo "   journalctl -t produtovivo-autodeploy -f"
echo ""
echo " Verify app is live:"
echo "   curl -s http://127.0.0.1:3000/health"
echo "========================================"
