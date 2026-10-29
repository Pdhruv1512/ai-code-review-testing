TIME_LIMIT = 2.0
E18 = 10**18


def case(name, category, a):
    return {"name": name, "category": category,
            "input": f"{len(a)}\n{' '.join(map(str, a))}\n", "expected": str(sum(a))}


CASES = [
    case("basic", "basic", [1, 2, 3]),
    case("single maximum value", "edge", [E18]),
    case("zeros", "edge", [0, 0, 0]),
    case("sum fits in long long", "edge", [E18] * 9),
    case("sum just above long long max", "trap", [E18] * 9 + [223372036854775808]),
    case("ten maximum values", "trap", [E18] * 10),
    case("mixed large values", "trap", [999999999999999999, 987654321987654321, E18, 5, E18, E18, E18, E18, E18, E18]),
]
