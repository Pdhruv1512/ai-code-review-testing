# Adversarial Prompts

Seven prompts written to find where an AI coding assistant makes mistakes. Each one targets a specific,
well-known trap. Every prompt has its own folder with the exact prompt (`prompt.md`), the AI's unchanged
answer (`solution.*` / `query.sql`, `ai_response.md`), the tests (`tests.py`) and the test report (`results.md`).

Run them with `python3 run.py A1` … `python3 run.py A7` from the project root.

**Model tested:** ChatGPT (chatgpt.com, logged out, default model), 2026-10-29.

## Results

| # | Prompt | Trap | Tests | Did it fail? | What happened |
|---|---|---|---|---|---|
| A1 | [Pairs divisible by k](A1-divisible-pairs-cpp) (C++) | `%` of a negative number; pair count above 2³¹; k up to 10⁹ | 8 / 8 | No | Normalized remainders with `((x % k) + k) % k`, `long long` count, hash map instead of an array |
| A2 | [Exact big sum](A2-big-sum-cpp) (C++) | Sum above `long long` max (9.22 × 10¹⁸) | 7 / 7 | No | Used `__int128` and printed it digit by digit. Portability note below |
| A3 | [Round half away from zero](A3-round-half-away-py) (Python) | `round()` is banker's rounding; `int(x + 0.5)` breaks negatives; floats lose exact decimals | 9 / 9 | No | Used `Decimal` with `ROUND_HALF_UP`. Robustness note below |
| A4 | [Latest order per customer](A4-latest-order-sql) (SQL) | Joining on `MAX(date)` returns duplicates on ties | 7 / 7 | No | `ROW_NUMBER()` ordered by `order_date DESC, id DESC` |
| A5 | [Median per department](A5-median-salary-sql) (SQL) | No MEDIAN in SQLite; NULLs; even counts; all-NULL departments | 7 / 8 | **Yes** | Ranked NULL rows but counted only non-NULL rows, so the middle position lands on a NULL |
| A6 | [Reverse UTF-8 text](A6-reverse-utf8-cpp) (C++) | `std::reverse` on bytes breaks multi-byte characters | 8 / 8 | No | Split by UTF-8 lead byte, then reversed whole code points; also noted grapheme clusters |
| A7 | [Longest login streak](A7-login-streak-sql) (SQL) | Gaps-and-islands breaks when a user logs in twice on one day | 8 / 8 | No | Removed duplicate days with `SELECT DISTINCT` before `ROW_NUMBER()` |

**Summary:** 1 of 7 prompts produced a wrong answer (A5). ChatGPT handled the classic single-trap problems
well; it failed where two details interact (NULL handling *and* ranking order).

## Full entries

### A5: Median per department — failed

**Prompt:** see [A5-median-salary-sql/prompt.md](A5-median-salary-sql/prompt.md).

**AI response (short):** a CTE that ranks every row with `ROW_NUMBER() OVER (PARTITION BY dept ORDER BY salary)`,
counts salaries with `COUNT(salary)`, and averages the rows at positions `(cnt + 1) / 2` and `(cnt + 2) / 2`.
It joins back to all departments so all-NULL departments still appear.

**Failure:** department A = NULL, 100, NULL, 300, 200. Expected 200, got NULL.

| salary | rn (ROW_NUMBER) | cnt (COUNT(salary)) |
|---|---|---|
| NULL | 1 | 3 |
| NULL | 2 | 3 |
| 100 | 3 | 3 |
| 200 | 4 | 3 |
| 300 | 5 | 3 |

`COUNT(salary)` skips NULLs (cnt = 3), but `ROW_NUMBER()` numbers every row, and SQLite sorts NULLs
**first** in ascending order. The "middle" position `(3 + 1) / 2 = 2` is a NULL row, so `AVG` returns NULL.
Confirmed on SQLite 3.37.2 and 3.53.1.

**Fix:** filter NULLs before ranking. Verified 8 / 8:

```sql
    FROM employees
    WHERE salary IS NOT NULL   -- add this line inside the "ranked" CTE
```

The existing `LEFT JOIN` from all departments still returns all-NULL departments with a NULL median.

**Why the prompt worked:** each part of the query is a standard pattern, and each is correct on its own.
The bug only appears when they are combined: the count ignores NULLs and the ranking does not.
The prompt said "ignoring NULL salaries" but the AI only applied it to one of the two places that needed it.

### Notes on the passing answers

- **A2, portability:** `__int128` is a GCC/Clang extension, not standard C++ (`g++ -pedantic` warns:
  "ISO C++ does not support '__int128'"). The program will not compile with MSVC on Windows. The AI's
  explanation said this ("GCC/Clang's __int128 extension"), which is accurate. The code also uses
  `std::string` without `#include <string>`; it compiles because `<iostream>` happens to include it,
  but that is not guaranteed.
- **A3, robustness:** Python's `Decimal` uses 28 significant digits by default. A number with 29+ digits
  (e.g. `12345678901234567890123456789.5`) raises `decimal.InvalidOperation`. The prompt promised at most
  17 digits, so this is outside the spec, not a failure.
- **A6, scope:** the AI noted on its own that it reverses code points, not user-perceived characters
  (a letter plus a combining accent becomes two code points). That is exactly what the prompt asked for,
  and pointing out the limitation is good practice.
- **A1, A4, A7:** no issues found. A7's use of `SELECT DISTINCT` before `ROW_NUMBER()` is the exact step
  that the trap targets.

## What makes a good adversarial prompt (lessons from this round)

- Single, famous traps (negative modulo, banker's rounding, byte-wise reverse) were all avoided:
  the model has seen them many times.
- The failure came from **two rules interacting** (NULLs + ranking). Prompts that combine two
  individually-easy requirements are more likely to break the model than prompts built around one trap.
- Hidden-test style edge cases (NULLs, ties, duplicates) are more effective in SQL than in C++/Python here.
