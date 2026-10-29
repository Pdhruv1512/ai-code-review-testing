import random

TIME_LIMIT = 3.0


def solve(k, nums):
    if k < 1:
        return "INVALID"
    if len(nums) < k:
        return ""
    out, s = [], sum(nums[:k])
    out.append(s / k)
    for i in range(k, len(nums)):
        s += nums[i] - nums[i - k]
        out.append(s / k)
    # A value that rounds to zero is printed as 0.00, never -0.00.
    return " ".join(f"{x:.2f}".replace("-0.00", "0.00") for x in out)


def case(name, category, k, nums, raw=None):
    line = raw if raw is not None else " ".join(map(str, nums))
    return {"name": name, "category": category, "input": f"{k}\n{line}\n", "expected": solve(k, nums)}


random.seed(5)
big = [random.randint(1, 1000) for _ in range(200000)]  # positive, so this test only measures speed

CASES = [
    case("basic", "basic", 3, [1, 2, 3, 4, 5]),
    case("window of 1", "edge", 1, [4, 8, 15]),
    case("window equals list length", "edge", 4, [2, 4, 6, 8]),
    case("window larger than list", "edge", 5, [1, 2, 3]),
    case("empty list", "edge", 2, []),
    case("k = 0 is invalid", "spec", 0, [1, 2, 3]),
    case("negative k is invalid", "spec", -2, [1, 2, 3]),
    case("negative numbers", "edge", 2, [-4, -6, 10, -2]),
    case("decimal numbers", "edge", 2, [1.5, 2.3, 3.1]),
    case("rounding to 2 decimals", "spec", 3, [1, 1, 2, 2]),
    # Added after manual review: floating-point sums can make an exact zero print as "-0.00".
    {"name": "average exactly zero prints 0.00", "category": "review",
     "input": "3\n-0.1 -0.2 0.3\n", "expected": "0.00"},
    # k = 999 so no average of integers lands exactly on a rounding tie (x.xx5);
    # the prompt does not define how ties round.
    case("200k numbers, k=999 (speed)", "performance", 999, big),
]
