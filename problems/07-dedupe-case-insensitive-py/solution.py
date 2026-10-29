import sys

def main():
    seen = set()
    write = sys.stdout.write

    for line in sys.stdin:
        word = line.strip()
        if not word:
            continue

        key = word.casefold()
        if key not in seen:
            seen.add(key)
            write(word + '\n')

if __name__ == "__main__":
    main()
