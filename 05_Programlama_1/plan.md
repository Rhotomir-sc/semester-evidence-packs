# Plan — Mini-Lab 01: C Log Analyzer → CSV Report

## Goal
- Demonstrate core C fundamentals (file I/O, string parsing, structs/fields, counters).
- Convert raw text logs into a structured CSV output suitable for reporting.

## Inputs / Outputs
- Input: `evidence/artifacts/lab01_sample.log`
- Output: `evidence/artifacts/lab01_report.csv` (+ `lab01_output.txt` as exported preview)

## Scope
- Parse fixed-format lines (timestamp + key=value fields).
- Compute basic metrics: total events, login_fail/success, sudo_ok/blocked, scan_detected.
- Basic IOC flag: failed login burst (>=3).

## Evidence to collect
- Screenshots:
  - `lab01_compile.png` (compile + exit code 0)
  - `lab01_run_output.png` (program execution)
  - `lab01_csv_preview.png` (CSV preview)
- Artifacts: `.c`, `.log`, `.csv`, `.txt`

## Success criteria
- Program compiles without errors.
- CSV output is generated and readable.
- README links match real filenames.
