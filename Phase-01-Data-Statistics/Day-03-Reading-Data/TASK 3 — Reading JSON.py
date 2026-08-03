import pandas as pd

# 3a. Read "people.json" into a DataFrame called df_json
df_json = pd.read_json(r"A:\Ai-Engineer\Day-03-Reading-Data\people.json")

# 3b. Print df_json
print(df_json)

# 3c. Print only the rows where Age > 26
print(df_json[df_json["Age"]>26])