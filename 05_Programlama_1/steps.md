# Reproduce the C log analyzer

Requires a C compiler such as GCC. The program reads and writes paths relative to the course folder.
From the repository root, in a shell with GCC:

```sh
cd 05_Programlama_1
gcc -std=c11 -Wall -Wextra -Werror evidence/artifacts/lab01_log_analyzer.c -o lab01_log_analyzer
./lab01_log_analyzer
```

On Windows the executable may be named `lab01_log_analyzer.exe`.
The program rewrites `evidence/artifacts/lab01_report.csv`; review the result before committing generated output.

Expected: 10 events, 6 failed logins, 5 hits on the fixture's predefined review IPs, and `failed_login_threshold_exceeded,true`.
This flag means at least three failed logins across the file. It does not measure a time window, group failures by identity/IP, or prove an attack.

The source skips malformed lines and recognizes only the demonstrated input format. The predefined IP list is part of the fictional fixture, not a threat-intelligence feed.
Historical screenshots may show the previous misleading metric name, `ioc_failed_login_burst`.

From the repository root, run the automated fixture check with Python 3.10+ and GCC installed:

```sh
python tools/check_c_example.py
```
