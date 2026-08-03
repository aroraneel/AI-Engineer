# Day 3 — Reading Data From Multiple Sources

**Topics:** CSV, JSON, SQL databases, REST APIs

## What I Learned

- `pd.read_csv("path")` reads a CSV directly into a DataFrame. Common options: `index_col`, `usecols`, `nrows`.
- `df.to_csv("path", index=False)` saves a DataFrame back to CSV — `index=False` avoids an extra unnamed index column in the file.
- `pd.read_json("path")` reads JSON into a DataFrame — works cleanly when the JSON is a list of similar records.
- SQL data: connect first (`sqlite3.connect(...)`), then `pd.read_sql(query, conn)` runs a SQL query and returns a DataFrame. Always close the connection afterward.
- Filtering can happen either in the SQL query itself (`WHERE Revenue > 3000`) or afterward in Pandas (`df[df["Revenue"] > 3000]`) — both are valid, but SQL-side filtering pushes the work to the database.
- REST APIs: `requests.get(url).json()` fetches and parses API data into a Python dict/list, then `pd.DataFrame(data)` converts it to a table.
- APIs often wrap the actual data list inside a key like `"results"` or `"data"` — always check the JSON structure before converting, since `pd.DataFrame()` expects a plain list of records or a dict of columns, not an object wrapping a list.
- Windows file paths need either a raw string (`r"A:\path\to\file"`) or forward slashes / escaped backslashes — plain backslash strings can trigger invalid escape sequence warnings (e.g. `\A`) and unreliable behavior.

## Resources Used

- [Pandas I/O documentation](https://pandas.pydata.org/docs/user_guide/io.html)
- [JSONPlaceholder — free test REST API](https://jsonplaceholder.typicode.com/)

## Mistakes I Made & Fixed

- Divided by `["Units_Sold"]` (a plain list containing a string) instead of `df_csv["Units_Sold"]` (the actual column) — any time you want a column's values, you need `df[...]` around the name, not just the bare string/list.
- Forgot the `r` prefix on a Windows file path in one case, triggering a `SyntaxWarning` for an invalid escape sequence (`\A`) — raw strings (`r"..."`) are needed for Windows paths to avoid backslashes being misread as escape characters.
- Tried to filter SQL results using a Pandas condition where the "column name" was the entire SQL query string — mixed up SQL-side filtering (a new query with `WHERE`) with Pandas-side filtering (`df[df["col"] > value]`); they're two different approaches and shouldn't be combined incorrectly.
- Selected multiple columns using `df[df["name","email"]]` (a tuple inside single brackets) instead of `df[["name","email"]]` (a proper list inside double brackets) — same "double brackets for multiple columns" rule from Day 2, reapplied here.

## Exercises Completed

- [x] Task 1 — Reading a CSV file (full + selected columns)
- [x] Task 2 — Writing a CSV file, then reading it back to confirm
- [x] Task 3 — Reading JSON and filtering rows
- [x] Task 4 — Reading from a SQL database (two queries, SQL-side filtering)
- [x] Task 5 — Reading from a live REST API

## Next Up

Day 4 — Data visualization with Matplotlib: line, bar, scatter, subplot layouts