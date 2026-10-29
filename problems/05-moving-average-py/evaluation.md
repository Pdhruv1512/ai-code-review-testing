# Evaluation: Problem 05 – Moving Average (Python)

| Field | Value |
|---|---|
| AI model | ChatGPT (chatgpt.com, logged out, default model) |
| Date | 2026-10-29 |
| Language | Python 3 |
| Tests passed | 11 / 12 |
| Verdict | Minor fix |

## Scores

| Dimension | Score (1–5) | Evidence |
|---|---|---|
| Correctness | 4 | All averages are numerically right; an average of exactly zero prints as `-0.00` |
| Edge cases | 4 | Handles k = 0, negative k, empty line, k larger than the list, decimals, negatives; misses negative zero |
| Efficiency | 5 | Sliding window, O(n); 200k numbers with k = 999 ran in 0.24 s |
| Instruction following | 4 | Prints INVALID / empty line / 2-decimal values as specified; `-0.00` is not a sensible 2-decimal value |
| Code quality | 4 | Clear structure and early returns; floating-point running sum is fine for normal values but loses precision at extreme magnitudes (see below) |
| Explanation accuracy | 5 | Every claim (validation order, sliding window, O(n), formatting) is accurate |

## Test results

**11/12 tests passed**

Environment: Python 3.10.12, Linux x86_64

| Test | Category | Result | Time (s) | Details |
|---|---|---|---|---|
| basic | basic | PASS | 0.03 |  |
| window of 1 | edge | PASS | 0.03 |  |
| window equals list length | edge | PASS | 0.03 |  |
| window larger than list | edge | PASS | 0.03 |  |
| empty list | edge | PASS | 0.03 |  |
| k = 0 is invalid | spec | PASS | 0.03 |  |
| negative k is invalid | spec | PASS | 0.03 |  |
| negative numbers | edge | PASS | 0.03 |  |
| decimal numbers | edge | PASS | 0.03 |  |
| rounding to 2 decimals | spec | PASS | 0.03 |  |
| average exactly zero prints 0.00 | review | FAIL | 0.03 | expected '0.00' got '-0.00' |
| 200k numbers, k=999 (speed) | performance | PASS | 0.24 |  |

Note: the "average exactly zero" test (category `review`) was added after reading the code, not before.

## Issues found

1. **Test:** average exactly zero prints 0.00
   **What happened:** input `k = 3`, `-0.1 -0.2 0.3`. Expected `0.00`, got `-0.00`.
   **Root cause:** `-0.1`, `-0.2` and `0.3` are not exact in binary floating point, so their sum is
   `-5.55e-17` instead of `0`. Formatting a tiny negative number with `:.2f` gives `-0.00`.
   **Fix:** normalize the formatted value:

   ```python
   def fmt(x):
       s = f"{x:.2f}"
       return "0.00" if s == "-0.00" else s
   ```

   (For exact results, `decimal.Decimal` could be used for the sums instead of `float`.)

2. **Not a test failure, found by experiment: precision loss at extreme values.**
   With `k = 2` and `10000000000000000 1 -10000000000000000 0.5 0.5`, the last window is
   `0.5 + 0.5 = 1.0 / 2 = 0.50`, but the program prints `0.00`. The running sum lost the `0.5` values
   when it was near 10¹⁶ (beyond float's 53-bit precision), and the error carries forward because
   the window sum is updated incrementally instead of recomputed.
   **Severity:** low. In a separate check with 20 random runs of 20,000 two-decimal numbers
   (about 400,000 windows), the output matched the exact average every time.

## AI's claims vs reality

- The AI said: "Sliding window: ... updates it in constant time." **True.**
- The AI said: "Time: O(n)." **True** (0.24 s for 200k numbers).
- The AI said: "Formats every average to exactly two decimal places." **True**, but it does not account for `-0.00`.

## Fix verified

- [x] Applied the `fmt` fix and re-ran the tests: 12 / 12 passed.

## Summary

Correct, fast, and well explained, with clean handling of every invalid-input rule in the prompt.
Floating-point sums make an exact zero print as `-0.00`, and the incremental running sum can drift at
extreme magnitudes. Both come from using `float` for money-like decimal data; the visible bug is a one-line fix.
