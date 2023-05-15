import sqlite3


def create_connection(db_file):
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except sqlite3.Error as ex:
        print(ex)
    return None


def create_employees_table(connection):
    query = """
    CREATE TABLE IF NOT EXISTS Employees (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        email TEXT,
        company_id INTEGER
    )
    """
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
    except sqlite3.Error as ex:
        print(ex)


def insert_employee(connection, name, email, company_id):
    query = """
    INSERT INTO Employees(name, email, company_id)
    VALUES (?, ?, ?)
    """
    try:
        cursor = connection.cursor()
        cursor.execute(query, (name, email, company_id))
        connection.commit()
        return cursor.lastrowid
    except sqlite3.Error as ex:
        print(ex)
        return None


def delete_employee(connection, employee_id):
    query = """
    DELETE FROM Employees
    WHERE id = ?
    """
    try:
        cursor = connection.cursor()
        cursor.execute(query, (employee_id,))
        connection.commit()
    except sqlite3.Error as ex:
        print(ex)


def select_employee(connection, employee_id):
    query = """
    SELECT * FROM Employees
    WHERE id = ?
    """
    try:
        cursor = connection.cursor()
        cursor.execute(query, (employee_id,))
        return cursor.fetchone()
    except sqlite3.Error as ex:
        print(ex)
        return None


def delete_all_employees(connection):
    query = """
    DELETE FROM Employees
    """
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
    except sqlite3.Error as ex:
        print(ex)


# Create a connection to the database
connection = create_connection("predavanje_11_05/employees.db")

# Create the Employees table if it doesn't exist
create_employees_table(connection)

# Insert a new employee
employee_id = insert_employee(connection, "John Doe", "john@example.com", 1)
employee_id_2 = insert_employee(connection, "Jane Doe", "jane@example.com", 2)
print("Inserted employee with ID:", employee_id)

# Select the employee by ID
employee = select_employee(connection, employee_id)
print("Selected employee:", employee)

# Delete the employee by ID
delete_employee(connection, employee_id)
print("Deleted employee with ID:", employee_id)

# Delete all employees
# delete_all_employees(connection)
# print("Deleted all employees")

# Close the connection
connection.close()
