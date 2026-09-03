# Day 23 — Window Functions & CTEs/Subqueries — Notes

Topics covered: ROW_NUMBER; RANK vs DENSE_RANK; LAG; running totals;
CTEs and subqueries for filtering window function results

---

## 1. What a Window Function Does

Unlike `GROUP BY`, which COLLAPSES rows into one summary row per group,
a window function performs a calculation across a set of related rows
WHILE KEEPING EVERY ROW INTACT. Every window function uses an `OVER()`
clause to define the "window" — the set of rows the calculation
applies to.

---

## 2. The OVER Clause

```sql
SOME_FUNCTION() OVER (PARTITION BY column ORDER BY column)
```

- `PARTITION BY` — splits rows into independent groups, similar to
  GROUP BY, but WITHOUT collapsing rows into summaries
- `ORDER BY` (inside OVER) — controls the processing order, which
  matters for ranking and running totals

---

## 3. ROW_NUMBER — Unique Sequential Numbering

Assigns a unique sequential number to each row within a window — never
any ties.

**Worked example (Task 1):**
```python
query = """SELECT salesperson, region, amount,
           ROW_NUMBER() OVER (PARTITION BY region ORDER BY amount DESC) AS rn
           FROM sales"""
# North: rn resets 1-5. South: rn resets 1-5 (independently).
```

**Why PARTITION BY matters:** without it, row numbers would continue
counting across the ENTIRE result set instead of resetting per region
— the numbering would no longer represent "position within this
specific group."

---

## 4. RANK vs DENSE_RANK — Handling Ties

- **RANK()** — ties get the same rank, but the next rank SKIPS numbers
  (e.g. 1, 1, 3, 4)
- **DENSE_RANK()** — ties get the same rank, but the next rank does
  NOT skip (e.g. 1, 1, 2, 3)

**Worked example (Task 2)** — Riya and Vikram tied at 7000 in North/
January:
```python
query = """SELECT salesperson, amount,
           RANK() OVER (ORDER BY amount DESC) AS rank,
           DENSE_RANK() OVER (ORDER BY amount DESC) AS dense_rank
           FROM sales WHERE region = 'North' AND sale_month = '2026-01'
           ORDER BY amount DESC"""
# [('Riya', 7000, 1, 1), ('Vikram', 7000, 1, 1), ('Aman', 5000, 3, 2)]
```

After the tie at rank 1, RANK() jumps to 3 for the next person (Aman),
while DENSE_RANK() gives him 2 — confirming the skip-vs-no-skip
distinction directly on real tied data.

---

## 5. LAG — Comparing Rows to Previous Rows

`LAG(column, offset)` pulls a value from a PREVIOUS row within the
window (default offset = 1). Returns `NULL` when no such row exists
(e.g. the very first row in an ordered sequence has no "previous").

**Worked example (Task 3)** — Aman's sales, comparing to the prior month:
```python
query = """SELECT sale_month, amount,
           LAG(amount, 1) OVER (ORDER BY sale_month) AS prev_amount
           FROM sales WHERE salesperson = 'Aman' ORDER BY sale_month"""
# [('2026-01', 5000, None), ('2026-02', 5500, 5000)]
```

January shows `None` (no earlier month exists for Aman), February
correctly shows 5000 (January's amount) — this is the standard pattern
for month-over-month comparisons without needing a self-join.

---

## 6. Running Totals

Combining a normal aggregate (`SUM`, `AVG`) with `OVER` produces a
cumulative value per row, per group — unlike `GROUP BY`, every row
stays visible.

**Worked example (Task 4):**
```python
query = """SELECT salesperson, sale_month, amount,
           SUM(amount) OVER (PARTITION BY salesperson ORDER BY sale_month) AS running_total
           FROM sales ORDER BY sale_month"""
# Aman: 5000 -> 10500 (5000+5500)
# Karan: 6000 -> 12500 (6000+6500)
```

**Key distinction from GROUP BY:** `GROUP BY` would collapse each
salesperson into ONE total row, losing the month-by-month progression
entirely. The window function preserves every row while still
accumulating the running sum.

---

## 7. Critical Gotcha — Window Functions Run AFTER WHERE

Window functions are evaluated AFTER `WHERE` in SQL's execution order
(same concept underlying Day 21's HAVING vs WHERE distinction). This
means you CANNOT filter directly on a window function's result using
`WHERE` in the same query — it would either error or fail to work as
intended.

**The fix:** wrap the window function in a CTE or subquery, then
filter in the OUTER query, where the window function's result already
exists as a normal column.

---

## 8. CTEs and Subqueries — Solving "Top N Per Group"

**CTE syntax:**
```sql
WITH ranked_employees AS (
    SELECT name, department, salary,
           RANK() OVER (PARTITION BY department ORDER BY salary DESC) AS rnk
    FROM employees
)
SELECT * FROM ranked_employees WHERE rnk <= 2;
```

**Subquery syntax (functionally equivalent):**
```sql
SELECT * FROM (
    SELECT name, department, salary,
           RANK() OVER (PARTITION BY department ORDER BY salary DESC) AS rnk
    FROM employees
) t
WHERE rnk <= 2;
```

**Worked example (Task 5)** — top 2 sales per region:
```python
query = """SELECT salesperson, region, amount, rank FROM
           (SELECT salesperson, region, amount,
            RANK() OVER (PARTITION BY region ORDER BY amount DESC) AS rank
            FROM sales) AS ranked_sales
           WHERE rank <= 2 ORDER BY region, rank"""
# North: Riya (rank 1), Riya/Vikram tied (rank 2 -- both included)
# South: Karan (rank 1), Karan (rank 2)
```

Used the subquery form here rather than `WITH ... AS`, which the task
explicitly allowed ("CTE or subquery") — both achieve the identical
result; CTEs are generally preferred for readability on more complex,
multi-step queries.

**What would happen without a CTE/subquery:** writing
`WHERE RANK() OVER (...) <= 2` directly in the same query as the
window function itself would fail, since WHERE executes before window
functions are calculated — there's nothing yet to filter on at that
point in execution.

---

## Mistakes I Made & Fixed Today

- No functional bugs this session — all 5 tasks were correct on the
  first working attempt. Only minor typos appeared in written
  explanations (e.g. "diffrence," "bacause") that didn't affect the
  underlying correctness of the reasoning.
- Used a subquery instead of a CTE (`WITH ... AS`) for the "top N per
  group" task — fully valid and explicitly allowed by the task, but
  worth deliberately practicing the CTE syntax specifically, since it
  tends to read more clearly for multi-step logic in real interview
  and production settings.

---

## Resources Used

- "Window Functions in SQL Full Tutorial 🔥 | ROW_NUMBER, RANK, LAG,
  LEAD Explained" — https://www.youtube.com/watch?v=MnDqhGAcRug