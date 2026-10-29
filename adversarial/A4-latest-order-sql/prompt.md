# A4: Latest Order per Customer (SQL)

**Trap being tested:** joining on `MAX(order_date)` returns several rows when a customer has two orders on
their latest date.

```
Write one SQLite query.

Table:
CREATE TABLE orders (
    id          INTEGER PRIMARY KEY,
    customer_id INTEGER NOT NULL,
    order_date  TEXT NOT NULL,     -- 'YYYY-MM-DD'
    amount      INTEGER NOT NULL
);

For each customer, return exactly one row: their most recent order (latest order_date). If a customer
has several orders on that latest date, return the one with the highest id.
Columns: customer_id, id, order_date, amount. Sort by customer_id.
```
