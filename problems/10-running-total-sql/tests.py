SCHEMA = """
CREATE TABLE orders (
    id          INTEGER PRIMARY KEY,
    customer_id INTEGER NOT NULL,
    order_date  TEXT NOT NULL,     -- 'YYYY-MM-DD'
    amount      INTEGER NOT NULL
);
"""


def solve(rows):
    rows = sorted(rows, key=lambda r: (r[1], r[2], r[0]))
    out, totals = [], {}
    for oid, cid, d, amt in rows:
        totals[cid] = totals.get(cid, 0) + amt
        out.append((cid, oid, d, amt, totals[cid]))
    return out


def case(name, category, rows):
    setup = "".join(f"INSERT INTO orders VALUES ({o}, {c}, '{d}', {a});\n" for o, c, d, a in rows)
    return {"name": name, "category": category, "setup": setup, "expected": solve(rows)}


CASES = [
    case("basic, one customer", "basic", [(1, 1, "2026-01-01", 10), (2, 1, "2026-01-05", 20), (3, 1, "2026-01-09", 5)]),
    case("two customers kept separate", "basic", [(1, 1, "2026-01-01", 10), (2, 2, "2026-01-02", 7),
                                                   (3, 1, "2026-01-03", 5), (4, 2, "2026-01-04", 3)]),
    case("inserted out of date order", "edge", [(1, 1, "2026-03-01", 10), (2, 1, "2026-01-01", 20)]),
    case("same-day orders add one by one", "spec", [(1, 1, "2026-01-01", 10), (2, 1, "2026-01-01", 20),
                                                     (3, 1, "2026-01-02", 5)]),
    case("same-day tie broken by id", "spec", [(5, 1, "2026-01-01", 1), (3, 1, "2026-01-01", 100)]),
    case("negative amount (refund)", "edge", [(1, 1, "2026-01-01", 50), (2, 1, "2026-01-02", -20)]),
    case("empty table", "edge", []),
    case("dates across a year boundary", "edge", [(1, 1, "2025-12-31", 4), (2, 1, "2026-01-01", 6)]),
]
