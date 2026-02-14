# Steps — Operating Systems (Kali Linux)

## Step 1 — System info
- Run: `uname -a`, `lsb_release -a`
- Screenshot: `evidence/screenshots/01_system_info.png`

## Step 2 — Users & permissions
- Run: `whoami`, `id`, `groups`
- Screenshot: `evidence/screenshots/02_user_id.png`

## Step 3 — Services & listening ports
- Run: `systemctl status ssh` (or another service you used), `ss -tulpn`
- Screenshot: `evidence/screenshots/03_services_ports.png`

## Step 4 — Authentication log quick review
- Run (example):
  - `sudo tail -n 60 /var/log/auth.log`
  - `sudo grep -i "failed\\|invalid" /var/log/auth.log | tail -n 30`
- Screenshot: `evidence/screenshots/04_auth_log.png`
- Artifact: save output to `evidence/artifacts/01_auth_log_summary.txt`
