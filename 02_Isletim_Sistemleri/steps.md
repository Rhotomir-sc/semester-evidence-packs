# Steps — Operating Systems (Practice & Administration)

1) Open **Event Viewer** → Windows Logs → **Security**
2) Filter current log:
   - Event ID **4624** (successful logon)
   - Event ID **4625** (failed logon)
3) Pick a short time window (e.g., last 24 hours) and note:
   - total counts
   - any unusual pattern (many failures, same account, same source)
4) Take screenshots:
   - filter settings
   - a 4624 event details (Logon Type visible)
   - a 4625 event details (Failure reason visible)
   - overview/counts view
5) (Optional) Export filtered events (EVTX or CSV) and place in `evidence/artifacts/`.
