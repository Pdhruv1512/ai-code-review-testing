import random

TIME_LIMIT = 2.0


def solve(iv):
    iv = sorted(iv)
    out = []
    for l, r in iv:
        if out and l <= out[-1][1]:
            out[-1][1] = max(out[-1][1], r)
        else:
            out.append([l, r])
    return "\n".join(f"{l} {r}" for l, r in out)


def case(name, category, iv):
    inp = f"{len(iv)}\n" + "".join(f"{l} {r}\n" for l, r in iv)
    return {"name": name, "category": category, "input": inp, "expected": solve(iv)}


random.seed(2)
big = []
for _ in range(200000):
    l = random.randint(-10**9, 10**9 - 1000)
    big.append((l, l + random.randint(0, 1000)))

CASES = [
    case("basic overlap", "basic", [(1, 3), (2, 6), (8, 10), (15, 18)]),
    case("unsorted input", "edge", [(8, 10), (1, 3), (2, 6)]),
    case("touching intervals merge", "spec", [(1, 2), (2, 3)]),
    case("adjacent intervals stay separate", "spec", [(1, 2), (3, 4)]),
    case("one interval inside another", "edge", [(1, 10), (2, 3), (4, 5)]),
    case("inner interval comes first", "edge", [(2, 3), (1, 10)]),
    case("duplicates", "edge", [(5, 5), (5, 5), (5, 5)]),
    case("negative values", "edge", [(-10, -5), (-6, 0), (1, 2)]),
    case("empty input", "edge", []),
    case("single point interval", "edge", [(7, 7)]),
    case("values near int limits", "edge", [(-2000000000, 0), (0, 2000000000)]),
    case("200k intervals (speed)", "performance", big),
]
