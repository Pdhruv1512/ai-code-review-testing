import random
from collections import Counter

TIME_LIMIT = 2.0


def solve(k, a):
    cnt = Counter(x % k for x in a)  # Python % is always non-negative
    total = 0
    for r, c in cnt.items():
        s = (k - r) % k
        if r < s:
            total += c * cnt.get(s, 0)
        elif r == s:
            total += c * (c - 1) // 2
    return str(total)


def case(name, category, k, a):
    return {"name": name, "category": category,
            "input": f"{len(a)} {k}\n{' '.join(map(str, a))}\n", "expected": solve(k, a)}


random.seed(11)
CASES = [
    case("basic", "basic", 3, [1, 2, 3, 4, 5, 6]),
    case("negative numbers", "trap", 5, [-1, 1, -6, 4, 9, -4]),
    case("negative and zero remainder", "trap", 4, [-4, 4, 8, -8, 0]),
    case("single element", "edge", 7, [7]),
    case("k = 1 (every pair)", "edge", 1, [5, -3, 9, 2]),
    case("k larger than all values", "trap", 10**9, [10**9 - 1, 1, -1, 999999999, 0, 0]),
    case("count overflows 32-bit int", "trap", 2, [2] * 200000),
    case("200k random values (speed)", "performance", 1000003,
         [random.randint(-10**9, 10**9) for _ in range(200000)]),
]
