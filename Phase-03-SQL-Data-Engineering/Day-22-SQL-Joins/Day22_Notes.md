# Day 22 — SQL Joins Deep Dive — Notes

Topics covered: INNER JOIN; LEFT JOIN; RIGHT JOIN (simulated); FULL JOIN
(concept); SELF JOIN; multi-table joins combined with GROUP BY/ORDER BY

---

## 1. The Core Idea

Joins combine data from two or more tables based on a shared column —
essential since real databases split data across multiple tables
(e.g. an `employees` table and a separate `departments` table) rather
than storing everything in one giant table.

---

## 2. INNER JOIN

Returns only rows with a match between the columns in both tables.
Rows without a match on either side are excluded entirely.

```sql
SELECT employees.name, departments.department_name
FROM employees
INNER JOIN departments ON employees.department_id = departments.id;
```

**Worked example (Task 1):**
```python
query = """SELECT employees.name, departments.department_name
           FROM employees
           INNER JOIN departments ON employees.department_id = departments.id"""
# 6 rows returned -- Neha is missing, since she has no department_id
```

**Key lesson:** predicted 5 rows before running it, but the actual
count was 6 — a reminder to verify against real output rather than
estimate from memory.

---

## 3. LEFT JOIN (LEFT OUTER JOIN)

Returns ALL rows from the left table, plus matching rows from the
right. Unmatched right-side columns come back as `NULL` (`None` in
Python).

```sql
SELECT e.name, d.department_name
FROM employees e
LEFT JOIN departments d ON e.department_id = d.id;
```

**Worked example (Task 2):**
```python
query = """SELECT employees.name, departments.department_name
           FROM employees
           LEFT JOIN departments ON employees.department_id = departments.id"""
# All 7 employees appear; Neha shows None for department_name
```

Because LEFT JOIN keeps every row from the left table regardless of a
match, Neha (no department) is preserved here — where INNER JOIN would
have silently dropped her.

---

## 4. RIGHT JOIN — Simulated in SQLite

**Important limitation:** SQLite doesn't reliably support RIGHT JOIN
natively. Since RIGHT JOIN is just the mirror of LEFT JOIN, it can
always be simulated by swapping which table is listed first.

```sql
-- "RIGHT JOIN employees ON departments" is equivalent to:
SELECT departments.department_name, employees.name
FROM departments
LEFT JOIN employees ON departments.id = employees.department_id;
```

**Worked example (Task 3):**
```python
query = """SELECT departments.department_name, employees.name
           FROM departments
           LEFT JOIN employees ON departments.id = employees.department_id"""
# All 4 departments appear; "HR" shows None for employee name
```

By putting `departments` on the left, every department is preserved —
including "HR," which has zero employees assigned — achieving the same
practical result as a RIGHT JOIN would, without needing SQLite to
support it directly.

---

## 5. FULL JOIN (FULL OUTER JOIN) — Concept

Returns everything from both tables, matched where possible, `NULL`
where not. Also not natively supported in SQLite (or MySQL up to
version 8) — would require combining a LEFT JOIN and a RIGHT/swapped-
LEFT JOIN using `UNION`:

```sql
SELECT * FROM employees e LEFT JOIN departments d ON e.department_id = d.id
UNION
SELECT * FROM departments d LEFT JOIN employees e ON d.id = e.department_id;
```

Understood conceptually this session; the practice focused on the more
commonly-needed INNER/LEFT/RIGHT patterns.

---

## 6. SELF JOIN

A table joined to itself — used for hierarchical data, like employees
referencing their own manager (also an employee) via `manager_id`.

```sql
SELECT e1.name AS employee, e2.name AS manager
FROM employees e1
LEFT JOIN employees e2 ON e1.manager_id = e2.id;
```

**Worked example (Task 4):**
```python
query = """SELECT e1.name AS employee_name, e2.name AS manager_name
           FROM employees e1
           LEFT JOIN employees e2 ON e1.manager_id = e2.id"""
# [('Aman', None), ('Riya', 'Sara'), ('Vikram', 'Aman'), ('Sara', None),
#  ('Karan', 'Aman'), ('Neha', None), ('Priya', None)]
```

**Why aliases are REQUIRED here (not just helpful):** without aliases,
if `employees.name` were referenced twice in the SELECT (once for the
employee, once for the manager), SQL couldn't tell which instance of
the identical table each reference points to — the alias (`e1`, `e2`)
disambiguates "this occurrence of the table" from "that occurrence."

---

## 7. Multi-Table Joins + GROUP BY/ORDER BY

To join `n` tables requires `n-1` JOIN statements. Joins also combine
naturally with Day 21's GROUP BY and ORDER BY — join first, then
aggregate the joined result.

```sql
SELECT a.col, b.col, c.col
FROM table_a a
JOIN table_b b ON a.id = b.a_id
JOIN table_c c ON b.id = c.b_id;
```

**Worked example (Task 5):** average salary per department, joining
employees and departments.
```python
query = """SELECT departments.department_name, AVG(employees.salary) AS average_salary
           FROM employees
           INNER JOIN departments ON employees.department_id = departments.id
           GROUP BY departments.department_name
           ORDER BY average_salary DESC"""
# [('Engineering', 84666.67), ('Sales', 56500.0), ('Marketing', 53000.0)]
```

**Why "HR" doesn't appear:** INNER JOIN drops any row without a match
on both sides. Since no employee has `department_id = 4` (HR's id), no
row survives the join for HR — even though HR still exists in the
`departments` table itself, it never enters the joined/grouped result.

---

## Mistakes I Made & Fixed Today

- Predicted Task 1's INNER JOIN would return 5 rows, but the actual
  output had 6 — miscounted before checking the real result. Fixed by
  recounting the printed tuples directly rather than trusting the
  initial estimate.
- Minor typo in a written comment ("emloyee" instead of "employee") —
  a typing slip, not a conceptual misunderstanding.
- Initial explanation for why SELF JOIN needs an alias was accurate but
  too general ("joining the same table to itself") without explaining
  the actual mechanism. Refined to state precisely: without an alias,
  SQL cannot distinguish between two references to the identical table,
  making column references ambiguous.

---

## Resources Used

- "SQL Joins in Hindi | INNER, LEFT, RIGHT, FULL Join Explained" —
  https://www.thevistaacademy.com/sql-joins-in-hindi-inner-left-right-full-join/