# Commands Used (Kali)

## Identity / sudo
- whoami
- id
- groups
- sudo -l

## Services / ports
- systemctl --type=service --state=running
- ss -tulpn

## Logs
- sudo tail -n 80 /var/log/auth.log
- journalctl -p 3 -xb | tail -n 80
