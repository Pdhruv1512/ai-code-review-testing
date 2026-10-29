from datetime import date

SCHEMA = """
CREATE TABLE logins (
    user_id    INTEGER NOT NULL,
    login_date TEXT NOT NULL
);
"""


def solve(rows):
    by_user = {}
    for u, d in rows:
        by_user.setdefault(u, set()).add(date.fromisoformat(d).toordinal())
    out = []
    for u in sorted(by_user):
        days = sorted(by_user[u])
        best = cur = 1
        for a, b in zip(days, days[1:]):
            cur = cur + 1 if b == a + 1 else 1
            best = max(best, cur)
        out.append((u, best))
    return out


def case(name, category, rows):
    setup = "".join(f"INSERT INTO logins VALUES ({u}, '{d}');\n" for u, d in rows)
    return {"name": name, "category": category, "setup": setup, "expected": solve(rows)}


CASES = [
    case("basic streak", "basic", [(1, "2026-01-01"), (1, "2026-01-02"), (1, "2026-01-03"), (1, "2026-01-05")]),
    case("two logins on the same day", "trap", [(1, "2026-01-01"), (1, "2026-01-02"), (1, "2026-01-02"), (1, "2026-01-03")]),
    case("many duplicates inside a streak", "trap", [(1, "2026-03-01")] * 3 + [(1, "2026-03-02")] * 2 + [(1, "2026-03-03")]),
    case("streak across a month end", "trap", [(1, "2026-01-30"), (1, "2026-01-31"), (1, "2026-02-01")]),
    case("streak across a leap day", "edge", [(1, "2028-02-28"), (1, "2028-02-29"), (1, "2028-03-01")]),
    case("several users", "basic", [(2, "2026-01-01"), (1, "2026-01-01"), (2, "2026-01-02"), (1, "2026-01-03")]),
    case("single login", "edge", [(5, "2026-06-06")]),
    case("rows inserted out of order", "edge", [(1, "2026-01-03"), (1, "2026-01-01"), (1, "2026-01-02")]),
]
