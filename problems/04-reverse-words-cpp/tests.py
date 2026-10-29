TIME_LIMIT = 2.0


def case(name, category, line):
    return {"name": name, "category": category, "input": line + "\n",
            # Only the space character separates words (per the prompt); tabs belong to words.
            "expected": " ".join(reversed([w for w in line.split(" ") if w]))}


CASES = [
    case("basic", "basic", "the sky is blue"),
    case("single word", "edge", "hello"),
    case("leading and trailing spaces", "edge", "   hello world   "),
    case("multiple spaces between words", "edge", "a   good    example"),
    case("empty line", "edge", ""),
    case("only spaces", "edge", "      "),
    case("punctuation stays attached", "spec", "Hello, world! How are you?"),
    case("numbers and symbols", "edge", "1 + 2 = 3"),
    case("tab is part of a word, not a separator", "review", "a\tb c"),
    case("long line (speed)", "performance", " ".join(f"w{i}" for i in range(200000))),
]
