# Evaluation: Problem 06 – Roman Numeral to Integer (Python)

| Field | Value |
|---|---|
| AI model | ChatGPT (chatgpt.com, logged out, default model) |
| Date | 2026-10-29 |
| Language | Python 3 |
| Tests passed | 12 / 12 |
| Verdict | Accept |

## Scores

| Dimension | Score (1–5) | Evidence |
|---|---|---|
| Correctness | 5 | Passes all 12 tests, including all 3,999 valid numerals |
| Edge cases | 5 | Rejects `IIII`, `VV`, `IL`, `IM`, `VIV`, `MMMM`, lowercase, and non-Roman letters without crashing |
| Efficiency | 5 | Regex + one pass per line; all 3,999 numerals in 0.06 s |
| Instruction following | 5 | Uppercase only, 1–3999, standard form, `INVALID` otherwise |
| Code quality | 4 | Validates before converting (no `KeyError` on bad letters); two redundant pieces, below |
| Explanation accuracy | 5 | Accurately describes the regex validation and the add/subtract rule |

## Test results

**12/12 tests passed**

Environment: Python 3.10.12, Linux x86_64

| Test | Category | Result | Time (s) | Details |
|---|---|---|---|---|
| basic | basic | PASS | 0.03 |  |
| all subtractive pairs | basic | PASS | 0.03 |  |
| largest value | edge | PASS | 0.03 |  |
| smallest value | edge | PASS | 0.03 |  |
| four in a row is invalid | spec | PASS | 0.03 |  |
| repeated V/L/D is invalid | spec | PASS | 0.03 |  |
| bad subtraction is invalid | spec | PASS | 0.03 |  |
| 4000 and above is invalid | spec | PASS | 0.03 |  |
| lowercase is invalid | spec | PASS | 0.03 |  |
| non-roman letters invalid | edge | PASS | 0.03 |  |
| wrong order is invalid | spec | PASS | 0.03 |  |
| every valid numeral 1-3999 | performance | PASS | 0.06 |  |

## Issues found

No failures. Two code-quality notes:

1. **Dead code:** `return str(total) if 1 <= total <= 3999 else "INVALID"`. The regex already limits
   input to standard numerals. I enumerated every string the regex accepts: there are exactly 3,999,
   with values from 1 to 3,999, all distinct. So the range check can never be false.
2. **Redundant anchors:** `re.fullmatch` already requires the whole string to match, so `^` and `$`
   in the pattern do nothing. Harmless, but it shows the code was assembled from two habits.

Also noted: `line.strip()` means ` IV ` (with spaces) is accepted as 4. The prompt does not say
whether surrounding spaces are allowed, so this is acceptable.

## AI's claims vs reality

- The AI said: "A regular expression checks that the string follows standard Roman numeral rules." **True.**
- The AI said: "supports all valid standard Roman numerals from I (1) through MMMCMXCIX (3999)." **True** (all 3,999 pass).

## Fix verified

- [x] No fix needed.

## Summary

Correct and robust. The key decision, validating with a strict regex before converting, avoids the most
common failure on this problem: accepting `IIII` or `IC` and returning a number. Minor redundancy only.
