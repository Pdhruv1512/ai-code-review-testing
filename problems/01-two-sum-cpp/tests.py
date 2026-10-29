import random

TIME_LIMIT = 2.0


def solve(n, target, a):
    # Reference: smallest i, then smallest j > i, with a[i] + a[j] == target.
    pos = {}
    for idx, v in enumerate(a):
        pos.setdefault(v, []).append(idx)
    import bisect
    for i, v in enumerate(a):
        lst = pos.get(target - v)
        if lst:
            k = bisect.bisect_right(lst, i)
            if k < len(lst):
                return f"{i} {lst[k]}"
    return "-1 -1"


def case(name, category, n, target, a):
    inp = f"{n} {target}\n{' '.join(map(str, a))}\n"
    return {"name": name, "category": category, "input": inp, "expected": solve(n, target, a)}


random.seed(1)
big = [random.randrange(0, 10**9, 2) for _ in range(100000)]

CASES = [
    case("basic example", "basic", 4, 9, [2, 7, 11, 15]),
    case("answer at the end", "basic", 5, 11, [1, 2, 3, 4, 7]),
    case("no pair exists", "edge", 4, 100, [1, 2, 3, 4]),
    case("single element", "edge", 1, 10, [5]),
    case("same value twice", "edge", 2, 6, [3, 3]),
    case("can't use one element twice", "edge", 3, 6, [3, 1, 5]),
    case("negative numbers", "edge", 5, -8, [-3, -5, 2, -4, 9]),
    case("tie-break: smallest i first", "spec", 4, 4, [2, 1, 3, 2]),
    case("many duplicates", "spec", 5, 6, [3, 3, 3, 3, 3]),
    case("sum overflows 32-bit int", "edge", 2, 4000000000, [2000000000, 2000000000]),
    case("large input, no pair (speed)", "performance", 100000, 1, big),
]
