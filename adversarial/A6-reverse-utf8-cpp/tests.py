TIME_LIMIT = 2.0


def case(name, category, text):
    return {"name": name, "category": category, "input": text + "\n", "expected": text[::-1]}


CASES = [
    case("ASCII only", "basic", "hello world"),
    case("accented letters (2 bytes)", "trap", "héllo café"),
    case("Japanese (3 bytes)", "trap", "日本語"),
    case("emoji (4 bytes)", "trap", "hi 😀🎉"),
    case("mixed scripts", "trap", "a€b日c😀"),
    case("single multi-byte character", "edge", "é"),
    case("empty line", "edge", ""),
    case("long line (speed)", "performance", "aé日😀" * 100000),
]
