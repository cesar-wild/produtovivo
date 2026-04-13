#!/usr/bin/env bash
# deploy.sh — pull latest from GitHub and restart the ProdutoVivo container
set -euo pipefail

REPO="github.com/cesar-wild/produtovivo"
CONTAINER="produtovivo"
PORT=8082

echo "==> Deploying ProdutoVivo from ${REPO}"

# Pull latest code
cd /opt/produtovivo 2>/dev/null || (git clone https://${REPO} /opt/produtovivo && cd /opt/produtovivo)
git -C /opt/produtovivo pull origin main

# Build and restart container
docker build -t produtovivo:latest /opt/produtovivo

docker stop ${CONTAINER} 2>/dev/null || true
docker rm ${CONTAINER} 2>/dev/null || true

docker run -d \
  --name ${CONTAINER} \
  --restart unless-stopped \
  -p ${PORT}:${PORT} \
  --env-file /opt/produtovivo/.env \
  produtovivo:latest

echo "==> ProdutoVivo running on port ${PORT}"
curl -sf http://localhost:${PORT}/health && echo "Health check: OK"
