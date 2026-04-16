#!/usr/bin/env bash
# auto-deploy.sh — ProdutoVivo continuous deploy script
# Invoked every 2 minutes by produtovivo-autodeploy.timer via systemd.
#
# Behaviour:
#   - Fetches origin/main on every tick (always logs a journal entry)
#   - If origin/main is ahead of HEAD: git pull --ff-only, then systemctl restart produtovivo
#   - If git pull fails (conflict, network), logs ERROR and exits non-zero — does NOT restart
#   - Never touches port 8080 or any service outside the produtovivo stack
#
# Logs are visible via: journalctl -t produtovivo-autodeploy -f

set -euo pipefail

REPO_DIR="/opt/produtovivo"
TAG="produtovivo-autodeploy"

log_info()  { logger -t "$TAG" "INFO:    $*"; }
log_noop()  { logger -t "$TAG" "NOOP:    $*"; }
log_error() { logger -t "$TAG" "ERROR:   $*"; }
log_ok()    { logger -t "$TAG" "SUCCESS: $*"; }

# Safety guard — this script must only operate on the produtovivo repo
if [ ! -f "${REPO_DIR}/docker-compose.prod.yml" ]; then
  log_error "REPO_DIR=${REPO_DIR} does not look like the produtovivo repo — aborting"
  exit 1
fi

# Every tick logs — this is the audit trail the CEO asked for
log_info "tick — checking origin/main at $(date -u '+%Y-%m-%dT%H:%M:%SZ')"

# Fetch without modifying the working tree
if ! git -C "$REPO_DIR" fetch origin main 2>&1; then
  log_error "git fetch failed — network issue? Skipping this tick."
  exit 1
fi

LOCAL=$(git  -C "$REPO_DIR" rev-parse HEAD)
REMOTE=$(git -C "$REPO_DIR" rev-parse origin/main)

if [ "$LOCAL" = "$REMOTE" ]; then
  log_noop "already at ${LOCAL:0:12} — nothing to deploy"
  exit 0
fi

BEHIND=$(git -C "$REPO_DIR" rev-list HEAD..origin/main --count)
log_info "update available: HEAD=${LOCAL:0:12} origin/main=${REMOTE:0:12} (${BEHIND} commit(s) behind)"

# Pull fast-forward only — exit non-zero if diverged or conflicted; do NOT restart broken state
if ! git -C "$REPO_DIR" pull --ff-only origin main; then
  log_error "git pull --ff-only failed (diverged branch or conflict) — NOT restarting. Next tick will retry."
  exit 1
fi

log_info "git pull succeeded — restarting produtovivo"

# Restart the systemd service (which runs docker compose up -d --build)
if ! systemctl restart produtovivo; then
  log_error "systemctl restart produtovivo failed after pulling ${REMOTE:0:12}"
  exit 1
fi

log_ok "deployed ${REMOTE:0:12} — produtovivo restarted"
