import sqlite3

# Connect to a new database or open an existing one
conn = sqlite3.connect("predavanje_09_05/mydatabase.db")

# Create a cursor object to interact with the database
cursor = conn.cursor()

# Create the Equipment table
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS Equipment (
        id INTEGER PRIMARY KEY,
        name TEXT,
        serial_number TEXT,
        location TEXT
    )
"""
)

# Create the Employee table with a foreign key to Equipment
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS Employee (
        id INTEGER PRIMARY KEY,
        name TEXT,
        email TEXT,
        equipment_id INTEGER,
        FOREIGN KEY (equipment_id) REFERENCES Equipment(id)
    )
"""
)

# Insert some sample data into the Equipment table
cursor.execute(
    "INSERT INTO Equipment (name, serial_number, location) VALUES (?, ?, ?)",
    ("Laptop", "1234", "Office"),
)
cursor.execute(
    "INSERT INTO Equipment (name, serial_number, location) VALUES (?, ?, ?)",
    ("Phone", "5678", "Home"),
)

# Insert some sample data into the Employee table
cursor.execute(
    "INSERT INTO Employee (name, email, equipment_id) VALUES (?, ?, ?)",
    ("John Doe", "johndoe@example.com", 1),
)
cursor.execute(
    "INSERT INTO Employee (name, email, equipment_id) VALUES (?, ?, ?)",
    ("Jane Smith", "janesmith@example.com", 2),
)

# Commit the changes to the database
conn.commit()

# Close the database connection
cursor.close()
conn.close()
