#!/usr/bin/env bash
# deploy.sh — pull latest from GitHub and restart the ProdutoVivo PRODUCTION container
# Production: app runs internally on 8082, exposed at 127.0.0.1:3000, nginx proxies 443 → 3000
# Dev/staging stays on port 8082 (container: produtovivo-dev)
set -euo pipefail

REPO_URL="https://github.com/cesar-wild/produtovivo"
REPO_DIR="/opt/produtovivo"
COMPOSE_FILE="docker-compose.prod.yml"
HEALTH_URL="http://127.0.0.1:3000/health"

echo "==> Deploying ProdutoVivo (production) from ${REPO_URL}"

# Clone or pull latest code
if [ -d "${REPO_DIR}/.git" ]; then
  echo "==> Pulling latest..."
  git -C "${REPO_DIR}" pull origin main
else
  echo "==> Cloning repo..."
  git clone "${REPO_URL}" "${REPO_DIR}"
fi

cd "${REPO_DIR}"

# Ensure .env exists
if [ ! -f "${REPO_DIR}/.env" ]; then
  echo "ERROR: .env file not found at ${REPO_DIR}/.env"
  echo "       Copy .env.example, fill in secrets, then re-run deploy.sh"
  exit 1
fi

# Build and restart production container
echo "==> Building and starting production container..."
docker compose -f "${COMPOSE_FILE}" pull 2>/dev/null || true
docker compose -f "${COMPOSE_FILE}" up -d --build

echo "==> Waiting for app to be ready..."
for i in $(seq 1 12); do
  if curl -sf "${HEALTH_URL}" > /dev/null 2>&1; then
    echo "Health check: OK"
    break
  fi
  if [ "$i" -eq 12 ]; then
    echo "ERROR: Health check failed after 60s"
    docker compose -f "${COMPOSE_FILE}" logs --tail=50
    exit 1
  fi
  echo "   Waiting... (${i}/12)"
  sleep 5
done

echo "==> ProdutoVivo production is live at https://produtovivo.com"
curl -s "${HEALTH_URL}"
echo ""
