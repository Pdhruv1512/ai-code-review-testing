# AI response: Problem 06

- **Model:** ChatGPT (chatgpt.com, logged out, default model)
- **Date:** 2026-10-29
- **Code:** saved unchanged in `solution.py`

## AI's explanation (copied as written)

**How it works**

> Validation: A regular expression checks that the string follows standard Roman numeral rules,
> including valid subtractive pairs such as IV, IX, XL, XC, CD, and CM.
>
> Conversion: Each symbol's value is added unless it is smaller than the following symbol, in which
> case it is subtracted.
>
> Input/output: Reads each line from standard input and prints the integer value or INVALID.

**Example** (given by the AI)

Input: `III / MCMXCIV / IIII / ABC` → Output: `3 / 1994 / INVALID / INVALID`

> The program processes each line independently and supports all valid standard Roman numerals from
> I (1) through MMMCMXCIX (3999).
