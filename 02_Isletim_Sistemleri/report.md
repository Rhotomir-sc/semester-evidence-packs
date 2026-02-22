# Report — Kali Baseline Hardening + Log Audit Pack

## Summary
- I collected a Kali Linux baseline (identity/sudo, running services, open ports) and documented it as an evidence pack.
- I validated authentication/privilege events using `journalctl` and packaged the proof with screenshots and reproducible commands.
- I added a small baseline script to make checks repeatable and easy to rerun.

## Key outputs
- Artifacts:
  - `evidence/artifacts/lab01_commands_used.md`
  - `evidence/artifacts/lab01_baseline_check.sh`
  - `evidence/artifacts/lab01_findings.md`
- Screenshots:
  - `evidence/screenshots/lab01_users_sudo.png`
  - `evidence/screenshots/lab01_services_ports.png`
  - `evidence/screenshots/lab01_logs_auth.png`

## What I learned (HR-friendly)
- How to validate least privilege and sudo visibility on a Linux host.
- How to map attack surface quickly via running services and listening ports.
- How to use journald (`journalctl`) to confirm sudo sessions and authentication-related events when classic log files are not present.
- How to package audit evidence in a structured, reproducible format suitable for SOC/IR workflows.

## Improvements (next time)
- Add a before/after hardening step (disable unused services and compare evidence).
- Add an optional sanitization step to remove usernames/IPs for public sharing.
