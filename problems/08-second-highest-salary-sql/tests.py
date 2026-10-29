SCHEMA = """
CREATE TABLE employees (
    id     INTEGER PRIMARY KEY,
    name   TEXT NOT NULL,
    salary INTEGER          -- may be NULL
);
"""


def rows(*vals):
    return "".join(f"INSERT INTO employees (name, salary) VALUES ('E{i}', {v});\n"
                   for i, v in enumerate(vals))


CASES = [
    {"name": "basic", "category": "basic", "setup": rows(100, 200, 300), "expected": [(200,)]},
    {"name": "tie at the top", "category": "spec", "setup": rows(300, 300, 200, 100), "expected": [(200,)]},
    {"name": "tie at second place", "category": "edge", "setup": rows(300, 200, 200), "expected": [(200,)]},
    {"name": "only one distinct salary", "category": "spec", "setup": rows(500, 500, 500), "expected": [(None,)]},
    {"name": "single employee", "category": "edge", "setup": rows(500), "expected": [(None,)]},
    {"name": "empty table", "category": "edge", "setup": "", "expected": [(None,)]},
    {"name": "NULL salaries ignored", "category": "edge", "setup": rows("NULL", 400, "NULL", 100), "expected": [(100,)]},
    {"name": "all salaries NULL", "category": "edge", "setup": rows("NULL", "NULL"), "expected": [(None,)]},
    {"name": "negative and zero", "category": "edge", "setup": rows(0, -50, -10), "expected": [(-10,)]},
]
