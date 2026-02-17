# Baseline Commands (Kali)

## Identity / sudo
- `whoami`
- `id`
- `groups`
- `sudo -l`

## Services / ports
- `systemctl --type=service --state=running | head -n 30`
- `ss -tulpn`

## Logs
- `sudo tail -n 60 /var/log/auth.log`
- `journalctl -p 3 -xb | tail -n 60`
- `journalctl -u ssh --since "today" | tail -n 60`

