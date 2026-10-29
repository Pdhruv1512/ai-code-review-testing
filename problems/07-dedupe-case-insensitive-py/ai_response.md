# AI response: Problem 07

- **Model:** ChatGPT (chatgpt.com, logged out, default model)
- **Date:** 2026-10-29
- **Code:** saved unchanged in `solution.py`

## AI's explanation (copied as written)

**Why this works**

> Case-insensitive Unicode comparison: casefold() handles non-English letters more thoroughly than
> lower(). For example, "Straße".casefold() and "STRASSE".casefold() both produce "strasse".
>
> Whitespace handling: strip() removes leading and trailing whitespace. The stripped version is printed.
>
> First occurrence preserved: A set tracks previously seen comparison keys, while lines are processed
> in input order.
>
> Blank lines skipped: Empty strings after stripping are ignored.
>
> Performance: Set lookups and insertions take O(1) expected time, giving O(n) expected time overall,
> where n is the total number of input characters. This is efficient for 200,000 lines.
>
> The program uses Python 3's built-in Unicode case folding and requires no external libraries.
