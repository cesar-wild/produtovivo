#!/bin/bash
# bootstrap-deploy.sh — one-time setup to enable GitHub Actions deploys + run first deploy.
#
# Run ONCE on the production server (5.223.73.101) as root.
# After this, every push to main auto-deploys via GitHub Actions.
#
# Usage (from Hetzner Cloud Console, logged in as root):
#   curl -sSL https://raw.githubusercontent.com/cesar-wild/produtovivo/main/scripts/bootstrap-deploy.sh | bash
set -e

DEPLOY_KEY='ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQDe9elor60yICQG+CHYgUmZ1ZVJkae6UF7ruo5+zIF+eC+fS5G+JWBEV8g0CrEOdqanvIZlHv3sb//qXkfHigdkTH5b4XU86H05bjwJgMTs0ohufwg2Ex4m3G1FRzzKrmwqLRACeioV48HuH4BgQ3bmYLnaWEAXiSN8zaew0RP1rt97PRvBhkMnxe35KiKZzqrpvkpJvMgSHVSv0Rd39RKTB++/+i58LkLxKKVNGInuJTz9HaD/9bPrLbxDeYqBDDgiL/lNrZwiwppZLL/0ZALgSpqVKcu/tJGkr3VwyGF3+2HGLuHkh+5UWlbURCLTaBgrTcyw7nbP/T8UYqQMQ+DcDCK+p1i2aCAy7mTtRTWB85q5zag5/lruvT7ztJyQWOMk2SvpblNwaTK6Y3OXY19yK0nOlXCc4JBczBLhKf3KjItUfZKl+B+KO0MLhwiBvaihzzItn93Qxn2uE9oTh+ToGxTT33z7bz71KZaRcbRSGS41Ls1PMo15GpvBjDqIA3L3Yt0P1nfOexdUiC5Yvingg6wC62PvQkKHlpe+mezHu3NSA/T4v7wFrT/G43SKQlP+a6N4bD58xTnH+aopLffe1dcYdFYIji9AKylO36Vztp9vcODsiyN2V5f4HnWcTFJsFT6k3RQhCNqFANStlleQQmS+mDIp7DidtP1V1p6rBQ== produtovivo-github-actions@cesar-wild'

KEY_TAG='produtovivo-github-actions@cesar-wild'

echo "[bootstrap] Installing GitHub Actions deploy key..."
mkdir -p /root/.ssh
chmod 700 /root/.ssh
touch /root/.ssh/authorized_keys
chmod 600 /root/.ssh/authorized_keys

if grep -qF "$KEY_TAG" /root/.ssh/authorized_keys; then
  echo "[bootstrap] Deploy key already present — skipping append."
else
  echo "$DEPLOY_KEY" >> /root/.ssh/authorized_keys
  echo "[bootstrap] Deploy key installed."
fi

echo "[bootstrap] Running first deploy..."
APP_DIR="/opt/produtovivo"
if [ ! -d "$APP_DIR" ]; then
  echo "[bootstrap] ERROR: $APP_DIR not found. Aborting."
  exit 1
fi

cd "$APP_DIR"
bash scripts/deploy.sh

echo ""
echo "[bootstrap] Done. Future pushes to main will auto-deploy via GitHub Actions."
