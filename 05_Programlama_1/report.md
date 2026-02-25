# Report — Mini-Lab 01: C Log Analyzer → CSV

## Summary
- I implemented a small C program that parses structured log lines and generates a CSV metrics report.
- I validated compilation, execution, and output correctness using terminal evidence and screenshots.

## Evidence
### Artifacts
- `evidence/artifacts/lab01_log_analyzer.c`
- `evidence/artifacts/lab01_sample.log`
- `evidence/artifacts/lab01_report.csv`
- `evidence/artifacts/lab01_output.txt`

### Screenshots
- `evidence/screenshots/lab01_compile.png`
- `evidence/screenshots/lab01_run_output.png`
- `evidence/screenshots/lab01_csv_preview.png`

## Results (from CSV)
- Total events: **10**
- login_fail: **6**
- suspicious_ip_hits: **5**
- IOC flag: **true** (failed-login burst)

## What I learned (HR-friendly)
- How to parse and validate structured text input in C (fgets/sscanf approach).
- How to convert raw logs into measurable metrics and machine-readable output (CSV).
- How to package a reproducible evidence pack for reviewers.

## Improvements
- Add CLI flags (input/output path, threshold).
- Add per-IP aggregation and time-window burst detection.
- Add malformed-line logging and unit tests.
