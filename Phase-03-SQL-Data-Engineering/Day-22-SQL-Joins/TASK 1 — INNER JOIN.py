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


# 1a. Write a query that joins employees and departments, showing
#     employee name and department_name -- ONLY for employees who
#     actually have a matching department.
#     (hint: use INNER JOIN ... ON employees.department_id = departments.id)
query = "SELECT employees.name, departments.department_name FROM employees INNER JOIN departments ON employees.department_id = departments.id"

# 1b. Execute, fetch, and print.
cursor.execute(query)

results = cursor.fetchall()

print(results)

conn.close()

# 1c. In a comment: how many rows do you expect? Which employee(s)
#     will be MISSING from the result, and why?
# -> I expect 6 rows in the result.
# -> The employee "Neha" will be missing from the result because she does not have a department assigned.