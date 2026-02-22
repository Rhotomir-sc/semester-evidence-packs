# Findings — Kali Baseline + Log Audit

## Observations
- **User / groups:** user `aykan` is part of `sudo` and `users` groups (least-privilege baseline confirmed).
- **Sudo capability:** `sudo -l` confirms the user can execute commands as root (expected for lab admin user).
- **Running services (notable):**
  - `NetworkManager` (network management)
  - `open-vm-tools` (VM integration; expected if running in VMware)
  - `systemd-timesyncd` (time sync; supports reliable logging)
- **Listening ports (notable):**
  - Observed a UDP listener during the snapshot (baseline recorded for future comparison).
- **Auth log source:** `/var/log/auth.log` was not present on this build; authentication events were validated via `journalctl` (journald).
- **Auth/journal highlights:**
  - `sudo` events show who executed privileged commands and when (USER + COMMAND fields).
  - `pam_unix(sudo:session)` open/close entries confirm privilege escalation sessions.

## Risk notes (short)
- Review unnecessary services if this host is used beyond lab work.
- Keep a baseline snapshot; compare future captures to detect unexpected new listeners/services.

## Evidence
- Screenshots:
  - `lab01_users_sudo.png`
  - `lab01_services_ports.png`
  - `lab01_logs_auth.png`
- Script:
  - `lab01_baseline_check.sh`
