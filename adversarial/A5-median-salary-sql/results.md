## Test results: A5-median-salary-sql

**7/8 tests passed**

Environment: Python 3.9.6, SQLite 3.43.2, Darwin x86_64

| Test | Category | Result | Time (s) | Details |
|---|---|---|---|---|
| odd count | basic | PASS | 0.00 |  |
| even count averages two middle values | trap | PASS | 0.00 |  |
| NULLs are ignored | trap | FAIL | 0.00 | row 1: expected ('A', 200) got ('A', None) |
| department with only NULLs | trap | PASS | 0.00 |  |
| several departments | basic | PASS | 0.00 |  |
| duplicate salaries | edge | PASS | 0.00 |  |
| single employee | edge | PASS | 0.00 |  |
| unsorted insert order | edge | PASS | 0.00 |  |
