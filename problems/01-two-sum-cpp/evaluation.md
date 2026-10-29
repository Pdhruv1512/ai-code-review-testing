# Evaluation: Problem 01 – Two Sum (C++)

| Field | Value |
|---|---|
| AI model | ChatGPT (chatgpt.com, logged out, default model) |
| Date | 2026-10-29 |
| Language | C++17 |
| Tests passed | 10 / 11 |
| Verdict | Minor fix (code), explanation not trustworthy |

## Scores

| Dimension | Score (1–5) | Evidence |
|---|---|---|
| Correctness | 3 | Wrong answer whenever several pairs exist and the pair with the smallest j is not the pair with the smallest i (`2 1 3 2`, target 4 → `1 2`, expected `0 3`) |
| Edge cases | 5 | Handles no pair, n = 1, duplicates, negatives, and a sum above 32-bit range (`long long` for values and complement) |
| Efficiency | 5 | One pass with a hash map; 100k-element test ran in 0.04 s |
| Instruction following | 2 | Ignores the one rule that makes this prompt different from textbook Two Sum: "smallest i; if there is still a tie, the smallest j" |
| Code quality | 4 | Clean and readable, `reserve` avoids rehashing; the comment "Keep the earliest index" is true but does not deliver the required tie-break |
| Explanation accuracy | 2 | Claims the tie-break is satisfied (false). Says O(n log n) at the top and O(n) at the bottom (it is O(n) expected) |

## Test results

**10/11 tests passed**

Environment: Python 3.10.12, g++ (Ubuntu 11.4.0-1ubuntu1~22.04.3) 11.4.0, Linux x86_64

| Test | Category | Result | Time (s) | Details |
|---|---|---|---|---|
| basic example | basic | PASS | 0.00 |  |
| answer at the end | basic | PASS | 0.00 |  |
| no pair exists | edge | PASS | 0.00 |  |
| single element | edge | PASS | 0.00 |  |
| same value twice | edge | PASS | 0.00 |  |
| can't use one element twice | edge | PASS | 0.00 |  |
| negative numbers | edge | PASS | 0.00 |  |
| tie-break: smallest i first | spec | FAIL | 0.00 | expected '0 3' got '1 2' |
| many duplicates | spec | PASS | 0.00 |  |
| sum overflows 32-bit int | edge | PASS | 0.00 |  |
| large input, no pair (speed) | performance | PASS | 0.04 |  |

## Issues found

1. **Test:** tie-break: smallest i first
   **What happened:** input `4 4 / 2 1 3 2`. Expected `0 3`, got `1 2`.
   **Root cause:** the loop walks j from left to right and stops at the **first j** that has a matching
   earlier value. Trace: j = 1 (value 1) needs 3, not seen yet; j = 2 (value 3) needs 1, seen at index 1
   → prints `1 2` and returns. The pair (0, 3) has a smaller i but a larger j, so it is never reached.
   Storing the earliest index only picks the smallest i *for that j*, which is a different rule.
   **Fix:** scan i from right to left. Keep, for each value, the nearest index to the right (that is the
   smallest j > i). Every time a pair is found, record it; the last one recorded has the smallest i.

   ```cpp
   unordered_map<long long, int> nextIdx;
   nextIdx.reserve(2 * n + 1);
   int bi = -1, bj = -1;
   for (int i = n - 1; i >= 0; --i) {
       auto it = nextIdx.find(target - a[i]);
       if (it != nextIdx.end()) { bi = i; bj = it->second; }
       nextIdx[a[i]] = i;   // overwrite: keeps the smallest index to the right
   }
   cout << bi << ' ' << bj << '\n';
   ```

## AI's claims vs reality

- The AI said: "The first pair found has the smallest possible j. For that j, the map stores the smallest
  possible i, so the tie-breaking requirements are satisfied."
- Reality: **false.** The first half of the sentence is correct, and it shows the problem: the prompt asks
  for the smallest i first, not the smallest j. The failing test proves it.
- The AI said: "runs in O(n log n) time" and later "Expected time: O(n)".
- Reality: the two claims contradict each other. A single pass with hash lookups is O(n) expected.

## Fix verified

- [x] Applied the fix above and re-ran the tests: 11 / 11 passed, 100k test in 0.03 s.

## Summary

The code is fast, overflow-safe, and correct for inputs with a single valid pair. It solves textbook
Two Sum instead of the prompt's version: it returns the pair with the smallest j, and its explanation
confidently claims the opposite. The fix is small, but the explanation should not be trusted.
