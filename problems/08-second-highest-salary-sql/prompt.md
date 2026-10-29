# Problem 08: Second Highest Salary (SQL)

Copy everything in the box below into the AI tool exactly as written.

```
Write one SQLite query.

Table:
CREATE TABLE employees (
    id     INTEGER PRIMARY KEY,
    name   TEXT NOT NULL,
    salary INTEGER          -- may be NULL
);

Return the second highest DISTINCT salary as a single column named second_salary.
The result must always be exactly one row. If there is no second highest distinct salary
(for example, every salary is the same, or the table is empty), return NULL in that row.
Ignore NULL salaries.
```
