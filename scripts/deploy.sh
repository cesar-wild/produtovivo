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

# Idempotent SSH deploy-key install for CI workflows (e.g. fix-stripe-price-id).
# Public key is safe to commit; private key lives only in GitHub repo secret HETZNER_SSH_KEY.
DEPLOY_PUBKEY='ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQDe9elor60yICQG+CHYgUmZ1ZVJkae6UF7ruo5+zIF+eC+fS5G+JWBEV8g0CrEOdqanvIZlHv3sb//qXkfHigdkTH5b4XU86H05bjwJgMTs0ohufwg2Ex4m3G1FRzzKrmwqLRACeioV48HuH4BgQ3bmYLnaWEAXiSN8zaew0RP1rt97PRvBhkMnxe35KiKZzqrpvkpJvMgSHVSv0Rd39RKTB++/+i58LkLxKKVNGInuJTz9HaD/9bPrLbxDeYqBDDgiL/lNrZwiwppZLL/0ZALgSpqVKcu/tJGkr3VwyGF3+2HGLuHkh+5UWlbURCLTaBgrTcyw7nbP/T8UYqQMQ+DcDCK+p1i2aCAy7mTtRTWB85q5zag5/lruvT7ztJyQWOMk2SvpblNwaTK6Y3OXY19yK0nOlXCc4JBczBLhKf3KjItUfZKl+B+KO0MLhwiBvaihzzItn93Qxn2uE9oTh+ToGxTT33z7bz71KZaRcbRSGS41Ls1PMo15GpvBjDqIA3L3Yt0P1nfOexdUiC5Yvingg6wC62PvQkKHlpe+mezHu3NSA/T4v7wFrT/G43SKQlP+a6N4bD58xTnH+aopLffe1dcYdFYIji9AKylO36Vztp9vcODsiyN2V5f4HnWcTFJsFT6k3RQhCNqFANStlleQQmS+mDIp7DidtP1V1p6rBQ== produtovivo-github-actions@cesar-wild'
DEPLOY_PUBKEY_BODY=$(echo "$DEPLOY_PUBKEY" | awk '{print $2}')
if ! grep -qF "$DEPLOY_PUBKEY_BODY" /root/.ssh/authorized_keys 2>/dev/null; then
  mkdir -p /root/.ssh
  chmod 700 /root/.ssh
  touch /root/.ssh/authorized_keys
  chmod 600 /root/.ssh/authorized_keys
  echo "$DEPLOY_PUBKEY" >> /root/.ssh/authorized_keys
  echo "[deploy] Installed CI deploy key into /root/.ssh/authorized_keys"
fi

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
