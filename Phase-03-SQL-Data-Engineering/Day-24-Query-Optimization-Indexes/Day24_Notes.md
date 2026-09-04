# Day 24 — Advanced SQL: Query Optimization, Indexes, EXPLAIN Plans — Notes

Topics covered: indexes; the read/write tradeoff; composite indexes;
EXPLAIN QUERY PLAN; LIKE patterns and index usage; SELECT * vs specific
columns

---

## 1. What Are Indexes?

Indexes help the database find data faster without scanning the whole
table — like a book's table of contents lets you jump straight to what
you need instead of flipping through every page.

```sql
CREATE INDEX idx_customer_name ON customers (customer_name);
```

- **Primary Index** — automatically created on the primary key
- **Secondary Index** — created manually on non-primary-key columns to
  speed up queries on those specific columns

---

## 2. The Tradeoff — Indexes Aren't Free

Indexes speed up READS (SELECT) but slow down WRITES (INSERT/UPDATE/
DELETE), since the index must be updated every time the underlying data
changes. This is why you don't index every column — only ones
frequently used in WHERE, JOIN, or ORDER BY clauses.

---

## 3. Worked Example — Index Before/After (Task 1)

```python
query_1a = "SELECT * FROM customers WHERE email = 'user500@test.com'"

# BEFORE any index:
cursor.execute("EXPLAIN QUERY PLAN " + query_1a)
# [(2, 0, 216, 'SCAN customers')]

# Create the index:
cursor.execute("CREATE INDEX idx_email ON customers(email)")

# Re-run the SAME query AFTER the index exists:
cursor.execute("EXPLAIN QUERY PLAN " + query_1a)
# [(3, 0, 62, 'SEARCH customers USING INDEX idx_email (email=?)')]
```

**SCAN** = full table scan, checking every row. **SEARCH ... USING
INDEX** = the database found and used the index to jump directly to
matching rows, without checking every row.

**Bug caught:** initially created the index but forgot to re-run the
EXPLAIN query afterward — `CREATE INDEX` itself returns no rows, so
`fetchall()` on it produced an empty list. Needed a separate,
deliberate second `cursor.execute()` call re-running the exact same
EXPLAIN QUERY PLAN string to see the "after" state.

---

## 4. Composite Indexes — Order Matters (Task 2)

An index built on multiple columns only works LEFT TO RIGHT.

```python
cursor.execute("CREATE INDEX idx_city_name ON customers(city, name)")

# Filtering by city (the LEFTMOST column):
cursor.execute("EXPLAIN QUERY PLAN SELECT * FROM customers WHERE city = 'Delhi'")
# [(3, 0, 62, 'SEARCH customers USING INDEX idx_city_name (city=?)')]

# Filtering by name (NOT the leftmost column):
cursor.execute("EXPLAIN QUERY PLAN SELECT * FROM customers WHERE name = 'Customer500'")
# [(2, 0, 216, 'SCAN customers')]
```

**Why order matters:** a composite index on `(city, name)` is sorted
first by city, then by name WITHIN each city. This speeds up queries
filtering by `city` alone, or by `city` AND `name` together — but NOT
`name` alone, since there's no way to jump directly to a specific name
without first knowing which city group to look inside.

---

## 5. LIKE Patterns and Index Usage — A Genuine SQLite Gotcha (Task 3)

**The general rule most tutorials state:** a trailing-`%` pattern
(`'Customer5%'`) CAN use an index; a leading-`%` pattern (`'%50'`)
CANNOT, since the database can't "jump to a starting point" in a
sorted index without knowing what the string begins with.

**The non-obvious detail, discovered through direct testing:** in
SQLite, the trailing-`%` optimization only activates if
`PRAGMA case_sensitive_like = ON` is set first.

```python
cursor.execute("CREATE INDEX idx_name ON customers(name)")
cursor.execute("PRAGMA case_sensitive_like = ON")

# Trailing % (Customer5%):
cursor.execute("EXPLAIN QUERY PLAN SELECT * FROM customers WHERE name LIKE 'Customer5%'")
# [(3, 0, 164, 'SEARCH customers USING INDEX idx_name (name>? AND name<?)')]

# Leading % (%50):
cursor.execute("EXPLAIN QUERY PLAN SELECT * FROM customers WHERE name LIKE '%50'")
# [(2, 0, 216, 'SCAN customers')]
```

**Why the pragma is needed:** SQLite's default LIKE is case-INsensitive
for ASCII, but a standard index is sorted case-SENSITIVELY. Without
`case_sensitive_like` turned on, SQLite can't guarantee that a
case-insensitive prefix match lines up cleanly with the case-sensitive
index order, so it plays it safe and falls back to a full scan — even
for a pattern that starts with fixed characters. Confirmed this
directly: without the pragma, even `'Customer5%'` fell back to `SCAN`;
with it enabled, the same query correctly used the index.

**Why leading `%` NEVER uses an index, pragma or not:** the search term
can appear anywhere in the string, so the database has no fixed
starting point to jump to in the sorted index — it must check every row
regardless.

---

## 6. SELECT * vs Specific Columns (Task 4)

```python
query_4a = "SELECT * FROM customers WHERE city = 'Delhi'"      # 333 rows
query_4b = "SELECT name FROM customers WHERE city = 'Delhi'"   # 333 rows
```

Both return the identical ROW COUNT (333) for the same filter — the
difference is in the amount of DATA retrieved per row. `SELECT *`
pulls all 4 columns (id, name, email, city) for every matching row;
`SELECT name` pulls just 1. This gap becomes significantly more
important on tables with many more columns (e.g. 50 instead of 4) or
many more rows (millions instead of thousands) — unnecessary data
transfer and processing adds up fast at scale.

---

## 7. Reading EXPLAIN on a JOIN Query (Task 5)

Joining `customers` and `orders`, filtering by `customers.city`, EXPLAIN
QUERY PLAN shows a separate line per table involved — revealing whether
EACH side of the join is doing a SCAN or using an index, both before
and after indexing the join column (`orders.customer_id`). Adding the
index changed the `orders` side of the plan from a scan to an indexed
search, while `customers` continued using its own city-based access
path.

---

## Mistakes I Made & Fixed Today

- In Task 1, created the index but forgot to re-execute the EXPLAIN
  QUERY PLAN query afterward — printed an empty result since
  `CREATE INDEX` returns no rows. Fixed by adding a distinct, deliberate
  second `cursor.execute()` call for the "after" state.
- Minor recurring typos in written comments ("diffrence," "specifies"
  instead of "specified," "retrives") — typing speed issues, not
  conceptual errors.
- Initially explained WHAT happened in the LIKE pattern task (which
  query used the index) without fully explaining WHY a leading %
  specifically breaks index usage — extended the reasoning to connect
  it back to how a sorted index physically works (no fixed starting
  point to jump to when the beginning of the string is unknown).

---

## Resources Used

- "Mastering MySQL Query Performance: An In Depth Analysis and Index
  Tuning Guide" — https://www.youtube.com/watch?v=7ygH7DYO7yw
- "SQL indexing best practices | How to make your database FASTER!" —
  https://www.youtube.com/watch?v=BIlFTFrEFOI