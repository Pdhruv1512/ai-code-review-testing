# Problem 09: Customers Without Orders (SQL)

Copy everything in the box below into the AI tool exactly as written.

```
Write one SQLite query.

Tables:
CREATE TABLE customers (
    id   INTEGER PRIMARY KEY,
    name TEXT NOT NULL
);
CREATE TABLE orders (
    id          INTEGER PRIMARY KEY,
    customer_id INTEGER,     -- may be NULL (guest checkout)
    amount      INTEGER NOT NULL
);

Return every customer who has never placed an order.
Columns: id, name. Sort by id ascending. Different customers can have the same name.
```
