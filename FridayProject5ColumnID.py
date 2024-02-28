import sqlite3 as sql
conn=sql.connect('FridayProj5.db')

cr=conn.cursor()
# Choose the table you want to retrieve column names from
table_name = 'your_table_name'

# Construct a SQL query to retrieve column names
query = f"PRAGMA table_info(QuestAns);"

# Execute the query
cr.execute(query)

# Fetch all column names
columns = cr.fetchall()

# Extract column names from the result
column_names = [column[1] for column in columns]

# Print the column names
print(f"Column names from table 'QuestAns':")
print(column_names)