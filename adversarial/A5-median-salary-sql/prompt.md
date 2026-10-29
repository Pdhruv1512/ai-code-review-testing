# A5: Median Salary per Department (SQL)

**Trap being tested:** SQLite has no MEDIAN function; NULLs must be excluded before finding the middle;
even counts need the average of two values; a department with only NULL salaries must still appear.

```
Write one SQLite query.

Table:
CREATE TABLE employees (
    id     INTEGER PRIMARY KEY,
    dept   TEXT NOT NULL,
    salary INTEGER          -- may be NULL
);

For each department, return the median salary, ignoring NULL salaries. If a department has an even
number of non-NULL salaries, the median is the average of the two middle values. If a department has
no non-NULL salaries, still return it with median_salary NULL.
Columns: dept, median_salary. Sort by dept.
```
