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


# A "RIGHT JOIN employees ON departments" would show every department,
# including ones with NO employees (like "HR"). Since RIGHT JOIN isn't
# reliably available in SQLite, simulate it by SWAPPING which table
# is on the LEFT.
#
# 3a. Write a LEFT JOIN starting FROM departments, joined to employees,
#     showing department_name and employee name for every department
#     -- including departments with no employees at all.
query = "SELECT departments.department_name, employees.name FROM departments LEFT JOIN employees ON departments.id = employees.department_id"

# 3b. Execute, fetch, and print.
cursor.execute(query)

results = cursor.fetchall()

print(results)

conn.close()

# 3c. In a comment: which department shows up with None for the
#     employee name, and why?
# -> The department "HR" shows up with None for the employee name because there are no employees assigned to that department.
# -> The LEFT JOIN keeps "HR" in the result because it returns all records from the left table and the matched records from the right table.
# -> Since there are no employees in the "HR" department, the employee name is shown as None.