import sqlite3

# 1.Connect to your database using the connect() method of the sqlite3 module. You can pass the path to your database file as an argument to the connect() method:
conn = sqlite3.connect("predavanje_08_05-baze-podataka/database.db")
# 2.Once you have a connection to your database, you can create a cursor object using the cursor() method of the connection object:
cursor = conn.cursor()
# 3.Use the execute() method of the cursor object to execute SQL statements. For example, you can create a table in your database like this:
query = "INSERT INTO books (title,author,year) VALUES (?,?,?)"
values = [
    ("Random knjiga 1", "Random autor 1", 2003),
    ("Random knjiga 2", "Random autor 2", 1996),
    ("Random knjiga 3", "Random autor 3", 1999),
]
cursor.executemany(query, values)

# 4.You can use the commit() method of the connection object to save changes to the database:
conn.commit()
# 5.You can use the fetchall() method of the cursor object to retrieve data from the database:
cursor.execute("SELECT * FROM books")
rows = cursor.fetchall()
for row in rows:
    print(row)
