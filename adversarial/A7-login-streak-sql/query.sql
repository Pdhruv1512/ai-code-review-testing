WITH distinct_days AS (
    SELECT DISTINCT user_id, login_date
    FROM logins
),
grouped_days AS (
    SELECT
        user_id,
        login_date,
        date(
            login_date,
            '-' || ROW_NUMBER() OVER (
                PARTITION BY user_id
                ORDER BY login_date
            ) || ' days'
        ) AS streak_group
    FROM distinct_days
),
streaks AS (
    SELECT
        user_id,
        streak_group,
        COUNT(*) AS streak_length
    FROM grouped_days
    GROUP BY user_id, streak_group
)
SELECT
    user_id,
    MAX(streak_length) AS longest_streak
FROM streaks
GROUP BY user_id
ORDER BY user_id;
