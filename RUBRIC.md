# Evaluation Rubric

Every AI response is scored 1–5 on six dimensions. Each score must be backed by evidence:
a test result, a line of code, or a quote from the AI's explanation.

| Dimension | 5 | 3 | 1 |
|---|---|---|---|
| **Correctness** | Passes every test | Passes basic tests, fails some spec/edge tests | Fails basic tests, does not compile, or crashes |
| **Edge cases** | Handles empty input, limits, duplicates, NULLs, and invalid input as specified | Handles some edge cases; misses one category (e.g. NULLs or overflow) | Ignores edge cases entirely |
| **Efficiency** | Meets the time limit with the expected complexity | Correct but slower than needed; passes small tests, fails the speed test | Far too slow (e.g. O(n²) where O(n) is required) or times out on most tests |
| **Instruction following** | Follows every rule in the prompt (input/output format, tie-break rules, language, column names) | Misses one stated rule | Ignores several rules or answers a different problem |
| **Code quality** | Readable, sensible names, safe types (no overflow), no dead code | Works but hard to read or has risky patterns | Messy, unsafe, or misleading code |
| **Explanation accuracy** | The AI's explanation matches what the code really does, including its complexity claim | Explanation is mostly right but overstates something (e.g. claims edge cases are handled when they are not) | Explanation is wrong or misleading |

Scores of 2 and 4 sit between the descriptions above. If the AI gives code with no explanation,
Explanation accuracy is marked **N/A**, and the missing explanation is noted in the write-up.

## Overall verdict

| Verdict | Meaning |
|---|---|
| **Accept** | Correct and complete. Could be used as is. |
| **Minor fix** | One small, clearly local bug (e.g. `<` instead of `<=`). |
| **Major fix** | Wrong approach for part of the problem, or several bugs. |
| **Reject** | Does not solve the problem or cannot be trusted. |

## Rules I follow

1. Run the tests before scoring. Never score from reading the code alone.
2. Every failed test gets a **root cause** (the exact line or idea that is wrong), not just "it failed".
3. Check the AI's own claims. If it says "handles all edge cases" or "runs in O(n)", verify it.
4. Suggest a concrete fix, then confirm the fix passes the tests.
5. Write so a reviewer can verify each point without re-running everything.
