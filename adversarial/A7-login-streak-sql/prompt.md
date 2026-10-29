# A7: Longest Login Streak (SQL)

**Trap being tested:** "gaps and islands" with duplicate rows. If a user logs in twice on one day,
`date - ROW_NUMBER()` no longer gives the same value for consecutive days, which splits a streak.

```
Write one SQLite query.

Table:
CREATE TABLE logins (
    user_id    INTEGER NOT NULL,
    login_date TEXT NOT NULL      -- 'YYYY-MM-DD'; a user can log in several times on the same day
);

For each user, return the length of their longest streak of consecutive calendar days with at least
one login. Columns: user_id, longest_streak. Sort by user_id.
```
