# A1: Pairs With a Sum Divisible by k (C++)

**Trap being tested:** `%` on negative numbers in C++, a pair count that overflows `int`, and k too large for an array of remainders.

```
Write a complete C++17 program that reads from standard input and writes to standard output.

Input:
- First line: two integers n and k (1 <= n <= 200000, 1 <= k <= 10^9).
- Second line: n integers a[0..n-1] (|a[i]| <= 10^9).

Count the pairs (i, j) with i < j such that a[i] + a[j] is divisible by k. Print the count.
The program must run in under 2 seconds.
```
