# Day 21 — SQL Fundamentals: SELECT, WHERE, ORDER BY, GROUP BY, HAVING — Notes

Topics covered: SELECT, WHERE, ORDER BY, GROUP BY, HAVING; running SQL
via Python's sqlite3 module; query execution order

---

## 1. SELECT — Choosing Columns

```sql
SELECT column1, column2 FROM table_name;
```

Retrieves specific columns from a table. `FROM` must be present in
every SELECT query — it specifies which table to pull from.

```sql
SELECT * FROM employees;              -- all columns
SELECT name, salary FROM employees;   -- specific columns only
```

---

## 2. WHERE — Filtering Rows

```sql
SELECT * FROM employees WHERE department = 'Sales';
```

Filters individual rows based on a condition — only matching rows are
returned. Works with `=`, `>`, `<`, `>=`, `<=`, `!=`, `AND`, `OR`.

**Worked example (Task 1):** selecting name and salary for Engineering
employees.
```python
query = "SELECT name, salary FROM employees WHERE department = 'Engineering'"
cursor.execute(query)
results = cursor.fetchall()
# [('Aman', 78000), ('Vikram', 85000), ('Karan', 91000), ('Divya', 72000)]
```

---

## 3. ORDER BY — Sorting Results

```sql
SELECT * FROM employees ORDER BY salary DESC;
```

Sorts the final output. Default is ascending (`ASC`, low to high) unless
`DESC` (high to low) is specified.

**Worked example (Task 2):** employees with salary > 55000, sorted
highest to lowest.
```python
query = "SELECT * FROM employees WHERE salary > 55000 ORDER BY salary desc"
# Returns 6 employees, correctly ordered: 91000, 85000, 78000, 72000, 61000, 58000
```

---

## 4. GROUP BY — Grouping for Aggregation

```sql
SELECT department, AVG(salary) FROM employees GROUP BY department;
```

Groups rows sharing the same value into summary rows — almost always
paired with an aggregate function (`COUNT()`, `SUM()`, `AVG()`,
`MAX()`, `MIN()`). This is the SQL equivalent of Day 8's Pandas
`groupby()` — same underlying concept, different syntax.

**Worked example (Task 3):** average salary per department.
```python
query = "SELECT department, AVG(salary) FROM employees GROUP BY department"
# [('Engineering', 81500.0), ('Marketing', 49666.67), ('Sales', 57000.0)]
```

---

## 5. HAVING — Filtering Groups After Aggregation

```sql
SELECT department, AVG(salary) FROM employees
GROUP BY department
HAVING AVG(salary) > 50000;
```

**The key distinction from WHERE:** WHERE filters individual rows
BEFORE grouping happens. HAVING filters GROUPS AFTER aggregation. You
cannot use WHERE to filter on an aggregate result like `AVG(salary)`,
because at the point WHERE runs, that average hasn't been calculated
yet — HAVING exists specifically to filter on aggregated values.

**Worked example (Task 4):** departments with average salary > 60000.
```python
query = "SELECT department, AVG(salary) FROM employees GROUP BY department HAVING AVG(salary) > 60000"
# [('Engineering', 81500.0)]  -- only Engineering qualifies
```

---

## 6. Query Execution Order

SQL clauses are WRITTEN in one order, but EXECUTED in a different order:

```
1. FROM       -- pick the table
2. WHERE      -- filter individual rows
3. GROUP BY   -- group the remaining rows
4. HAVING     -- filter the groups
5. SELECT     -- choose which columns to show
6. ORDER BY   -- sort the final result
```

This execution order is exactly WHY HAVING can filter on aggregates and
WHERE can't — by the time HAVING runs, GROUP BY has already completed
and the aggregate values exist.

---

## 7. Running SQL via Python — The Standard Pattern

Reused identically across all 5 tasks:

```python
query = "SELECT ... FROM ... WHERE ... GROUP BY ... HAVING ... ORDER BY ..."
cursor.execute(query)          # sends the query to the database
results = cursor.fetchall()    # retrieves all matching rows
print(results)                 # displays them
```

A common early mistake: writing raw SQL directly as Python code (e.g.
`SELECT * FROM employees WHERE...` with no quotes) — Python does not
parse SQL syntax natively. The query must always be a STRING passed
into `cursor.execute()`.

---

## 8. Worked Example — Combining All 5 Clauses (Task 5)

The hardest task: combine WHERE, GROUP BY, COUNT, HAVING, and ORDER BY
in a single query.

**Requirements:**
- Only employees with `years_experience >= 3` (WHERE)
- Grouped by department (GROUP BY)
- Count employees per department (COUNT)
- Only departments with 2+ such employees (HAVING)
- Ordered by count, highest first (ORDER BY)

```python
query = """
    SELECT department, COUNT(*)
    FROM employees
    WHERE years_experience >= 3
    GROUP BY department
    HAVING COUNT(*) >= 2
    ORDER BY COUNT(*) DESC
"""
# [('Engineering', 4), ('Sales', 3)]
```

**Key lesson from building this piece by piece:** when a clause needs
to reference "the count" (in HAVING or ORDER BY), you must write the
actual `COUNT(*)` expression again — you can't invent a placeholder
name like `result` or reference the grouped column itself (`departments`)
as if it represented the count. SQL has no automatic variable to refer
back to a SELECT-ed aggregate by name in HAVING/ORDER BY unless using
a column alias (a more advanced pattern for a later day).

---

## Mistakes I Made & Fixed Today

- Wrote raw SQL directly as Python code without wrapping it in a
  string — caused a syntax error, since Python doesn't parse SQL syntax
  natively. Fixed by assigning the query to a string variable first.
- In Task 2, merged the WHERE condition into the ORDER BY clause
  (`ORDER BY salary desc < 55000`) instead of using separate clauses,
  and had the comparison direction backwards. Rebuilt with WHERE and
  ORDER BY as distinct clauses in the correct order.
- In Task 4, two typos broke the query: `GROPU BY` (should be
  `GROUP BY`) and `> 6000` instead of `> 60000` — a missing zero that
  would have drastically changed which departments passed the filter.
- In Task 5, built the query incrementally through several broken
  states: missing `SELECT`/`COUNT(*)` entirely at first, then using
  invalid placeholder references (`departments`, `result`) in
  HAVING/ORDER BY instead of the real `COUNT(*)` expression, and having
  the HAVING comparison direction backwards. Fixed one piece at a time
  until the full query correctly combined all 5 required clauses.
- Noticed `employees.db` was being created at the repo root rather than
  inside the Day 21 folder, caused by VS Code executing scripts from the
  workspace root directory. Resolved by NOT tracking the file in Git at
  all (added to `.gitignore`), since every task file fully regenerates
  the database's contents on every run (DROP + CREATE + INSERT) —
  unlike Day 3's `store.db`, which held static input data worth keeping.

---

## Resources Used

- "LIVE SQL Hindi Tutorial – Master SELECT, WHERE, ORDER BY with Real
  Use Case" — https://www.youtube.com/watch?v=tQnDvQmFZNM
- "MySQL #33: GROUP BY & ORDER BY in SQL in Hindi" —
  https://www.youtube.com/watch?v=6j7XB62eHYA