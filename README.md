# AI Code Review & Testing

Evaluating AI-generated code in **C++, Python, and SQL** with automated edge-case tests and a written
rubric. Each AI answer is run against 8–12 tests (basic, edge, spec, and performance), scored on six
dimensions, and written up with root causes and verified fixes. A second set of **adversarial prompts**
was written specifically to make the model fail.

**Model tested:** ChatGPT (chatgpt.com, logged out, default model), October 2026.

## Key findings

- **7 of 10** standard problems were fully correct (one of them, 08, failed a test only because of a
  bug in old SQLite). **3** had a real defect:
  - **01 Two Sum:** ignored the prompt's tie-break rule (smallest i) and returned the smallest j, then
    claimed in its explanation that the rule was satisfied. The most serious finding: wrong *and* confidently explained.
  - **04 Reverse Words:** split on all whitespace, so a tab inside a word became a separator.
  - **05 Moving Average:** floating-point sums printed an exact zero as `-0.00`.
- **08 Second Highest Salary:** correct SQL, but wrong on SQLite 3.37.2 because of a
  [documented SQLite bug](https://sqlite.org/forum/forumpost/a5148faa49); 9 / 9 on SQLite 3.53.1.
  A reminder that a failing test is not always the code's fault.
- **1 of 7** adversarial prompts broke the model (**A5**, median salary): it counted only non-NULL
  salaries but ranked every row, and SQLite sorts NULLs first, so the "middle" row was a NULL.
- The model reliably avoided **single, famous traps** (NOT IN with NULLs, default window frame, banker's
  rounding, negative modulo, byte-wise UTF-8 reverse). It failed where **two requirements interacted**
  or where the prompt **changed a textbook rule** (Two Sum tie-break).
- **3 of 7** C++ answers (01, 02, A1) used `#include <bits/stdc++.h>`, which exists only in GCC: they
  **do not compile on macOS** (Apple clang) as written. `run.py` detects this, tests the logic with a
  compatibility header in `compat/`, and records the problem in `results.md`.
- **5 of 17** SQL/code answers came with no explanation at all (08, 09, A4, A5, A7), which makes review harder.

## Results: standard problems

| # | Problem | Language | Tests passed | Verdict | Main issue found |
|---|---|---|---|---|---|
| 01 | [Two Sum](problems/01-two-sum-cpp/evaluation.md) | C++ | 10 / 11 | Minor fix | Returns smallest j instead of smallest i; explanation claims otherwise; GCC-only header |
| 02 | [Merge Intervals](problems/02-merge-intervals-cpp/evaluation.md) | C++ | 12 / 12 | Accept | GCC-only header; does not compile on macOS clang |
| 03 | [First Occurrence](problems/03-first-occurrence-cpp/evaluation.md) | C++ | 11 / 11 | Accept | None |
| 04 | [Reverse Words](problems/04-reverse-words-cpp/evaluation.md) | C++ | 9 / 10 | Minor fix | Tab treated as a word separator |
| 05 | [Moving Average](problems/05-moving-average-py/evaluation.md) | Python | 11 / 12 | Minor fix | Prints `-0.00`; float drift at extreme values |
| 06 | [Roman to Integer](problems/06-roman-to-int-py/evaluation.md) | Python | 12 / 12 | Accept | Dead code (range check the regex makes unreachable) |
| 07 | [Case-Insensitive Dedupe](problems/07-dedupe-case-insensitive-py/evaluation.md) | Python | 10 / 10 | Accept | None |
| 08 | [Second Highest Salary](problems/08-second-highest-salary-sql/evaluation.md) | SQL | 9 / 9 (8 / 9 on SQLite 3.37) | Accept | Engine bug in old SQLite; portable rewrite provided |
| 09 | [Customers Without Orders](problems/09-customers-without-orders-sql/evaluation.md) | SQL | 8 / 8 | Accept | None (avoided the NOT IN + NULL trap) |
| 10 | [Running Total](problems/10-running-total-sql/evaluation.md) | SQL | 8 / 8 | Accept | None (avoided the default window-frame trap) |

## Results: adversarial prompts

| # | Prompt | Trap | Tests passed | Failed? |
|---|---|---|---|---|
| A1 | Pairs divisible by k (C++) | Negative `%`, count overflow | 8 / 8 | No |
| A2 | Exact big sum (C++) | Sum above `long long` | 7 / 7 | No |
| A3 | Round half away from zero (Python) | Banker's rounding, float precision | 9 / 9 | No |
| A4 | Latest order per customer (SQL) | Duplicate rows on date ties | 7 / 7 | No |
| A5 | Median per department (SQL) | NULLs + ranking + even counts | 7 / 8 | **Yes** |
| A6 | Reverse UTF-8 text (C++) | Byte-wise reverse | 8 / 8 | No |
| A7 | Longest login streak (SQL) | Gaps-and-islands with duplicate days | 8 / 8 | No |

Full write-up: [adversarial/README.md](adversarial/README.md).

## How it works

1. Each problem folder has a `prompt.md` with an exact prompt, including edge-case rules and a time limit.
2. The prompt is given to the AI in a new chat. Its code is saved **unchanged** in `solution.cpp`,
   `solution.py` or `query.sql`, and its explanation in `ai_response.md`.
3. `run.py` compiles/runs the code against every test in `tests.py` and writes `results.md`,
   including the Python / SQLite / compiler versions used.
4. The answer is scored with the [rubric](RUBRIC.md) in `evaluation.md`: every score has evidence, every
   failure has a root cause, and every fix is re-tested.

Test categories:

- **basic** – the normal case from the problem statement
- **edge** – empty input, limits, duplicates, negatives, NULLs, overflow
- **spec** – rules stated in the prompt that differ from the "textbook" version of the problem
- **performance** – large input that a slow algorithm cannot finish within the time limit
- **review** – tests added *after* reading the AI's code, for a problem found during review
- **trap** – (adversarial prompts) the specific mistake the prompt was designed to provoke

Every test file was checked in both directions before use: correct solutions pass every test, and
typical buggy solutions (e.g. `NOT IN` with NULLs, `int` overflow, `lower()` instead of `casefold()`)
are caught.

## Run it

Requirements: Python 3.8+ and a C++17 compiler (`g++`/`clang++`; on macOS run `xcode-select --install`).
SQLite is built into Python.

```bash
python3 run.py 01     # one standard problem
python3 run.py A5     # one adversarial prompt
python3 run.py all    # everything
```

Note: SQL results can depend on the SQLite version (see problem 08). `results.md` records the version used.

## Structure

```
run.py                     test runner
compat/bits/stdc++.h       stand-in for GCC's <bits/stdc++.h> on other compilers (used only as a fallback)
RUBRIC.md                  scoring rubric (6 dimensions, 1–5)
EVALUATION_TEMPLATE.md     template for each write-up
problems/NN-name/
    prompt.md              exact prompt given to the AI
    solution.* / query.sql AI's code, unchanged
    ai_response.md         AI's explanation, as written
    tests.py               test cases (with a reference checker)
    results.md             generated test report
    evaluation.md          scored evaluation
adversarial/AN-name/       same layout, for prompts designed to make the AI fail
```

## Skills demonstrated

Code review · test design · edge-case analysis · root-cause debugging · algorithm complexity ·
floating-point and Unicode pitfalls · SQL NULL semantics and window functions ·
rubric-based evaluation · adversarial prompt design · written technical feedback
