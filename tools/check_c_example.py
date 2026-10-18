"""Compile and verify the C fixture in a temporary directory (requires GCC)."""
from pathlib import Path
import csv
import shutil
import subprocess
import tempfile

root = Path(__file__).resolve().parents[1]
source = root / '05_Programlama_1/evidence/artifacts'
compiler = shutil.which('gcc')
if not compiler:
    raise SystemExit('GCC is required for this check; compilation was not performed.')
with tempfile.TemporaryDirectory() as temporary:
    work = Path(temporary)
    artifacts = work / 'evidence/artifacts'
    artifacts.mkdir(parents=True)
    shutil.copyfile(source / 'lab01_sample.log', artifacts / 'lab01_sample.log')
    executable = work / 'analyzer.exe'
    subprocess.run([compiler, '-std=c11', '-Wall', '-Wextra', '-Werror', str(source / 'lab01_log_analyzer.c'), '-o', str(executable)], check=True)
    subprocess.run([str(executable)], cwd=work, check=True)
    with (artifacts / 'lab01_report.csv').open(newline='') as handle:
        results = {row['metric']: row['value'] for row in csv.DictReader(handle)}
    expected = {'total_events': '10', 'login_fail': '6', 'suspicious_ip_hits': '5', 'failed_login_threshold_exceeded': 'true'}
    if any(results.get(key) != value for key, value in expected.items()):
        raise SystemExit(f'Unexpected fixture output: {results}')
    print('C fixture checks passed')
