"""
CHECKPOINT TEST — Days 21-24 — ANSWER SHEET
Covers: SQL Fundamentals (21), SQL Joins (22), Window Functions & CTEs (23),
        Query Optimization & Indexes (24)
"""

import sqlite3

# =============================================================
# PART A — CONCEPTUAL ANSWERS
# =============================================================

# A1. FROM -> WHERE -> GROUP BY -> HAVING -> SELECT -> ORDER BY

# A2. WHERE is applied BEFORE aggregation happens (before GROUP BY),
#     so an aggregate result like AVG(salary) doesn't exist yet at the
#     point WHERE runs. HAVING runs AFTER aggregation, specifically to
#     filter on aggregate results.

# A3. INNER JOIN returns only rows with a match on BOTH sides --
#     unmatched rows are dropped entirely. LEFT JOIN returns ALL rows
#     from the left table, plus matches from the right; unmatched
#     right-side columns show as NULL.

# A4. RIGHT JOIN is the mirror image of LEFT JOIN. Swap which table is
#     listed first (put the table that would be on the "right" as the
#     left table instead), and use LEFT JOIN -- this achieves the same
#     result.

# A5. A SELF JOIN joins a table to itself, so both sides of the join
#     reference the exact same table. Without an alias, SQL cannot
#     distinguish between the two references to the identical table,
#     making column references ambiguous. A normal join between two
#     DIFFERENT tables doesn't have this problem, since each table name
#     is already unique.

# A6. RANK() gives tied rows the same rank, but the NEXT rank SKIPS
#     numbers. DENSE_RANK() gives tied rows the same rank, but the next
#     rank does NOT skip.
#     Example -- 3 people with scores 100, 100, 90:
#     RANK():       100->1, 100->1, 90->3   (skips 2)
#     DENSE_RANK():  100->1, 100->1, 90->2   (no skip)

# A7. WHERE is applied BEFORE window functions are calculated, so the
#     window function's result (e.g. a row number) doesn't exist yet
#     at the point WHERE would try to use it. Instead, use a CTE or
#     subquery: calculate the window function first, then filter on
#     its result in the OUTER query.

# A8. An index lets the database jump directly to matching rows
#     instead of scanning the whole table, speeding up SELECT queries.
#     The tradeoff: indexes take extra storage space, and slow down
#     INSERT/UPDATE/DELETE operations, since the index itself must be
#     updated whenever the underlying data changes.

# A9. No. A composite index on (city, name) is sorted first by city,
#     then by name WITHIN each city. Filtering by name alone gives the
#     database no starting point to jump to in the index, since it
#     doesn't know which city group to look inside first -- this forces
#     a full table scan instead.

# A10. "SCAN table_name" means the database is checking every row in
#      the table (a full table scan) -- often a sign of a missing or
#      unused index. "SEARCH table_name USING INDEX ..." means the
#      database found and used an index to jump directly to matching
#      rows, without checking every row.


# =============================================================
# PART B — MINI PROJECT ANSWERS
# =============================================================

conn = sqlite3.connect("bookstore.db")
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS books")
cursor.execute("DROP TABLE IF EXISTS sales")

cursor.execute("""
    CREATE TABLE books (
        id INTEGER PRIMARY KEY,
        title TEXT,
        genre TEXT,
        price INTEGER
    )
""")
cursor.execute("""
    CREATE TABLE sales (
        id INTEGER PRIMARY KEY,
        book_id INTEGER,
        quantity INTEGER,
        sale_month TEXT
    )
""")

books_data = [
    (1, "Python Basics", "Tech", 500),
    (2, "The Silent Forest", "Fiction", 300),
    (3, "Data Science 101", "Tech", 650),
    (4, "Mystery at Midnight", "Fiction", 350),
    (5, "Cooking Made Easy", "Lifestyle", 400),
    (6, "The Lost Kingdom", "Fiction", 320),   # never sold
]
sales_data = [
    (1, 1, 10, "2026-01"),
    (2, 2, 15, "2026-01"),
    (3, 3, 8, "2026-01"),
    (4, 4, 12, "2026-01"),
    (5, 1, 14, "2026-02"),
    (6, 2, 9, "2026-02"),
    (7, 3, 11, "2026-02"),
    (8, 5, 6, "2026-02"),
]
cursor.executemany("INSERT INTO books VALUES (?, ?, ?, ?)", books_data)
cursor.executemany("INSERT INTO sales VALUES (?, ?, ?, ?)", sales_data)
conn.commit()


# B1. Total quantity sold per genre
query_b1 = """
    SELECT b.genre, SUM(s.quantity) AS total_quantity_sold
    FROM books b
    JOIN sales s ON b.id = s.book_id
    GROUP BY b.genre
    ORDER BY total_quantity_sold DESC
"""
cursor.execute(query_b1)
print("B1:", cursor.fetchall())
# Expected: [('Tech', 43), ('Fiction', 36), ('Lifestyle', 6)]


# B2. Every book's title + total quantity sold, including never-sold books
query_b2 = """
    SELECT b.title, SUM(s.quantity) AS total_quantity_sold
    FROM books b
    LEFT JOIN sales s ON b.id = s.book_id
    GROUP BY b.title
"""
cursor.execute(query_b2)
print("B2:", cursor.fetchall())
# Expected: 'The Lost Kingdom' shows None (never sold), all others show
# their correct summed totals


# B3. Rank books within each genre by price, highest first
query_b3 = """
    SELECT title, genre, price,
           RANK() OVER (PARTITION BY genre ORDER BY price DESC) AS price_rank
    FROM books
"""
cursor.execute(query_b3)
print("B3:", cursor.fetchall())
# Expected: each genre's books ranked independently by price, starting
# at 1 within each genre


# B4. Top 1 highest-priced book per genre (using a subquery)
query_b4 = """
    SELECT genre, title, price FROM (
        SELECT genre, title, price,
               RANK() OVER (PARTITION BY genre ORDER BY price DESC) AS price_rank
        FROM books
    )
    WHERE price_rank = 1
"""
cursor.execute(query_b4)
print("B4:", cursor.fetchall())
# Expected: [('Fiction', 'Mystery at Midnight', 350),
#            ('Lifestyle', 'Cooking Made Easy', 400),
#            ('Tech', 'Data Science 101', 650)]


# B5. EXPLAIN QUERY PLAN before and after an index
query_b5 = "EXPLAIN QUERY PLAN SELECT * FROM books WHERE genre = 'Fiction'"

cursor.execute(query_b5)
print("B5 before index:", cursor.fetchall())
# Expected: SCAN books -- full table scan (exact cost numbers may vary)

cursor.execute("CREATE INDEX idx_genre ON books(genre)")

cursor.execute(query_b5)
print("B5 after index:", cursor.fetchall())
# Expected: SEARCH books USING INDEX idx_genre (genre=?)

conn.close()
