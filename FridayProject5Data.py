import sqlite3

# Connect to the SQLite database file
conn = sqlite3.connect('FridayProj5.db')

# Create a cursor object to execute SQL queries
cursor = conn.cursor()

# Choose the table you want to retrieve values from
table_name = 'QuestAns'

# Construct SQL query to select all columns
query = f"SELECT * FROM {table_name};"

# Execute the query
cursor.execute(query)

# Fetch all rows
rows = cursor.fetchall()

# Print each value for each column
for row in rows:
    print("ID:", row[0])
    print("Question:", row[1])
    print("Answer:", row[2])
    print()  # Add a new line for better readability