"""
CHECKPOINT TEST — Days 21-24
Covers: SQL Fundamentals (21), SQL Joins (22), Window Functions & CTEs (23),
        Query Optimization & Indexes (24)

RULES:
- No looking at your notes for Part A (conceptual questions) -- answer from memory.
- You MAY use your notes/previous task files for Part B (code) if truly stuck,
  but try from memory first.
- Write all answers directly in this file, in the spaces provided.
- This is a checkpoint, not a graded exam -- the point is to reveal what
  needs review before continuing further into Phase 3.

SETUP:
- No installation needed -- sqlite3 is part of Python's standard library.
"""

import sqlite3

# =============================================================
# PART A — CONCEPTUAL (answer in comments, no code needed)
# =============================================================

# A1. What is the SQL query execution order (the order clauses are
#     actually EXECUTED in, not the order they're written)?
# -> 


# A2. Why must you use HAVING instead of WHERE to filter on an
#     aggregate result like AVG(salary)?
# -> 


# A3. What's the difference between INNER JOIN and LEFT JOIN? What
#     happens to unmatched rows in each?
# -> 


# A4. SQLite doesn't natively support RIGHT JOIN. How can you achieve
#     the same result using LEFT JOIN instead?
# -> 


# A5. Why is a table alias REQUIRED for a SELF JOIN, but not for a
#     normal join between two different tables?
# -> 


# A6. What's the key difference between RANK() and DENSE_RANK() when
#     there's a tie? Give a small example.
# -> 


# A7. Why can't you write "WHERE ROW_NUMBER() OVER (...) = 1" directly
#     in a query? What do you need to use instead?
# -> 


# A8. What does an index actually do, and what's the tradeoff of
#     adding one?
# -> 


# A9. You have a composite index on (city, name). Would a query
#     filtering only by "name" be able to use this index? Why or why not?
# -> 


# A10. In EXPLAIN QUERY PLAN output, what's the difference between
#      seeing "SCAN table_name" and "SEARCH table_name USING INDEX..."?
# -> 


# =============================================================
# PART B — MINI PROJECT (end-to-end, mixing everything)
# =============================================================

# You're analyzing data for a small bookstore. Two tables are set up
# for you below -- do not modify the setup.

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


# B1. Write a query to find the total quantity sold PER GENRE (join
#     books and sales, group by genre, order by total quantity
#     descending).

# --- your code here ---




# B2. Write a query using LEFT JOIN to list every book's title
#     alongside its total quantity sold -- including books that have
#     NEVER been sold (their total should show as None or 0).

# --- your code here ---




# B3. Using a window function, rank books within each genre by price
#     (highest first). Show title, genre, price, and the rank.

# --- your code here ---




# B4. Using a CTE (or subquery), find only the TOP 1 highest-priced
#     book PER GENRE.

# --- your code here ---




# B5. Run EXPLAIN QUERY PLAN on this query:
#     SELECT * FROM books WHERE genre = 'Fiction'
#     Then create an index on the genre column, and run the EXACT
#     SAME EXPLAIN QUERY PLAN again. Print both results.

# --- your code here ---




conn.close()
