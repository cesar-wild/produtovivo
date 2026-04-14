#!/bin/bash
# deploy.sh — run on Hetzner to pull latest code and restart the service
# Usage: bash scripts/deploy.sh
# Called by GitHub Actions (via SSH) on every push to main.
set -e

APP_DIR="/opt/produtovivo"
SERVICE="produtovivo"

echo "[deploy] Pulling latest code..."
cd "$APP_DIR"
git pull origin main

echo "[deploy] Installing production dependencies..."
npm install --omit=dev

echo "[deploy] Restarting service..."
sudo systemctl restart "$SERVICE"

echo "[deploy] Waiting for service to come up..."
sleep 4

echo "[deploy] Health check..."
curl -sf http://localhost:8082/health && echo "[deploy] OK" || { echo "[deploy] Health check FAILED"; exit 1; }
