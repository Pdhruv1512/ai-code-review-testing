## Test results: 01-two-sum-cpp

**10/11 tests passed**

Environment: Python 3.9.6, Apple clang version 17.0.0 (clang-1700.0.13.5), Darwin x86_64

Note: Does not compile with this compiler as written: `<bits/stdc++.h>` is GCC-only. Tested using the compatibility header in `compat/`.

| Test | Category | Result | Time (s) | Details |
|---|---|---|---|---|
| basic example | basic | PASS | 0.32 |  |
| answer at the end | basic | PASS | 0.01 |  |
| no pair exists | edge | PASS | 0.01 |  |
| single element | edge | PASS | 0.01 |  |
| same value twice | edge | PASS | 0.01 |  |
| can't use one element twice | edge | PASS | 0.01 |  |
| negative numbers | edge | PASS | 0.01 |  |
| tie-break: smallest i first | spec | FAIL | 0.01 | expected '0 3' got '1 2' |
| many duplicates | spec | PASS | 0.01 |  |
| sum overflows 32-bit int | edge | PASS | 0.01 |  |
| large input, no pair (speed) | performance | PASS | 0.30 |  |
