# AI response: Problem 10

- **Model:** ChatGPT (chatgpt.com, logged out, default model)
- **Date:** 2026-10-29
- **Code:** saved unchanged in `query.sql`

## AI's explanation (copied as written)

**Why it works:**

> PARTITION BY customer_id resets the running total for each customer.
>
> ORDER BY order_date, id ensures orders are processed chronologically, with ties broken by id.
>
> ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW sums every row from the customer's first order
> through the current order, including refunds (negative amounts).
>
> The final ORDER BY sorts the output as requested.
