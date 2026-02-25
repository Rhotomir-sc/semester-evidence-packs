# Plan — Mini-Lab 01: Wireshark Baseline + DNS/TLS

## Goal
- Capture a short baseline PCAP and validate protocol visibility (DNS + TLS handshake).
- Package evidence for future anomaly comparison.

## Scope
- Interface: eth0 (Kali VM)
- Duration: 3–5 minutes
- Activities: browse 2–3 HTTPS sites

## Outputs
- PCAP: `evidence/artifacts/lab01_baseline.pcapng`
- Findings: `evidence/artifacts/lab01_filters_and_findings.md`

## Evidence to collect
- Screenshots:
  - `lab01_capture_overview.png`
  - `lab01_dns_filter.png`
  - `lab01_tls_handshake.png`

## Success criteria
- PCAP saved and accessible via “View raw”.
- DNS packets visible under `dns` filter.
- TLS handshakes visible under `tls.handshake` filter.
