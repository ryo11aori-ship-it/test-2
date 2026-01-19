#!/usr/bin/env python3
# sample/main.py
import sys
import io
from pathlib import Path

# Ensure stdout/stderr are UTF-8 wrapped (helps in packed exe on Windows)
try:
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8", errors="replace")
except Exception:
    pass

def ci_short_run():
    print("PY sample: CI short run")
    p = Path("sample_py_artifact.txt")
    p.write_text("py_ci_ok\n", encoding="utf-8")
    print("Wrote sample_py_artifact.txt")

def full_run():
    print("PY sample: full run (this is the non-CI behavior)")
    # Lightweight example workload
    s = sum(range(10000))
    print("sum(0..9999) =", s)
    p = Path("sample_py_artifact.txt")
    p.write_text("py_full_ok\n", encoding="utf-8")
    print("Wrote sample_py_artifact.txt")

def main():
    if "--ci-test" in sys.argv:
        ci_short_run()
        return 0
    # otherwise do a small normal run
    full_run()
    return 0

if __name__ == "__main__":
    sys.exit(main())
