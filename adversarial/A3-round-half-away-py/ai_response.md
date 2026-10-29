# AI response: A3

- **Model:** ChatGPT (chatgpt.com, logged out, default model)
- **Date:** 2026-10-29
- **Code:** saved unchanged in `solution.py`

## AI's explanation (copied as written)

> Use Python's Decimal with ROUND_HALF_UP to round decimal numbers to the nearest integer, with halfway
> cases rounded away from zero. This avoids floating-point precision errors.

**Example** (given by the AI)

Input: `2.5 / -2.5 / 0.49999999999999994 / -0.4 / 3.7` → Output: `3 / -3 / 0 / 0 / 4`

**Why this works**

> Decimal(line) preserves the exact decimal value from the input.
>
> ROUND_HALF_UP rounds halfway cases away from zero for both positive and negative numbers.
>
> int(result) ensures that negative zero is printed as 0.
>
> The program processes every input line until EOF, making it suitable for programming contests.
