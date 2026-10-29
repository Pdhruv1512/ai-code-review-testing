# Evaluation: Problem 07 – Remove Duplicates, Case-Insensitive (Python)

| Field | Value |
|---|---|
| AI model | ChatGPT (chatgpt.com, logged out, default model) |
| Date | 2026-10-29 |
| Language | Python 3 |
| Tests passed | 10 / 10 |
| Verdict | Accept |

## Scores

| Dimension | Score (1–5) | Evidence |
|---|---|---|
| Correctness | 5 | Passes all 10 tests |
| Edge cases | 5 | `Straße` = `STRASSE`, accented letters, blank and space-only lines, empty input |
| Efficiency | 5 | Set lookups, O(total characters); 200k lines in 0.15 s |
| Instruction following | 5 | Keeps the first spelling, prints the stripped version, skips blanks, preserves order |
| Code quality | 5 | Short and clear; streams input line by line instead of reading it all at once |
| Explanation accuracy | 5 | Correctly explains why `casefold()` is needed instead of `lower()` |

## Test results

**10/10 tests passed**

Environment: Python 3.10.12, Linux x86_64

| Test | Category | Result | Time (s) | Details |
|---|---|---|---|---|
| basic | basic | PASS | 0.02 |  |
| different case | spec | PASS | 0.02 |  |
| keeps FIRST spelling | spec | PASS | 0.02 |  |
| surrounding spaces ignored | spec | PASS | 0.02 |  |
| blank lines ignored | edge | PASS | 0.02 |  |
| order preserved | spec | PASS | 0.03 |  |
| German sharp s | spec | PASS | 0.02 |  |
| accented letters | edge | PASS | 0.03 |  |
| empty input | edge | PASS | 0.02 |  |
| 200k lines (speed) | performance | PASS | 0.15 |  |

## Issues found

None. Points I checked specifically:

- **Unicode:** `"Straße".lower()` is `"straße"` but `"Straße".casefold()` is `"strasse"`. The code uses
  `casefold()`, so `STRASSE` is correctly treated as a duplicate. A `lower()` version fails this test.
- **Speed:** a `set` gives O(1) lookups. A `list` (`if key not in seen_list`) would be O(n²) and time out
  on the 200k-line test.

## AI's claims vs reality

- The AI said: "'Straße'.casefold() and 'STRASSE'.casefold() both produce 'strasse'." **True.**
- The AI said: "O(n) expected time overall, where n is the total number of input characters." **True.**

## Fix verified

- [x] No fix needed.

## Summary

Correct, fast, and well explained. It avoided both traps in this prompt: `lower()` instead of
`casefold()`, and a list instead of a set. A model answer.
