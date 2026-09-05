# SQL — Cheat Sheet

A quick reference covering core SQL query clauses, joins, window
functions, and query optimization basics.

---

## Query Execution Order (memorize this)

SQL clauses are WRITTEN in one order, but EXECUTED in a different order:

```
1. FROM       -- pick the table
2. WHERE      -- filter individual rows
3. GROUP BY   -- group the remaining rows
4. HAVING     -- filter the groups
5. SELECT     -- choose which columns to show
6. ORDER BY   -- sort the final result
```

This explains most "why can't I filter on X here" questions in SQL.

---

## 1. Core Clauses

### SELECT — choose columns
```sql
SELECT column1, column2 FROM table_name;
SELECT * FROM table_name;   -- all columns (avoid on wide/large tables)
```

### WHERE — filter rows (before grouping)
```sql
SELECT * FROM employees WHERE department = 'Sales';
SELECT * FROM employees WHERE salary > 55000;
```
Operators: `=`, `>`, `<`, `>=`, `<=`, `!=`, `AND`, `OR`, `LIKE`

### ORDER BY — sort results
```sql
SELECT * FROM employees ORDER BY salary DESC;   -- high to low
SELECT * FROM employees ORDER BY salary ASC;    -- low to high (default)
```

### GROUP BY — group rows for aggregation
```sql
SELECT department, AVG(salary) FROM employees GROUP BY department;
```
Aggregate functions: `COUNT()`, `SUM()`, `AVG()`, `MAX()`, `MIN()`

### HAVING — filter groups (after aggregation)
```sql
SELECT department, AVG(salary) FROM employees
GROUP BY department
HAVING AVG(salary) > 60000;
```
**Key rule:** use HAVING (not WHERE) when filtering on an aggregate
result — WHERE runs before GROUP BY, so the aggregate doesn't exist yet.

---

## 2. Joins

### INNER JOIN — only matching rows
```sql
SELECT e.name, d.department_name
FROM employees e
INNER JOIN departments d ON e.department_id = d.id;
```

### LEFT JOIN — all of left table + matches
```sql
SELECT e.name, d.department_name
FROM employees e
LEFT JOIN departments d ON e.department_id = d.id;
```
Unmatched right-side columns show as `NULL`.

### RIGHT JOIN — all of right table + matches
```sql
-- SQLite doesn't support RIGHT JOIN natively.
-- Simulate it by swapping table order with LEFT JOIN:
SELECT d.department_name, e.name
FROM departments d
LEFT JOIN employees e ON d.id = e.department_id;
```

### FULL JOIN — everything, both sides
```sql
-- Not natively supported in SQLite. Simulate with UNION:
SELECT * FROM employees e LEFT JOIN departments d ON e.department_id = d.id
UNION
SELECT * FROM departments d LEFT JOIN employees e ON d.id = e.department_id;
```

### SELF JOIN — table joined to itself (aliases required)
```sql
SELECT e1.name AS employee, e2.name AS manager
FROM employees e1
LEFT JOIN employees e2 ON e1.manager_id = e2.id;
```
Aliases are required because SQL can't otherwise distinguish two
references to the identical table.

### Multi-table joins
```sql
-- n tables need n-1 JOIN clauses
SELECT a.col, b.col, c.col
FROM table_a a
JOIN table_b b ON a.id = b.a_id
JOIN table_c c ON b.id = c.b_id;
```

**Join type decision guide:**

| Need | Join |
|---|---|
| Only rows that match on both sides | INNER JOIN |
| All of table A, matches from B | LEFT JOIN |
| All of table B, matches from A | RIGHT JOIN (or swap + LEFT) |
| Everything from both sides | FULL JOIN (or UNION of LEFT + swapped LEFT) |
| A table related to itself (e.g. employee/manager) | SELF JOIN with aliases |

---

## 3. Window Functions

All window functions use `OVER()` and calculate across related rows
WITHOUT collapsing them (unlike GROUP BY).

```sql
SOME_FUNCTION() OVER (PARTITION BY column ORDER BY column)
```
- `PARTITION BY` — splits rows into independent groups (no collapsing)
- `ORDER BY` (inside OVER) — controls processing order

### ROW_NUMBER — unique sequential numbering
```sql
SELECT name, department, salary,
       ROW_NUMBER() OVER (PARTITION BY department ORDER BY salary DESC) AS rn
FROM employees;
```

### RANK vs DENSE_RANK — handling ties
```sql
RANK()       -- ties share a rank, next rank SKIPS numbers (1,1,3)
DENSE_RANK() -- ties share a rank, next rank does NOT skip (1,1,2)
```

### LAG / LEAD — compare to neighboring rows
```sql
SELECT month, revenue,
       LAG(revenue, 1) OVER (ORDER BY month) AS prev_month_revenue
FROM monthly_revenue;
```
`LAG` = previous row, `LEAD` = following row. Both return `NULL` when no
such row exists (e.g. first row has no previous).

### Running totals
```sql
SELECT month, revenue,
       SUM(revenue) OVER (ORDER BY month) AS running_total
FROM monthly_revenue;
```

### The critical gotcha
Window functions run AFTER `WHERE` — you CANNOT filter on a window
function's result directly with `WHERE` in the same query.

**Fix: use a CTE or subquery**
```sql
-- CTE version
WITH ranked AS (
    SELECT name, department, salary,
           RANK() OVER (PARTITION BY department ORDER BY salary DESC) AS rnk
    FROM employees
)
SELECT * FROM ranked WHERE rnk <= 3;

-- Subquery version (equivalent)
SELECT * FROM (
    SELECT name, department, salary,
           RANK() OVER (PARTITION BY department ORDER BY salary DESC) AS rnk
    FROM employees
) t
WHERE rnk <= 3;
```
This is the standard pattern for "top N per group" queries.

---

## 4. Query Optimization & Indexes

### Creating an index
```sql
CREATE INDEX idx_customer_email ON customers(email);
```
- **Primary index** — automatic on the primary key
- **Secondary index** — manually created on other frequently-queried columns

**The tradeoff:** indexes speed up reads (SELECT), but slow down writes
(INSERT/UPDATE/DELETE), since the index itself must update too. Don't
index every column — only ones used often in WHERE/JOIN/ORDER BY.

### Composite indexes — order matters
```sql
CREATE INDEX idx_city_name ON customers(city, name);
```
Only speeds up queries filtering by `city` alone, or `city` AND `name`
together — NOT `name` alone. Composite indexes work strictly left to right.

### Reading EXPLAIN QUERY PLAN (SQLite)
```sql
EXPLAIN QUERY PLAN SELECT * FROM customers WHERE email = 'x@test.com';
```
- `SCAN table_name` → full table scan, checking every row (slow, often
  means a missing/unused index)
- `SEARCH table_name USING INDEX ...` → the database used an index
  (fast, targeted lookup)

### LIKE patterns and indexes
```sql
LIKE 'abc%'   -- trailing % — CAN use an index (with a caveat below)
LIKE '%abc'   -- leading % — can NEVER use an index (no fixed starting point)
```
**SQLite-specific gotcha:** a trailing-`%` pattern only uses an index if
`PRAGMA case_sensitive_like = ON` is set — without it, SQLite falls
back to a full scan even for prefix-anchored patterns, since it can't
guarantee case-insensitive matching lines up with the index's
case-sensitive sort order.

### General optimization habits
- Avoid `SELECT *` — retrieve only the columns you actually need
- Write selective WHERE clauses to reduce processed data early
- Watch for leading-`%` LIKE patterns — they force full scans
- Re-check `EXPLAIN QUERY PLAN` after schema changes; what was optimal
  can silently stop being so

---

## Quick Reference — Running SQL via Python (sqlite3)

```python
import sqlite3

conn = sqlite3.connect("mydb.db")
cursor = conn.cursor()

query = "SELECT * FROM table_name WHERE condition"
cursor.execute(query)
results = cursor.fetchall()
print(results)

conn.close()
```
