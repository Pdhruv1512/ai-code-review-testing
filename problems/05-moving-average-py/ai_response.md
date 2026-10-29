# AI response: Problem 05

- **Model:** ChatGPT (chatgpt.com, logged out, default model)
- **Date:** 2026-10-29
- **Code:** saved unchanged in `solution.py`

## AI's explanation (copied as written)

**How it works**

> Input validation: If k < 1, prints INVALID.
>
> Insufficient numbers: If fewer than k numbers are provided, prints an empty line.
>
> Sliding window: Calculates the first window's sum, then updates it in constant time by adding the
> incoming number and subtracting the outgoing number.
>
> Formatting: Formats every average to exactly two decimal places.

**Complexity**

> Time: O(n), where n is the number of input numbers.
>
> Space: O(n) for storing the numbers and output averages.
>
> This approach efficiently handles 200,000 numbers with k = 1000 within the 3-second limit under
> normal execution conditions.
