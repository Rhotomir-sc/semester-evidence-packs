## Filters used
- `dns`
- `tls.handshake`

## Findings
- DNS queries/responses observed → name resolution baseline confirmed.
- TLS handshakes observed (ClientHello/ServerHello) → HTTPS session establishment validated.
- Baseline PCAP is suitable for later anomaly comparison (unexpected DNS volume, unknown destinations, handshake failures).
