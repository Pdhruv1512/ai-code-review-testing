# AI response: Problem 01

- **Model:** ChatGPT (chatgpt.com, logged out, default model)
- **Date:** 2026-10-29
- **Code:** saved unchanged in `solution.cpp`

## AI's explanation (copied as written)

> Here is a complete C++17 solution that runs in O(n log n) time and uses O(n) extra space.
> It guarantees the required tie-breaking: smallest i, then smallest j.

**Why this works**

> The algorithm processes indices j in increasing order.
>
> Before checking index j, the hash map contains the earliest index of every value seen at an earlier position.
>
> If target - a[j] exists in the map, the algorithm has found a valid pair.
>
> The first pair found has the smallest possible j. For that j, the map stores the smallest possible i,
> so the tie-breaking requirements are satisfied.
>
> Using long long prevents integer overflow when calculating the complement.

**Complexity**

> Expected time: O(n) using a hash map, which comfortably meets the 2-second requirement for n = 100000.
>
> Space: O(n).
>
> The program prints the indices using zero-based indexing and outputs -1 -1 when no valid pair exists.
