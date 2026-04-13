#!/usr/bin/env bash
# setup-server.sh — One-time Hetzner server setup for produtovivo.com
# Run as root on the Hetzner server (IP: 5.223.73.101)
# DNS A record must already point produtovivo.com → 5.223.73.101 before running certbot.
#
# IMPORTANT: Do NOT touch port 8080 (another company's production environment).
set -euo pipefail

DOMAIN="produtovivo.com"
REPO_URL="https://github.com/cesar-wild/produtovivo"
REPO_DIR="/opt/produtovivo"
EMAIL="tech@produtovivo.com"   # Used for Let's Encrypt expiry notices

echo "========================================"
echo " ProdutoVivo — Server Setup"
echo " Target: ${DOMAIN}"
echo "========================================"

# 1. System updates
echo "==> Updating system packages..."
apt-get update -y && apt-get upgrade -y

# 2. Install Docker (if not present)
if ! command -v docker &>/dev/null; then
  echo "==> Installing Docker..."
  curl -fsSL https://get.docker.com | bash
  systemctl enable docker
  systemctl start docker
fi

# 3. Install docker-compose plugin (v2)
if ! docker compose version &>/dev/null; then
  echo "==> Installing Docker Compose plugin..."
  apt-get install -y docker-compose-plugin
fi

# 4. Install nginx
if ! command -v nginx &>/dev/null; then
  echo "==> Installing nginx..."
  apt-get install -y nginx
fi

# 5. Install certbot
if ! command -v certbot &>/dev/null; then
  echo "==> Installing certbot..."
  apt-get install -y certbot python3-certbot-nginx
fi

# 6. Clone or update repo
echo "==> Setting up repo at ${REPO_DIR}..."
if [ -d "${REPO_DIR}/.git" ]; then
  git -C "${REPO_DIR}" pull origin main
else
  git clone "${REPO_URL}" "${REPO_DIR}"
fi

# 7. Create .env from example if it doesn't exist
if [ ! -f "${REPO_DIR}/.env" ]; then
  echo "==> Creating .env from template..."
  cp "${REPO_DIR}/.env.example" "${REPO_DIR}/.env"
  chmod 600 "${REPO_DIR}/.env"
  echo ""
  echo "!!! ACTION REQUIRED: Fill in secrets in ${REPO_DIR}/.env"
  echo "    - DATABASE_URL"
  echo "    - STRIPE_SECRET_KEY"
  echo "    - STRIPE_WEBHOOK_SECRET"
  echo "    - STRIPE_PRICE_ID"
  echo "    - RESEND_API_KEY"
  echo "    - DOWNLOAD_SECRET (run: openssl rand -hex 32)"
  echo ""
fi

# 8. Install nginx site config
echo "==> Installing nginx config..."
cp "${REPO_DIR}/nginx/produtovivo.conf" /etc/nginx/sites-available/produtovivo.conf

# Disable default site if present
if [ -L /etc/nginx/sites-enabled/default ]; then
  rm /etc/nginx/sites-enabled/default
fi

# Enable produtovivo site
if [ ! -L /etc/nginx/sites-enabled/produtovivo.conf ]; then
  ln -s /etc/nginx/sites-available/produtovivo.conf /etc/nginx/sites-enabled/produtovivo.conf
fi

# 9. Obtain SSL certificate (HTTP-01 challenge via nginx)
# The nginx config handles HTTP for ACME challenge and redirects everything else to HTTPS.
# We need a temporary HTTP-only config to get the first cert.
echo "==> Obtaining Let's Encrypt certificate for ${DOMAIN}..."

# Temporarily serve HTTP so certbot can do ACME challenge
# Use standalone mode with webroot
mkdir -p /var/www/certbot

# Get cert using webroot (nginx must be running)
nginx -t && systemctl restart nginx

certbot certonly \
  --webroot \
  --webroot-path /var/www/certbot \
  --non-interactive \
  --agree-tos \
  --email "${EMAIL}" \
  -d "${DOMAIN}" \
  -d "www.${DOMAIN}" \
  || true  # Don't fail if cert already exists

# 10. Test nginx config and reload
echo "==> Testing nginx config..."
nginx -t && systemctl reload nginx

# 11. Set up certbot auto-renewal (already installed via package, but ensure timer is active)
systemctl enable certbot.timer 2>/dev/null || true
systemctl start certbot.timer 2>/dev/null || true

# Add a renewal hook to reload nginx after cert renewal
mkdir -p /etc/letsencrypt/renewal-hooks/deploy
cat > /etc/letsencrypt/renewal-hooks/deploy/reload-nginx.sh <<'EOF'
#!/bin/bash
systemctl reload nginx
EOF
chmod +x /etc/letsencrypt/renewal-hooks/deploy/reload-nginx.sh

# 12. Set up UFW firewall (if available)
if command -v ufw &>/dev/null; then
  echo "==> Configuring firewall..."
  ufw allow 22/tcp   # SSH
  ufw allow 80/tcp   # HTTP (for ACME + redirect)
  ufw allow 443/tcp  # HTTPS
  ufw --force enable
fi

echo ""
echo "========================================"
echo " Setup complete!"
echo ""
echo " Next steps:"
echo " 1. Fill in ${REPO_DIR}/.env with real secrets (if not done)"
echo " 2. Run: cd ${REPO_DIR} && ./deploy.sh"
echo " 3. Verify: curl https://${DOMAIN}/health"
echo " 4. Set Stripe webhook URL to: https://${DOMAIN}/webhook/stripe"
echo "========================================"
