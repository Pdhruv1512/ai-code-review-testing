# A3: Round Half Away From Zero (Python)

**Trap being tested:** Python's `round()` uses banker's rounding (2.5 → 2), `int(x + 0.5)` is wrong for
negatives, and converting to `float` loses the exact decimal value.

```
Write a complete Python 3 program that reads from standard input and writes to standard output.

Input: one or more lines. Each line contains one decimal number (it may be negative and may have
up to 17 significant digits, e.g. 0.49999999999999994).

For each line, print the number rounded to the nearest integer. Values exactly halfway between two
integers round away from zero: 2.5 -> 3, -2.5 -> -3. Never print "-0"; print 0 instead.
```
