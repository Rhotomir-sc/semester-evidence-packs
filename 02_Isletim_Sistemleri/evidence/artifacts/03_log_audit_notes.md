# Log Audit Notes (Kali)

## What I checked
- `/var/log/auth.log` (auth/sudo/ssh)
- `journalctl -p 3 -xb` (high priority)
- `journalctl -u ssh --since "today"` (ssh events)

## Findings
- SSH service: (running / not running) + port (22 / custom)
- Failed logins: (yes/no)
- Sudo usage: (yes/no)
- High priority errors: (yes/no)

## Evidence
- `01_users_sudo.png`
- `02_services_ports.png`
- `03_logs.png`

