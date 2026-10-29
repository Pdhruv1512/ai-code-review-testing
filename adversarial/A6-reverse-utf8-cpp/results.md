## Test results: A6-reverse-utf8-cpp

**8/8 tests passed**

Environment: Python 3.9.6, Apple clang version 17.0.0 (clang-1700.0.13.5), Darwin x86_64

| Test | Category | Result | Time (s) | Details |
|---|---|---|---|---|
| ASCII only | basic | PASS | 0.27 |  |
| accented letters (2 bytes) | trap | PASS | 0.01 |  |
| Japanese (3 bytes) | trap | PASS | 0.01 |  |
| emoji (4 bytes) | trap | PASS | 0.01 |  |
| mixed scripts | trap | PASS | 0.01 |  |
| single multi-byte character | edge | PASS | 0.01 |  |
| empty line | edge | PASS | 0.01 |  |
| long line (speed) | performance | PASS | 0.10 |  |
