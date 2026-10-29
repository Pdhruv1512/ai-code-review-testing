import sys
import re

def roman_to_int(s):
    pattern = r'^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$'

    if not s or not re.fullmatch(pattern, s):
        return "INVALID"

    values = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }

    total = 0
    for i in range(len(s)):
        if i + 1 < len(s) and values[s[i]] < values[s[i + 1]]:
            total -= values[s[i]]
        else:
            total += values[s[i]]

    return str(total) if 1 <= total <= 3999 else "INVALID"


def main():
    for line in sys.stdin:
        s = line.strip()
        print(roman_to_int(s))


if __name__ == "__main__":
    main()
