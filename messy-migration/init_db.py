import sqlite3
import bcrypt

conn = sqlite3.connect('users.db')
cursor = conn.cursor()

# Create the users table
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    password TEXT NOT NULL
)
''')

# Insert sample users with hashed passwords
users = [
    ("John Doe", "john@example.com", "password123"),
    ("Jane Smith", "jane@example.com", "secret456"),
    ("Bob Johnson", "bob@example.com", "qwerty789")
]

for name, email, raw_password in users:
    hashed_pw = bcrypt.hashpw(raw_password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    cursor.execute("INSERT INTO users (name, email, password) VALUES (?, ?, ?)", (name, email, hashed_pw))
    
    #INSERTING THE HASHED PASSWORD INTO THE DATABASE

conn.commit()
conn.close()

print("Database initialized with sample data")
