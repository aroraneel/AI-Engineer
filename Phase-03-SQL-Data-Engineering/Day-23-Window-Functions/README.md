# Day 23 — Window Functions: ROW_NUMBER, RANK, LAG/LEAD, Running Totals; CTEs and Subqueries

**Topics:** ROW_NUMBER, RANK vs DENSE_RANK, LAG, running totals with SUM() OVER, CTEs and subqueries for filtering window function results

## What I Learned

- **Window functions** calculate across a set of related rows WITHOUT collapsing them into one summary row — unlike GROUP BY, every original row stays visible alongside the calculated value.
- **The OVER() clause** defines the "window": `PARTITION BY` splits rows into independent groups (like GROUP BY but without collapsing), and `ORDER BY` inside OVER controls processing order (essential for ranking and running totals).
- **ROW_NUMBER()** — assigns a unique sequential number per partition, no ties possible. Forgetting `PARTITION BY` means numbering continues across the entire result instead of resetting per group.
- **RANK() vs DENSE_RANK()** — both give tied rows the same rank, but RANK() skips the next number(s) after a tie (1, 1, 3), while DENSE_RANK() does not (1, 1, 2). Verified directly on a real tie in the data (Riya and Vikram both at 7000).
- **LAG()** — pulls a value from a previous row within the window, defaulting to `NULL` when no such row exists (e.g., the very first row in an ordered sequence). Used for month-over-month comparisons without needing a self-join.
- **Running totals** — combining `SUM()` with `OVER (PARTITION BY ... ORDER BY ...)` produces a cumulative sum per row, per group — genuinely different from `GROUP BY`, which would collapse everything into one total row per group and lose the row-by-row progression.
- **Critical gotcha:** window functions run AFTER `WHERE` in SQL's execution order, so a window function's result (like a rank) cannot be filtered directly with `WHERE` in the same query — same underlying reason Day 21's `HAVING` exists for aggregates.
- **CTEs and subqueries** solve this — calculate the window function first (inside the CTE/subquery), then filter on that result in the outer query. This is the standard pattern for the classic "top N per group" interview question.

## Resources Used

- "Window Functions in SQL Full Tutorial 🔥 | ROW_NUMBER, RANK, LAG, LEAD Explained" — https://www.youtube.com/watch?v=MnDqhGAcRug

## Mistakes I Made & Fixed

- No functional bugs this session — all 5 tasks were correct on the first working attempt, with only minor typos in written explanations (e.g. "diffrence," "bacause") that didn't affect the underlying reasoning.
- Used a subquery instead of a CTE (`WITH ... AS`) for Task 5 — functionally equivalent and fully valid, since the task allowed either approach, but worth practicing the CTE syntax specifically next time for readability on more complex multi-step queries.

## Exercises Completed

- [x] Task 1 — ROW_NUMBER with PARTITION BY
- [x] Task 2 — RANK vs DENSE_RANK on tied data
- [x] Task 3 — LAG for month-over-month comparison
- [x] Task 4 — Running total with SUM() OVER
- [x] Task 5 — CTE/subquery for the "top N per group" pattern

## Next Up

Day 24 — Advanced SQL: query optimization, indexes, reading EXPLAIN plans