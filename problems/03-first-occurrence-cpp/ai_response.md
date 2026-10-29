# AI response: Problem 03

- **Model:** ChatGPT (chatgpt.com, logged out, default model)
- **Date:** 2026-10-29
- **Code:** saved unchanged in `solution.cpp`

## AI's explanation (copied as written)

> Here is a complete C++17 solution using std::lower_bound, which finds the first occurrence of each
> query value in a sorted array.

**How it works**

> lower_bound(a.begin(), a.end(), x) returns an iterator to the first element that is greater than or equal to x.
>
> If that element equals x, its iterator difference from a.begin() gives the 0-based index of the first occurrence.
>
> If the iterator equals a.end() or the element differs from x, the value is absent, so the program prints -1.

**Complexity analysis**

> Time: O(n + q log n). Reading the array takes O(n), and each of the q queries takes O(log n).
>
> Space: O(n) for storing the array.
>
> With n = q = 200,000, this solution performs roughly 3.6 million binary-search comparisons at most,
> making it suitable for a 2-second time limit under typical competitive programming constraints.
