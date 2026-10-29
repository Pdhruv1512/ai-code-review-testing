from decimal import Decimal, ROUND_HALF_UP

TIME_LIMIT = 3.0


def r(s):
    v = Decimal(s).quantize(Decimal(1), rounding=ROUND_HALF_UP)  # HALF_UP in decimal = away from zero
    return "0" if v == 0 else str(v)


def case(name, category, lines):
    return {"name": name, "category": category, "input": "\n".join(lines) + "\n",
            "expected": "\n".join(r(s) for s in lines)}


CASES = [
    case("basic", "basic", ["1.2", "1.7", "3"]),
    case("positive halves", "trap", ["0.5", "1.5", "2.5", "3.5"]),
    case("negative halves", "trap", ["-0.5", "-1.5", "-2.5"]),
    case("negative non-halves", "edge", ["-1.2", "-1.7"]),
    case("small negative prints 0, not -0", "trap", ["-0.4", "-0.0"]),
    case("just below one half (17 digits)", "trap", ["0.49999999999999994"]),
    case("negative just below one half", "trap", ["-0.49999999999999994"]),
    case("half that a float cannot store", "trap", ["4503599627370496.5"]),
    case("large value", "edge", ["123456789012345.5"]),
]
