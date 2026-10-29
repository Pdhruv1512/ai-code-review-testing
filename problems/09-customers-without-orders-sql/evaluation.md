# Evaluation: Problem 09 – Customers Without Orders (SQL)

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
| Edge cases | 5 | Correct when orders contain NULL `customer_id`, orders for unknown customers, no orders, all customers ordered |
| Efficiency | 5 | `NOT EXISTS` can stop at the first matching order per customer |
| Instruction following | 5 | Columns `id, name`, sorted by `id`, duplicate names returned as separate customers |
| Code quality | 5 | Clear aliases, `SELECT 1` in the subquery, explicit `ASC` |
| Explanation accuracy | N/A | The AI gave the query without any explanation |

## Test results

**8/8 tests passed**

Environment: Python 3.10.12, SQLite 3.37.2, Linux x86_64

| Test | Category | Result | Time (s) | Details |
|---|---|---|---|---|
| basic | basic | PASS | 0.00 |  |
| customer with many orders | edge | PASS | 0.00 |  |
| guest orders with NULL customer_id | spec | PASS | 0.00 |  |
| no orders at all | edge | PASS | 0.00 |  |
| everyone has ordered | edge | PASS | 0.00 |  |
| two customers with same name | spec | PASS | 0.00 |  |
| order for deleted customer id | edge | PASS | 0.00 |  |
| sorted by id, not name | spec | PASS | 0.00 |  |

## Issues found

None. The key check:

- **NULL trap:** the prompt says `customer_id` may be NULL. The common alternative,
  `WHERE id NOT IN (SELECT customer_id FROM orders)`, returns **zero rows** as soon as one order has a NULL
  `customer_id`, because `id <> NULL` is UNKNOWN, never TRUE. The AI used `NOT EXISTS`, which is not affected.
  The "guest orders with NULL customer_id" test confirms it.

## AI's claims vs reality

- No explanation was given. It would have helped to say *why* `NOT EXISTS` was chosen over `NOT IN`,
  since that choice is what makes the query correct.

## Fix verified

- [x] No fix needed.

## Summary

Correct, and it avoids the classic `NOT IN` + NULL bug that silently returns an empty result. The only
weakness is that it gives no explanation for that important choice.
