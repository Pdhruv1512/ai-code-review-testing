TIME_LIMIT = 3.0


def to_roman(n):
    vals = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"), (90, "XC"),
            (50, "L"), (40, "XL"), (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")]
    out = ""
    for v, s in vals:
        while n >= v:
            out += s
            n -= v
    return out


VALID = {to_roman(i): i for i in range(1, 4000)}


def case(name, category, lines):
    return {"name": name, "category": category, "input": "\n".join(lines) + "\n",
            "expected": "\n".join(str(VALID.get(s, "INVALID")) for s in lines)}


CASES = [
    case("basic", "basic", ["III", "LVIII", "MCMXCIV"]),
    case("all subtractive pairs", "basic", ["IV", "IX", "XL", "XC", "CD", "CM"]),
    case("largest value", "edge", ["MMMCMXCIX"]),
    case("smallest value", "edge", ["I"]),
    case("four in a row is invalid", "spec", ["IIII", "XXXX", "CCCC"]),
    case("repeated V/L/D is invalid", "spec", ["VV", "LL", "DD"]),
    case("bad subtraction is invalid", "spec", ["IL", "IC", "XD", "VX", "IIV"]),
    case("4000 and above is invalid", "spec", ["MMMM"]),
    case("lowercase is invalid", "spec", ["xiv"]),
    case("non-roman letters invalid", "edge", ["ABC", "X1"]),
    case("wrong order is invalid", "spec", ["IM", "XM", "VIV"]),
    case("every valid numeral 1-3999", "performance", list(VALID)),
]
