# A6: Reverse UTF-8 Text (C++)

**Trap being tested:** `std::reverse` on a `std::string` reverses bytes, which breaks any character
that takes more than one byte in UTF-8 (accents, Asian scripts, emoji).

```
Write a complete C++17 program that reads one line of UTF-8 text from standard input and prints its
characters in reverse order.

The text may contain non-English characters and emoji, for example "héllo" -> "olléh" and "日本" -> "本日".
Treat each Unicode code point as one character. The input is valid UTF-8 and may be empty.
```
