#!/usr/bin/env python3
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Tuple

SUSPICIOUS_IPS = {"203.0.113.77", "198.51.100.23"}
SENSITIVE_CMDS = {"/etc/shadow", "shadow", "passwd"}

@dataclass
class Event:
    ts: str
    user: str
    ip: str
    action: str
    status: str
    cmd: str = ""

def parse_kv_line(line: str) -> Dict[str, str]:
    parts = line.strip().split()
    if not parts:
        return {}
    ts = parts[0]
    kv: Dict[str, str] = {"ts": ts}
    for p in parts[1:]:
        if "=" not in p:
            continue
        k, v = p.split("=", 1)
        kv[k] = v.strip('"')
    return kv

def to_event(kv: Dict[str, str]) -> Event:
    return Event(
        ts=kv.get("ts", ""),
        user=kv.get("user", "unknown"),
        ip=kv.get("ip", "0.0.0.0"),
        action=kv.get("action", "unknown"),
        status=kv.get("status", "unknown"),
        cmd=kv.get("cmd", ""),
    )

def detect_iocs(events: List[Event]) -> List[str]:
    hits: List[str] = []
    # IOC 1: suspicious IPs
    for e in events:
        if e.ip in SUSPICIOUS_IPS:
            hits.append(f"[IOC] Suspicious IP seen: {e.ip} ({e.action}, {e.status}) at {e.ts}")

    # IOC 2: sensitive command attempts
    for e in events:
        if e.action == "sudo_cmd" and any(x in e.cmd for x in SENSITIVE_CMDS):
            hits.append(f"[IOC] Sensitive command attempt by {e.user} from {e.ip}: {e.cmd} ({e.status})")

    # IOC 3: failed login burst per IP (>=3 fails)
    fails_by_ip: Dict[str, int] = {}
    for e in events:
        if e.action == "login" and e.status == "fail":
            fails_by_ip[e.ip] = fails_by_ip.get(e.ip, 0) + 1
    for ip, cnt in fails_by_ip.items():
        if cnt >= 3:
            hits.append(f"[IOC] Failed-login burst: {cnt} fails from {ip}")

    return hits

def summarize(events: List[Event]) -> str:
    total = len(events)
    by_action: Dict[str, int] = {}
    by_status: Dict[str, int] = {}
    for e in events:
        by_action[e.action] = by_action.get(e.action, 0) + 1
        by_status[e.status] = by_status.get(e.status, 0) + 1

    lines = []
    lines.append(f"Total events: {total}")
    lines.append("Events by action:")
    for k in sorted(by_action):
        lines.append(f"  - {k}: {by_action[k]}")
    lines.append("Events by status:")
    for k in sorted(by_status):
        lines.append(f"  - {k}: {by_status[k]}")
    return "\n".join(lines)

def main() -> None:
    in_path = Path("evidence/artifacts/lab01_sample.log")
    out_path = Path("evidence/artifacts/lab01_output.txt")

    raw = in_path.read_text(encoding="utf-8").splitlines()
    events = [to_event(parse_kv_line(line)) for line in raw if line.strip()]

    summary = summarize(events)
    iocs = detect_iocs(events)

    report_lines = [summary, "", "IOC hits:"]
    report_lines.extend(iocs if iocs else ["(none)"])
    out_path.write_text("\n".join(report_lines) + "\n", encoding="utf-8")

    print(report_lines[0])
    print("Written:", out_path)

if __name__ == "__main__":
    main()
