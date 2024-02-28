import sqlite3 as sql
conn=sql.connect('FridayProj5.db')

cr=conn.cursor()
query = "SELECT name FROM sqlite_master WHERE type='table';"

# Execute the query
cr.execute(query)

# Fetch all table names
table_names = cr.fetchall()

# Print the table names
print("Table Names:")
for name in table_names:
    print(name[0])