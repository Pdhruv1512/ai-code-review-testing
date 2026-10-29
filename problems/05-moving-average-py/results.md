## Test results: 05-moving-average-py

**11/12 tests passed**

Environment: Python 3.9.6, Darwin x86_64

| Test | Category | Result | Time (s) | Details |
|---|---|---|---|---|
| basic | basic | PASS | 0.05 |  |
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
| 200k numbers, k=999 (speed) | performance | PASS | 0.20 |  |
