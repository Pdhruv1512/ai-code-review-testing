SCHEMA = """
CREATE TABLE employees (
    id     INTEGER PRIMARY KEY,
    dept   TEXT NOT NULL,
    salary INTEGER
);
"""


def median(vals):
    v = sorted(x for x in vals if x is not None)
    if not v:
        return None
    m = len(v) // 2
    return v[m] if len(v) % 2 else (v[m - 1] + v[m]) / 2


def case(name, category, rows):
    setup = "".join(f"INSERT INTO employees (dept, salary) VALUES ('{d}', {'NULL' if s is None else s});\n"
                    for d, s in rows)
    depts = sorted({d for d, _ in rows})
    return {"name": name, "category": category, "setup": setup,
            "expected": [(d, median([s for dd, s in rows if dd == d])) for d in depts]}


CASES = [
    case("odd count", "basic", [("A", 100), ("A", 300), ("A", 200)]),
    case("even count averages two middle values", "trap", [("A", 100), ("A", 200), ("A", 400), ("A", 1000)]),
    case("NULLs are ignored", "trap", [("A", None), ("A", 100), ("A", None), ("A", 300), ("A", 200)]),
    case("department with only NULLs", "trap", [("A", 100), ("B", None), ("B", None)]),
    case("several departments", "basic", [("B", 5), ("A", 1), ("A", 3), ("C", 7), ("C", 9), ("B", 6), ("B", 4)]),
    case("duplicate salaries", "edge", [("A", 50), ("A", 50), ("A", 50), ("A", 70)]),
    case("single employee", "edge", [("Z", 42)]),
    case("unsorted insert order", "edge", [("A", 900), ("A", 100), ("A", 500), ("A", 300)]),
]
