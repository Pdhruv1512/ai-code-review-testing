# Evaluation: Problem 04 – Reverse Words (C++)

| Field | Value |
|---|---|
| AI model | ChatGPT (chatgpt.com, logged out, default model) |
| Date | 2026-10-29 |
| Language | C++17 |
| Tests passed | 9 / 10 |
| Verdict | Minor fix |

## Scores

| Dimension | Score (1–5) | Evidence |
|---|---|---|
| Correctness | 4 | Correct for every space-separated input; wrong when a word contains a tab |
| Edge cases | 4 | Handles empty line, only spaces, leading/trailing and repeated spaces; misses tab characters |
| Efficiency | 5 | O(n); a 1.49M-character line ran in 0.09 s |
| Instruction following | 4 | The prompt defines a word as "any run of non-space characters"; the code splits on all whitespace |
| Code quality | 4 | Simple and readable; the repeated `static_cast<int>(words.size()) - 1` could be a named variable |
| Explanation accuracy | 4 | Says `iss >> word` skips "consecutive spaces"; it actually skips all whitespace (tabs too), which is why the tab test fails |

## Test results

**9/10 tests passed**

Environment: Python 3.10.12, g++ (Ubuntu 11.4.0-1ubuntu1~22.04.3) 11.4.0, Linux x86_64

| Test | Category | Result | Time (s) | Details |
|---|---|---|---|---|
| basic | basic | PASS | 0.00 |  |
| single word | edge | PASS | 0.00 |  |
| leading and trailing spaces | edge | PASS | 0.00 |  |
| multiple spaces between words | edge | PASS | 0.00 |  |
| empty line | edge | PASS | 0.00 |  |
| only spaces | edge | PASS | 0.00 |  |
| punctuation stays attached | spec | PASS | 0.00 |  |
| numbers and symbols | edge | PASS | 0.00 |  |
| tab is part of a word, not a separator | review | FAIL | 0.00 | expected 'c a\tb' got 'c b a' |
| long line (speed) | performance | PASS | 0.09 |  |

Note: the "tab is part of a word" test (category `review`) was added after reading the code, not before.

## Issues found

1. **Test:** tab is part of a word, not a separator
   **What happened:** input `a<TAB>b c`. Expected `c a<TAB>b`, got `c b a`.
   **Root cause:** `operator>>` on a stream skips any whitespace (`' '`, `'\t'`, `'\n'`, `'\r'`, ...),
   so it treats the tab as a separator. The prompt only treats the space character as a separator.
   **Fix:** split on `' '` only:

   ```cpp
   vector<string> words;
   string cur;
   for (char ch : line) {
       if (ch == ' ') { if (!cur.empty()) words.push_back(cur); cur.clear(); }
       else cur += ch;
   }
   if (!cur.empty()) words.push_back(cur);
   ```

**Severity:** low. Real input rarely has tabs, but the code does not follow the prompt's definition of a word.

## AI's claims vs reality

- The AI said: "istringstream with iss >> word extracts words while automatically skipping consecutive spaces."
- Reality: partly true. It skips any whitespace, not only spaces. That difference is the bug.
- The AI said: "handles lines up to 2,000,000 characters long." **True** (`getline` into `std::string`; long-line test passed).

## Fix verified

- [x] Applied the fix above and re-ran the tests: 10 / 10 passed.

## Summary

A clean, idiomatic solution that handles every spacing case in the prompt. It splits on all whitespace
instead of spaces only, so a tab inside a word is treated as a separator. The fix is local and small.
