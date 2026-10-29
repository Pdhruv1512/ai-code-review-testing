# Evaluation: Problem 08 – Second Highest Salary (SQL)

| Field | Value |
|---|---|
| AI model | ChatGPT (chatgpt.com, logged out, default model) |
| Date | 2026-10-29 |
| Language | SQL (SQLite) |
| Tests passed | 9 / 9 on SQLite 3.53.1 · 8 / 9 on SQLite 3.37.2 |
| Verdict | Accept, with a portability note |

## Scores

| Dimension | Score (1–5) | Evidence |
|---|---|---|
| Correctness | 4 | Correct SQL; returns a wrong value on SQLite 3.37.2 because of a database engine bug (below) |
| Edge cases | 5 | Ignores NULL salaries, handles ties at the top, empty table, and always returns exactly one row |
| Efficiency | 5 | One scan with DISTINCT and a sort; fine for this task |
| Instruction following | 5 | Single column `second_salary`, one row, NULL when there is no second distinct salary |
| Code quality | 4 | Wrapping the query in `SELECT ( ... )` to force one row is a good technique; the construct it relies on is not reliable on older SQLite |
| Explanation accuracy | N/A | The AI gave the query without any explanation |

## Test results

**Run 1: SQLite 3.37.2** (Python 3.10 on Linux)

**8/9 tests passed**

Environment: Python 3.10.12, SQLite 3.37.2, Linux x86_64

| Test | Category | Result | Time (s) | Details |
|---|---|---|---|---|
| basic | basic | PASS | 0.00 |  |
| tie at the top | spec | PASS | 0.00 |  |
| tie at second place | edge | PASS | 0.00 |  |
| only one distinct salary | spec | FAIL | 0.00 | row 1: expected (None,) got (500,) |
| single employee | edge | PASS | 0.00 |  |
| empty table | edge | PASS | 0.00 |  |
| NULL salaries ignored | edge | PASS | 0.00 |  |
| all salaries NULL | edge | PASS | 0.00 |  |
| negative and zero | edge | PASS | 0.00 |  |

**Run 2: SQLite 3.53.1** (Python 3.13 on Linux): **9 / 9 passed.**

## Issues found

1. **Test:** only one distinct salary (SQLite 3.37.2 only)
   **What happened:** three employees all earning 500. Expected NULL, got 500.
   **Root cause:** not the AI's logic. The query is correct by SQL rules: `SELECT DISTINCT` leaves one row
   (500), and `OFFSET 1` skips it, so the subquery is empty and the outer `SELECT` returns NULL.
   SQLite 3.37.2 has a known bug where `DISTINCT` with `ORDER BY ... LIMIT ... OFFSET` inside a scalar
   subquery returns a row it should have skipped
   ([SQLite forum report](https://sqlite.org/forum/forumpost/a5148faa49), fixed in a later check-in).
   I confirmed it directly:

   | Query on SQLite 3.37.2 (three rows of 500) | Result |
   |---|---|
   | `SELECT DISTINCT salary ... LIMIT 1 OFFSET 1` (on its own) | no rows (correct) |
   | Same query inside `SELECT ( ... )` | `500` (wrong) |
   | Same query using `GROUP BY salary` instead of `DISTINCT` | NULL (correct) |

   **Fix (portable):** either version below passes 9 / 9 on both SQLite versions.

   ```sql
   SELECT (SELECT salary FROM employees WHERE salary IS NOT NULL
           GROUP BY salary ORDER BY salary DESC LIMIT 1 OFFSET 1) AS second_salary;

   SELECT MAX(salary) AS second_salary
   FROM employees
   WHERE salary < (SELECT MAX(salary) FROM employees);
   ```

## AI's claims vs reality

- No explanation was given, so there are no claims to check. For a reviewer, the missing explanation is a
  small weakness: it does not say why the outer `SELECT ( ... )` is needed (to return NULL instead of zero rows).

## Fix verified

- [x] Both portable versions re-run: 9 / 9 on SQLite 3.37.2 and 9 / 9 on SQLite 3.53.1.

## Summary

The query is correct and handles every edge case in the prompt, including returning exactly one row.
It fails on SQLite 3.37.2 only because of a documented engine bug. This shows why test results should
record the environment: a "failed test" is not always the code's fault.
