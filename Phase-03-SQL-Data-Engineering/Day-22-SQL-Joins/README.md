# Day 22 — SQL Joins Deep Dive: Inner/Left/Right/Full, Self-Joins, Multi-Table Joins

**Topics:** INNER JOIN, LEFT JOIN, RIGHT JOIN (simulated in SQLite), FULL JOIN concept, SELF JOIN, multi-table joins combined with GROUP BY/ORDER BY

## What I Learned

- **INNER JOIN** — returns only rows with a match on both sides. Employees without a department (or departments without employees) are excluded entirely.
- **LEFT JOIN** — returns ALL rows from the left table, plus matching data from the right; unmatched right-side columns show as `NULL`/`None`.
- **RIGHT JOIN** — the mirror of LEFT JOIN, but SQLite doesn't reliably support it natively. Simulated by swapping which table is listed first with LEFT JOIN — starting the query `FROM departments LEFT JOIN employees` achieves the same result as `employees RIGHT JOIN departments`.
- **FULL JOIN** — returns everything from both tables, matched where possible. Also not natively supported in SQLite (would require a `UNION` of a LEFT and a RIGHT/swapped-LEFT join) — not directly practiced this session, but understood conceptually.
- **SELF JOIN** — a table joined to itself, essential for hierarchical data (employees referencing their own manager via `manager_id`). Requires table aliases (`e1`, `e2`) because otherwise SQL can't distinguish between two references to the identical table — the alias resolves the ambiguity.
- **Multi-table joins + aggregation** — joins combine directly with Day 21's GROUP BY/ORDER BY. Joining first, then grouping and ordering the joined result, is a natural, common pattern (e.g. average salary per department).
- **Why some rows silently disappear** — INNER JOIN drops any row lacking a match on either side, which is exactly why a department with zero employees (like "HR") vanishes from an INNER JOIN + GROUP BY result, even though it still exists in the source table.

## Diagram

Visualized INNER/LEFT/RIGHT/FULL JOIN as overlapping circles (Venn-diagram style): INNER = only the overlap, LEFT = entire left circle plus overlap, RIGHT = entire right circle plus overlap, FULL = both circles combined. SELF JOIN was shown separately as one table connecting to itself via two labeled aliases.

## Resources Used

- "SQL Joins in Hindi | INNER, LEFT, RIGHT, FULL Join Explained" — https://www.thevistaacademy.com/sql-joins-in-hindi-inner-left-right-full-join/

## Mistakes I Made & Fixed

- In Task 1, predicted the INNER JOIN result would have 5 rows, but the actual output had 6 — miscounted before verifying against the real printed result. A reminder to count actual output rather than estimate from memory when a task asks for a specific number.
- Minor typo in a written comment ("emloyee" instead of "employee") — not a conceptual issue, just a typing slip.
- Initial explanation for why SELF JOIN requires an alias was correct but too general ("we are joining the same table to itself") — refined to explain the actual mechanism: without an alias, SQL cannot distinguish between two references to the identical table, causing ambiguous column references.

## Exercises Completed

- [x] Task 1 — INNER JOIN
- [x] Task 2 — LEFT JOIN
- [x] Task 3 — RIGHT JOIN (simulated via table-order swap, since SQLite lacks native support)
- [x] Task 4 — SELF JOIN with aliases
- [x] Task 5 — Multi-table join combined with GROUP BY and ORDER BY

## Next Up

Day 23 — Window functions: ROW_NUMBER, RANK, LAG/LEAD, running totals; CTEs and subqueries