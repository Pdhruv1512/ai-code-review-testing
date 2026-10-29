# AI response: Problem 04

- **Model:** ChatGPT (chatgpt.com, logged out, default model)
- **Date:** 2026-10-29
- **Code:** saved unchanged in `solution.cpp`

## AI's explanation (copied as written)

**How it works**

> getline(cin, line) reads one complete line, including leading and trailing spaces.
>
> istringstream with iss >> word extracts words while automatically skipping consecutive spaces.
>
> The words are stored in a vector<string>.
>
> A loop prints the words in reverse order, inserting exactly one space between them.
>
> If the input is empty or contains only spaces, no words are printed, and the program outputs an empty line.
>
> Time complexity: O(n), where n is the line length.
>
> Space complexity: O(n), to store the input and extracted words.
>
> The program supports C++17 and handles lines up to 2,000,000 characters long.
