## Test results: 04-reverse-words-cpp

**9/10 tests passed**

Environment: Python 3.9.6, Apple clang version 17.0.0 (clang-1700.0.13.5), Darwin x86_64

| Test | Category | Result | Time (s) | Details |
|---|---|---|---|---|
| basic | basic | PASS | 0.27 |  |
| single word | edge | PASS | 0.01 |  |
| leading and trailing spaces | edge | PASS | 0.01 |  |
| multiple spaces between words | edge | PASS | 0.01 |  |
| empty line | edge | PASS | 0.00 |  |
| only spaces | edge | PASS | 0.01 |  |
| punctuation stays attached | spec | PASS | 0.01 |  |
| numbers and symbols | edge | PASS | 0.01 |  |
| tab is part of a word, not a separator | review | FAIL | 0.01 | expected 'c a\tb' got 'c b a' |
| long line (speed) | performance | PASS | 0.13 |  |
