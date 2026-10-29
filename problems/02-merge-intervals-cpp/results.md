## Test results: 02-merge-intervals-cpp

**12/12 tests passed**

Environment: Python 3.9.6, Apple clang version 17.0.0 (clang-1700.0.13.5), Darwin x86_64

Note: Does not compile with this compiler as written: `<bits/stdc++.h>` is GCC-only. Tested using the compatibility header in `compat/`.

| Test | Category | Result | Time (s) | Details |
|---|---|---|---|---|
| basic overlap | basic | PASS | 0.26 |  |
| unsorted input | edge | PASS | 0.01 |  |
| touching intervals merge | spec | PASS | 0.01 |  |
| adjacent intervals stay separate | spec | PASS | 0.00 |  |
| one interval inside another | edge | PASS | 0.00 |  |
| inner interval comes first | edge | PASS | 0.00 |  |
| duplicates | edge | PASS | 0.01 |  |
| negative values | edge | PASS | 0.01 |  |
| empty input | edge | PASS | 0.01 |  |
| single point interval | edge | PASS | 0.01 |  |
| values near int limits | edge | PASS | 0.01 |  |
| 200k intervals (speed) | performance | PASS | 1.32 |  |
