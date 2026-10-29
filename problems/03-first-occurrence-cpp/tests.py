import bisect
import random

TIME_LIMIT = 2.0


def solve(a, qs):
    out = []
    for q in qs:
        k = bisect.bisect_left(a, q)
        out.append(str(k) if k < len(a) and a[k] == q else "-1")
    return "\n".join(out)


def case(name, category, a, qs):
    inp = f"{len(a)} {len(qs)}\n{' '.join(map(str, a))}\n{' '.join(map(str, qs))}\n"
    return {"name": name, "category": category, "input": inp, "expected": solve(a, qs)}


random.seed(3)
big = sorted(random.randint(-10**9, 10**9) for _ in range(200000))
big_q = [random.choice(big) if i % 2 else random.randint(-10**9, 10**9) for i in range(200000)]

CASES = [
    case("basic", "basic", [1, 3, 5, 7, 9], [5, 1, 9]),
    case("value missing", "basic", [1, 3, 5, 7, 9], [4]),
    case("duplicates: return FIRST index", "spec", [2, 2, 2, 2, 3], [2]),
    case("duplicates in the middle", "spec", [1, 4, 4, 4, 4, 4, 8], [4]),
    case("smaller than all", "edge", [10, 20, 30], [5]),
    case("larger than all", "edge", [10, 20, 30], [40]),
    case("single element found", "edge", [7], [7]),
    case("single element missing", "edge", [7], [8]),
    case("int limits", "edge", [-2147483648, 0, 2147483647], [2147483647, -2147483648]),
    case("all values equal", "edge", [5] * 1000, [5, 4, 6]),
    case("200k queries (speed)", "performance", big, big_q),
]
