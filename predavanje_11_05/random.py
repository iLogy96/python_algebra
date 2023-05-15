import sqlite3

# Establish a connection to the database
conn = sqlite3.connect("predavanje_11_05/company_database.db")
cursor = conn.cursor()

# Create the Company table
cursor.execute(
    """CREATE TABLE IF NOT EXISTS Company (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    address TEXT NOT NULL,
                    industry TEXT,
                    annualRevenue INTEGER
                )"""
)

# Create the Employees table
cursor.execute(
    """CREATE TABLE IF NOT EXISTS Employees (
                    id INTEGER,
                    name TEXT,
                    email TEXT,
                    company_id INTEGER,
                    FOREIGN KEY (company_id) REFERENCES Company(id)
                )"""
)

# Sample data for Company table
company_data = [
    (1, "Company A", "Address A", "Industry A", 100000),
    (2, "Company B", "Address B", "Industry B", 200000),
    (3, "Company C", "Address C", "Industry C", 300000),
]

# Insert sample data into the Company table with a duplicate check
for data in company_data:
    try:
        cursor.execute(
            "INSERT INTO Company (id, name, address, industry, annualRevenue) VALUES (?, ?, ?, ?, ?)",
            data,
        )
    except sqlite3.IntegrityError as e:
        print("Skipping row with duplicate ID:", data)


# Sample data for Employees table
employee_data = [
    (1, "John Doe", "john@example.com", 1),
    (2, "Jane Smith", "jane@example.com", 2),
    (3, "Robert Johnson", "robert@example.com", 3),
]

# Insert sample data into the Employees table with a duplicate check
for data in employee_data:
    id = data[0]
    cursor.execute("SELECT 1 FROM Employees WHERE id = ?", (id,))
    existing_row = cursor.fetchone()
    if not existing_row:
        cursor.execute(
            "INSERT INTO Employees (id, name, email,company_id) VALUES (?, ?, ?, ?)",
            data,
        )


# Update existing employees
cursor.execute(
    "UPDATE Employees SET email = 'john.doe@example1.com' WHERE name = 'John Doe'"
)

# Commit the changes and close the connection
conn.commit()
conn.close()
