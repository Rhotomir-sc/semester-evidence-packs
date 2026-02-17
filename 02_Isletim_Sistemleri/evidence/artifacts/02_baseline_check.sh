#!/usr/bin/env bash
set -euo pipefail

echo "=== WHOAMI ==="
whoami || true

echo "=== ID / GROUPS ==="
id || true
groups || true

echo "=== RUNNING SERVICES (top 30) ==="
systemctl --type=service --state=running 2>/dev/null | head -n 30 || true

echo "=== OPEN PORTS ==="
ss -tulpn 2>/dev/null || true

echo "=== AUTH LOG (tail) ==="
sudo tail -n 60 /var/log/auth.log 2>/dev/null || true

echo "=== JOURNAL priority<=3 (tail) ==="
journalctl -p 3 -xb 2>/dev/null | tail -n 60 || true

