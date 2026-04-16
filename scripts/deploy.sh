#!/bin/bash
# deploy.sh — run on Hetzner to pull latest code and restart the docker container
# Usage: bash scripts/deploy.sh
# Called by GitHub Actions (via SSH) on every push to main.
set -e

APP_DIR="/opt/produtovivo"
COMPOSE_FILE="docker-compose.prod.yml"

echo "[deploy] Pulling latest code..."
cd "$APP_DIR"
git pull origin main

echo "[deploy] Rebuilding and restarting docker container..."
GIT_SHA=$(git rev-parse --short HEAD)
BUILT_AT=$(date -u +"%Y-%m-%dT%H:%M:%SZ")
echo "[deploy] SHA: $GIT_SHA  built_at: $BUILT_AT"
docker compose -f "$COMPOSE_FILE" build --build-arg GIT_SHA="$GIT_SHA" --build-arg BUILT_AT="$BUILT_AT"
docker compose -f "$COMPOSE_FILE" up -d

echo "[deploy] Waiting for container to come up..."
sleep 6

echo "[deploy] Health check..."
curl -sf http://localhost:3000/health && echo "[deploy] OK" || { echo "[deploy] Health check FAILED"; docker compose -f "$COMPOSE_FILE" logs --tail=50 produtovivo; exit 1; }
