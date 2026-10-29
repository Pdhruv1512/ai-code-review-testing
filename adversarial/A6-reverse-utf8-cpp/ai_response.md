# AI response: A6

- **Model:** ChatGPT (chatgpt.com, logged out, default model)
- **Date:** 2026-10-29
- **Code:** saved unchanged in `solution.cpp`

## AI's explanation (copied as written)

> Here is a complete C++17 program that reverses a UTF-8 string by Unicode code point, rather than by
> individual bytes. It preserves non-English characters and emoji.

**Examples** (given by the AI): `héllo` → `olléh`, `日本` → `本日`, `Hello 🌍!` → `!🌍 olleH`

**How it works**

> Read one line using getline, including spaces and allowing empty input.
>
> Determine each UTF-8 code point's byte length from its leading byte.
>
> Store each complete code point as a separate string.
>
> Reverse the vector of code points and print them in order.
>
> Complexity: O(n) time and O(n) additional space, where n is the input length in bytes.
>
> Note: This reverses Unicode code points, as requested, not user-perceived grapheme clusters. For example,
> a base letter followed by a combining accent will be reversed as two code points.
