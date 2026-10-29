#!/usr/bin/env python3
"""
Test runner for AI-generated solutions.

Usage:
    python3 run.py 01        # test one problem
    python3 run.py all       # test every problem that has a solution pasted in
    python3 run.py A1        # test an adversarial problem

For each problem it finds the solution file (solution.cpp, solution.py or
query.sql), runs every test case in tests.py, prints a summary, and writes
results.md inside the problem folder so you can paste it into your evaluation.
"""
import importlib.util
import os
import platform
import sqlite3
import subprocess
import sys
import tempfile
import time

sys.dont_write_bytecode = True  # don't leave __pycache__ folders in the problem directories

ROOT = os.path.dirname(os.path.abspath(__file__))
PROBLEMS = os.path.join(ROOT, "problems")
ADVERSARIAL = os.path.join(ROOT, "adversarial")
PLACEHOLDER = "PASTE AI CODE HERE"


def load_tests(folder):
    spec = importlib.util.spec_from_file_location("tests", os.path.join(folder, "tests.py"))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def short(text, limit=60, keep_spaces=False):
    text = str(text) if keep_spaces else " ".join(str(text).split())
    return text if len(text) <= limit else text[: limit - 3] + "..."


def run_program(cmd, stdin_text, time_limit):
    start = time.time()
    try:
        # errors="replace": a program that prints broken UTF-8 fails the test instead of crashing the runner
        p = subprocess.run(cmd, input=stdin_text, capture_output=True, text=True, encoding="utf-8",
                           errors="replace", timeout=time_limit)
    except subprocess.TimeoutExpired:
        return None, "TIMEOUT", time.time() - start
    if p.returncode != 0:
        return None, f"CRASH (exit {p.returncode}): {last_line(p.stderr)}", time.time() - start
    return p.stdout, None, time.time() - start


def last_line(text):
    lines = [l for l in text.strip().splitlines() if l.strip()]
    return short(lines[-1], 120) if lines else ""


def diff_detail(expected, got):
    """Point to the first line that differs, showing spaces exactly (repr)."""
    e_lines, g_lines = norm(expected).split("\n"), norm(got).split("\n")
    for i in range(max(len(e_lines), len(g_lines))):
        e = e_lines[i] if i < len(e_lines) else "<missing line>"
        g = g_lines[i] if i < len(g_lines) else "<missing line>"
        if e != g:
            where = f"line {i + 1}: " if max(len(e_lines), len(g_lines)) > 1 else ""
            e_tok, g_tok = e.split(" "), g.split(" ")
            if max(len(e_tok), len(g_tok)) > 5 and len(e_tok) == len(g_tok):
                j = next(j for j in range(len(e_tok)) if e_tok[j] != g_tok[j])
                return f"{where}value #{j + 1}: expected {e_tok[j]!r} got {g_tok[j]!r}"
            return f"{where}expected {short(repr(e), keep_spaces=True)} got {short(repr(g), keep_spaces=True)}"
    return "output differs"


def norm(text):
    lines = [line.rstrip() for line in text.strip().splitlines()]
    return "\n".join(lines)


def test_program(folder, tests, lang):
    time_limit = getattr(tests, "TIME_LIMIT", 2.0)
    with tempfile.TemporaryDirectory() as tmp:
        if lang == "cpp":
            exe = os.path.join(tmp, "sol")
            base_cmd = ["g++", "-O2", "-std=c++17", "-o", exe, os.path.join(folder, "solution.cpp")]
            c = subprocess.run(base_cmd, capture_output=True, text=True)
            if c.returncode != 0 and "bits/stdc++.h" in c.stderr:
                # <bits/stdc++.h> is GCC-only. Retry with the compatibility header so the logic can
                # still be tested, and record the portability problem in the report.
                c = subprocess.run(base_cmd + ["-I", os.path.join(ROOT, "compat")], capture_output=True, text=True)
                NOTES.append("Does not compile with this compiler as written: `<bits/stdc++.h>` is GCC-only. "
                             "Tested using the compatibility header in `compat/`.")
            if c.returncode != 0:
                return [("compile", "build", False, "COMPILE ERROR: " + short(c.stderr, 200), 0)]
            cmd = [exe]
        else:
            cmd = [sys.executable, os.path.join(folder, "solution.py")]
        results = []
        for case in tests.CASES:
            out, err, secs = run_program(cmd, case["input"], time_limit)
            if err:
                results.append((case["name"], case["category"], False, err, secs))
            elif norm(out) == norm(case["expected"]):
                results.append((case["name"], case["category"], True, "", secs))
            else:
                results.append((case["name"], case["category"], False,
                                diff_detail(case["expected"], out), secs))
        return results


def sql_diff(expected, rows):
    if len(expected) != len(rows):
        return f"expected {len(expected)} rows {short(expected)} got {len(rows)} rows {short(rows)}"
    for i, (e, g) in enumerate(zip(expected, rows)):
        if e != g:
            return f"row {i + 1}: expected {e} got {g}"
    return "output differs"


def test_sql(folder, tests):
    query = open(os.path.join(folder, "query.sql")).read()
    results = []
    for case in tests.CASES:
        db = sqlite3.connect(":memory:")
        db.executescript(tests.SCHEMA)
        db.executescript(case["setup"])
        start = time.time()
        try:
            rows = [tuple(r) for r in db.execute(query).fetchall()]
        except Exception as e:  # noqa: BLE001
            results.append((case["name"], case["category"], False, f"SQL ERROR: {short(e, 120)}", 0))
            continue
        secs = time.time() - start
        expected = [tuple(r) for r in case["expected"]]
        if rows == expected:
            results.append((case["name"], case["category"], True, "", secs))
        else:
            results.append((case["name"], case["category"], False,
                            sql_diff(expected, rows), secs))
    return results


def environment(lang):
    parts = [f"Python {platform.python_version()}"]
    if lang == "sql":
        parts.append(f"SQLite {sqlite3.sqlite_version}")
    if lang == "cpp":
        try:
            v = subprocess.run(["g++", "--version"], capture_output=True, text=True).stdout.splitlines()[0]
            parts.append(v)
        except (OSError, IndexError):
            parts.append("g++ unknown")
    parts.append(f"{platform.system()} {platform.machine()}")
    return ", ".join(parts)


NOTES = []  # portability notes collected while testing one problem


def run_problem(pid):
    NOTES.clear()
    base = ADVERSARIAL if pid.upper().startswith("A") else PROBLEMS
    pid = pid.upper() if base == ADVERSARIAL else pid
    matches = [d for d in sorted(os.listdir(base))
               if d.startswith(pid) and os.path.isdir(os.path.join(base, d))]
    if not matches:
        print(f"No problem folder starting with {pid}")
        return None
    folder = os.path.join(base, matches[0])
    tests = load_tests(folder)
    for fname, lang in (("solution.cpp", "cpp"), ("solution.py", "py"), ("query.sql", "sql")):
        path = os.path.join(folder, fname)
        if os.path.exists(path):
            break
    else:
        print(f"{matches[0]}: no solution file found")
        return None
    if PLACEHOLDER in open(path).read():
        print(f"{matches[0]}: skipped (paste the AI's code into {fname} first)")
        return None

    results = test_sql(folder, tests) if lang == "sql" else test_program(folder, tests, lang)
    passed = sum(1 for r in results if r[2])
    total = len(results)

    lines = [f"## Test results: {matches[0]}", "",
             f"**{passed}/{total} tests passed**", "",
             f"Environment: {environment(lang)}", "",
             *[line for n in NOTES for line in (f"Note: {n}", "")],
             "| Test | Category | Result | Time (s) | Details |",
             "|---|---|---|---|---|"]
    for name, cat, ok, detail, secs in results:
        lines.append(f"| {name} | {cat} | {'PASS' if ok else 'FAIL'} | {secs:.2f} | {detail.replace('|', '/')} |")
    report = "\n".join(lines) + "\n"
    with open(os.path.join(folder, "results.md"), "w") as f:
        f.write(report)

    print(f"\n{matches[0]}: {passed}/{total} passed")
    for n in NOTES:
        print(f"  NOTE  {n}")
    for name, cat, ok, detail, _ in results:
        if not ok:
            print(f"  FAIL  {name} [{cat}]  {detail}")
    print(f"  -> saved {os.path.relpath(os.path.join(folder, 'results.md'), ROOT)}")
    return passed, total


def main():
    if len(sys.argv) != 2:
        print(__doc__)
        sys.exit(1)
    arg = sys.argv[1]
    if arg == "all":
        ids = [d[:2] for d in sorted(os.listdir(PROBLEMS))]
        ids += [d[:2] for d in sorted(os.listdir(ADVERSARIAL)) if os.path.isdir(os.path.join(ADVERSARIAL, d))]
    elif arg.upper().startswith("A"):
        ids = [arg.upper()]
    else:
        ids = [arg.zfill(2)]
    for pid in ids:
        run_problem(pid)


if __name__ == "__main__":
    main()
