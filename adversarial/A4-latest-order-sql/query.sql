SELECT customer_id, id, order_date, amount
FROM (
    SELECT *,
           ROW_NUMBER() OVER (
               PARTITION BY customer_id
               ORDER BY order_date DESC, id DESC
           ) AS rn
    FROM orders
)
WHERE rn = 1
ORDER BY customer_id;
