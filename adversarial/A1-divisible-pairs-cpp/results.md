## Test results: A1-divisible-pairs-cpp

**8/8 tests passed**

Environment: Python 3.9.6, Apple clang version 17.0.0 (clang-1700.0.13.5), Darwin x86_64

Note: Does not compile with this compiler as written: `<bits/stdc++.h>` is GCC-only. Tested using the compatibility header in `compat/`.

| Test | Category | Result | Time (s) | Details |
|---|---|---|---|---|
| basic | basic | PASS | 0.26 |  |
| negative numbers | trap | PASS | 0.01 |  |
| negative and zero remainder | trap | PASS | 0.01 |  |
| single element | edge | PASS | 0.01 |  |
| k = 1 (every pair) | edge | PASS | 0.01 |  |
| k larger than all values | trap | PASS | 0.01 |  |
| count overflows 32-bit int | trap | PASS | 0.22 |  |
| 200k random values (speed) | performance | PASS | 0.66 |  |
