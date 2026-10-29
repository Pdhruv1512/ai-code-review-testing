TIME_LIMIT = 3.0


def solve(lines):
    seen, out = set(), []
    for line in lines:
        w = line.strip()
        if not w:
            continue
        key = w.casefold()
        if key not in seen:
            seen.add(key)
            out.append(w)
    return "\n".join(out)


def case(name, category, lines):
    return {"name": name, "category": category, "input": "\n".join(lines) + "\n", "expected": solve(lines)}


CASES = [
    case("basic", "basic", ["apple", "banana", "apple"]),
    case("different case", "spec", ["Apple", "APPLE", "apple"]),
    case("keeps FIRST spelling", "spec", ["hELLo", "Hello", "hello"]),
    case("surrounding spaces ignored", "spec", ["  cat", "cat  ", "Cat"]),
    case("blank lines ignored", "edge", ["dog", "", "   ", "dog", "fish"]),
    case("order preserved", "spec", ["c", "b", "a", "B", "C"]),
    case("German sharp s", "spec", ["Straße", "STRASSE", "strasse"]),
    case("accented letters", "edge", ["Éclair", "éclair", "ÉCLAIR"]),
    case("empty input", "edge", []),
    case("200k lines (speed)", "performance", [f"Word{i % 50000}" for i in range(200000)]),
]
