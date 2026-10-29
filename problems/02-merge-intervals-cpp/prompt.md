# Problem 02: Merge Intervals (C++)

Copy everything in the box below into the AI tool exactly as written.

```
Write a complete C++17 program that reads from standard input and writes to standard output.

Input:
- First line: integer n (0 <= n <= 200000).
- Next n lines: two integers l r (-2 * 10^9 <= l <= r <= 2 * 10^9), an inclusive interval [l, r].
  Intervals are given in no particular order.

Merge all overlapping intervals. Intervals that share an endpoint, like [1, 2] and [2, 3],
count as overlapping and must be merged. Intervals like [1, 2] and [3, 4] do NOT overlap.

Output: the merged intervals sorted by start, one per line as "l r". Print nothing if n = 0.
The program must run in under 2 seconds for n = 200000.
```
