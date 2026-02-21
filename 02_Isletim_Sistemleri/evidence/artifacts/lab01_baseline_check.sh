#!/usr/bin/env bash
set -euo pipefail

echo "=== IDENTITY ==="
whoami || true
id || true
groups || true

echo "=== SUDO RULES ==="
sudo -n true 2>/dev/null && sudo -l || echo "sudo requires password (expected)"

echo "=== RUNNING SERVICES (top 40) ==="
systemctl --type=service --state=running 2>/dev/null | head -n 40 || true

echo "=== LISTENING PORTS ==="
ss -tulpn 2>/dev/null || true

echo "=== AUTH LOG (tail) ==="
sudo tail -n 80 /var/log/auth.log 2>/dev/null || true

echo "=== JOURNAL priority<=3 (tail) ==="
journalctl -p 3 -xb 2>/dev/null | tail -n 80 || true
