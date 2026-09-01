import sqlite3

# =============================================================
# SETUP — creates two sample tables. Do not modify this part.
# =============================================================
conn = sqlite3.connect("company.db")
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS employees")
cursor.execute("DROP TABLE IF EXISTS departments")

cursor.execute("""
    CREATE TABLE departments (
        id INTEGER PRIMARY KEY,
        department_name TEXT
    )
""")
cursor.execute("""
    CREATE TABLE employees (
        id INTEGER PRIMARY KEY,
        name TEXT,
        department_id INTEGER,
        salary INTEGER,
        manager_id INTEGER
    )
""")

departments_data = [
    (1, "Engineering"),
    (2, "Sales"),
    (3, "Marketing"),
    (4, "HR"),          # no employees assigned to this department
]

employees_data = [
    (1, "Aman", 1, 78000, None),
    (2, "Riya", 2, 52000, 4),
    (3, "Vikram", 1, 85000, 1),
    (4, "Sara", 2, 61000, None),
    (5, "Karan", 1, 91000, 1),
    (6, "Neha", None, 47000, None),   # no department assigned
    (7, "Priya", 3, 53000, None),
]

cursor.executemany("INSERT INTO departments VALUES (?, ?)", departments_data)
cursor.executemany("INSERT INTO employees VALUES (?, ?, ?, ?, ?)", employees_data)
conn.commit()


# Notice the employees table has a manager_id column, referencing
# another employee's id in the SAME table.
#
# 4a. Write a SELF JOIN that shows each employee's name alongside
#     their manager's name (use table aliases, e.g. e1 and e2).
#     Employees with no manager should show None for manager name.
query = "SELECT e1.name AS employee_name, e2.name AS manager_name FROM employees e1 LEFT JOIN employees e2 ON e1.manager_id = e2.id"

# 4b. Execute, fetch, and print.
cursor.execute(query)

results = cursor.fetchall()

print(results)

conn.close()


# 4c. In a comment: why is an alias REQUIRED here, unlike Tasks 1-3?
# -> An alias is required here because we are joining the same table to itself.
# -> Without aliases, the SQL engine would not be able to distinguish between the two instances of the employees table, leading to ambiguity in the query.