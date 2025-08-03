# For Database Connection
import sqlite3

conn = sqlite3.connect('users.db', check_same_thread=False)
cursor = conn.cursor()
