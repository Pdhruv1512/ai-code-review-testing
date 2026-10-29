WITH ranked AS (
    SELECT
        dept,
        salary,
        ROW_NUMBER() OVER (
            PARTITION BY dept
            ORDER BY salary
        ) AS rn,
        COUNT(salary) OVER (
            PARTITION BY dept
        ) AS cnt
    FROM employees
),
medians AS (
    SELECT
        dept,
        AVG(salary * 1.0) AS median_salary
    FROM ranked
    WHERE rn IN (
        (cnt + 1) / 2,
        (cnt + 2) / 2
    )
    GROUP BY dept
)
SELECT
    e.dept,
    m.median_salary
FROM (SELECT DISTINCT dept FROM employees) AS e
LEFT JOIN medians AS m
    ON m.dept = e.dept
ORDER BY e.dept;
