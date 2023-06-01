import tkinter as tk
import sqlite3

# Connect to the database
conn = sqlite3.connect('vjezba_SQL/user_database.db')
c = conn.cursor()

# Create a users table if it doesn't exist
c.execute('''CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL UNIQUE,
                password TEXT NOT NULL
            )''')

def register():
    username = username_entry.get()
    password = password_entry.get()
    confirm_password = confirm_password_entry.get()

    # Check if the username is already taken
    c.execute("SELECT * FROM users WHERE username=?", (username,))
    existing_user = c.fetchone()

    if existing_user:
        result_label.config(text="Username already exists")
    elif password != confirm_password:
        result_label.config(text="Passwords do not match")
    else:
        # Insert the new user into the database
        c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        result_label.config(text="Registration successful")

def login():
    username = username_entry.get()
    password = password_entry.get()

    # Check if the username and password match
    c.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    existing_user = c.fetchone()

    if existing_user:
        result_label.config(text="Login successful")
    else:
        result_label.config(text="Invalid username or password")

window = tk.Tk()

# Username label and entry
username_label = tk.Label(window, text="Username:")
username_label.pack()
username_entry = tk.Entry(window)
username_entry.pack()

# Password label and entry
password_label = tk.Label(window, text="Password:")
password_label.pack()
password_entry = tk.Entry(window, show="*")
password_entry.pack()

# Confirm password label and entry
confirm_password_label = tk.Label(window, text="Confirm Password:")
confirm_password_label.pack()
confirm_password_entry = tk.Entry(window, show="*")
confirm_password_entry.pack()

# Register button
register_button = tk.Button(window, text="Register", command=register)
register_button.pack()

# Login button
login_button = tk.Button(window, text="Login", command=login)
login_button.pack()

# Result label
result_label = tk.Label(window, text="")
result_label.pack()

window.mainloop()

# Close the database connection
conn.close()
