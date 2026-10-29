# Problem 10: Running Total per Customer (SQL)

Copy everything in the box below into the AI tool exactly as written.

```
Write one SQLite query.

Table:
CREATE TABLE orders (
    id          INTEGER PRIMARY KEY,
    customer_id INTEGER NOT NULL,
    order_date  TEXT NOT NULL,     -- 'YYYY-MM-DD'
    amount      INTEGER NOT NULL   -- may be negative (refunds)
);

For every order, show a running total of amount for that customer. Orders are counted in
order of order_date; when a customer has several orders on the same date, count them in order of id
(so each order's running total includes only the orders counted before it plus itself).

Columns: customer_id, id, order_date, amount, running_total
Sort by customer_id, then order_date, then id.
```
