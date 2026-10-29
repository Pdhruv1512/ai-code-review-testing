SCHEMA = """
CREATE TABLE orders (
    id          INTEGER PRIMARY KEY,
    customer_id INTEGER NOT NULL,
    order_date  TEXT NOT NULL,
    amount      INTEGER NOT NULL
);
"""


def solve(rows):
    best = {}
    for oid, cid, d, amt in rows:
        if cid not in best or (d, oid) > (best[cid][2], best[cid][1]):
            best[cid] = (cid, oid, d, amt)
    return [best[c] for c in sorted(best)]


def case(name, category, rows):
    setup = "".join(f"INSERT INTO orders VALUES ({o}, {c}, '{d}', {a});\n" for o, c, d, a in rows)
    return {"name": name, "category": category, "setup": setup, "expected": solve(rows)}


CASES = [
    case("basic", "basic", [(1, 1, "2026-01-01", 10), (2, 1, "2026-02-01", 20), (3, 2, "2026-01-15", 5)]),
    case("two orders on the latest date", "trap", [(1, 1, "2026-03-01", 10), (2, 1, "2026-03-01", 20), (3, 1, "2026-01-01", 7)]),
    case("tie: higher id inserted first", "trap", [(9, 1, "2026-03-01", 10), (4, 1, "2026-03-01", 20)]),
    case("three-way tie", "trap", [(1, 1, "2026-05-05", 1), (2, 1, "2026-05-05", 2), (3, 1, "2026-05-05", 3)]),
    case("same date, different customers", "edge", [(1, 1, "2026-01-01", 10), (2, 2, "2026-01-01", 20)]),
    case("one order only", "edge", [(1, 3, "2026-01-01", 10)]),
    case("empty table", "edge", []),
]
