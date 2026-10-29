SCHEMA = """
CREATE TABLE customers (
    id   INTEGER PRIMARY KEY,
    name TEXT NOT NULL
);
CREATE TABLE orders (
    id          INTEGER PRIMARY KEY,
    customer_id INTEGER,     -- may be NULL (guest checkout)
    amount      INTEGER NOT NULL
);
"""

BASE = """
INSERT INTO customers VALUES (1, 'Asha'), (2, 'Ben'), (3, 'Carla'), (4, 'Dev');
"""

CASES = [
    {"name": "basic", "category": "basic",
     "setup": BASE + "INSERT INTO orders (customer_id, amount) VALUES (1, 50), (3, 20);",
     "expected": [(2, "Ben"), (4, "Dev")]},
    {"name": "customer with many orders", "category": "edge",
     "setup": BASE + "INSERT INTO orders (customer_id, amount) VALUES (1, 5), (1, 6), (1, 7), (2, 1);",
     "expected": [(3, "Carla"), (4, "Dev")]},
    {"name": "guest orders with NULL customer_id", "category": "spec",
     "setup": BASE + "INSERT INTO orders (customer_id, amount) VALUES (1, 50), (NULL, 20);",
     "expected": [(2, "Ben"), (3, "Carla"), (4, "Dev")]},
    {"name": "no orders at all", "category": "edge", "setup": BASE,
     "expected": [(1, "Asha"), (2, "Ben"), (3, "Carla"), (4, "Dev")]},
    {"name": "everyone has ordered", "category": "edge",
     "setup": BASE + "INSERT INTO orders (customer_id, amount) VALUES (1, 1), (2, 1), (3, 1), (4, 1);",
     "expected": []},
    {"name": "two customers with same name", "category": "spec",
     "setup": "INSERT INTO customers VALUES (1, 'Sam'), (2, 'Sam'), (3, 'Zoe');"
              "INSERT INTO orders (customer_id, amount) VALUES (1, 10);",
     "expected": [(2, "Sam"), (3, "Zoe")]},
    {"name": "order for deleted customer id", "category": "edge",
     "setup": BASE + "INSERT INTO orders (customer_id, amount) VALUES (99, 10), (2, 5);",
     "expected": [(1, "Asha"), (3, "Carla"), (4, "Dev")]},
    {"name": "sorted by id, not name", "category": "spec",
     "setup": "INSERT INTO customers VALUES (1, 'Zed'), (2, 'Amy'), (3, 'Max');",
     "expected": [(1, "Zed"), (2, "Amy"), (3, "Max")]},
]
