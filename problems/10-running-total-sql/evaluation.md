# Evaluation: Problem 10 – Running Total per Customer (SQL)

| Field | Value |
|---|---|
| AI model | ChatGPT (chatgpt.com, logged out, default model) |
| Date | 2026-10-29 |
| Language | SQL (SQLite) |
| Tests passed | 8 / 8 |
| Verdict | Accept |

## Scores

| Dimension | Score (1–5) | Evidence |
|---|---|---|
| Correctness | 5 | Passes all 8 tests |
| Edge cases | 5 | Same-day orders, ties broken by id, refunds (negative amounts), empty table, year boundary |
| Efficiency | 5 | One window function pass per customer |
| Instruction following | 5 | Exact columns and sort order; same-day orders counted one by one in id order |
| Code quality | 5 | Readable layout; the window frame is written out explicitly |
| Explanation accuracy | 5 | Each line of the explanation matches what the clause does |

## Test results

**8/8 tests passed**

Environment: Python 3.10.12, SQLite 3.37.2, Linux x86_64

| Test | Category | Result | Time (s) | Details |
|---|---|---|---|---|
| basic, one customer | basic | PASS | 0.00 |  |
| two customers kept separate | basic | PASS | 0.00 |  |
| inserted out of date order | edge | PASS | 0.00 |  |
| same-day orders add one by one | spec | PASS | 0.00 |  |
| same-day tie broken by id | spec | PASS | 0.00 |  |
| negative amount (refund) | edge | PASS | 0.00 |  |
| empty table | edge | PASS | 0.00 |  |
| dates across a year boundary | edge | PASS | 0.00 |  |

## Issues found

None. The key check:

- **Window frame trap:** with only `ORDER BY order_date` and no frame, SQL uses the default frame
  `RANGE ... CURRENT ROW`, which gives every order on the same date the **same** total (the whole day's
  sum). The AI ordered by `order_date, id` and wrote `ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW`,
  so each order adds one at a time. I tested each change on its own: `ORDER BY order_date, id` alone also
  passes 8 / 8. `ROWS` with only `ORDER BY order_date` also passed, but only because SQLite happened to read
  same-day rows in id order; that order is not guaranteed. Using both makes the intent explicit and safe.

## AI's claims vs reality

- The AI said: "ORDER BY order_date, id ensures orders are processed chronologically, with ties broken by id." **True.**
- The AI said: "ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW sums every row from the customer's first
  order through the current order, including refunds." **True** (refund test passes).

## Fix verified

- [x] No fix needed.

## Summary

Correct and clearly explained. It avoided the default-frame trap that makes same-day orders share a running
total, which is the main way this query goes wrong.
