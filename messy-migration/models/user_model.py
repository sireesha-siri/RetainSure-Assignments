import bcrypt
from utils.db import cursor, conn

#=================== QUERY FOR GETTING ALL USERS ===================

def get_all_users():
    cursor.execute("SELECT * FROM users")
    return cursor.fetchall()

#=================== FETCHING THE DETAILS WITH USER ID ===================

def get_user_by_id(user_id):
    cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
    return cursor.fetchone()

#=================== INSERTING DATA ===================

def create_user(name, email, password):
    hashed_pw = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    cursor.execute("INSERT INTO users (name, email, password) VALUES (?, ?, ?)", (name, email, hashed_pw))
    conn.commit()

#=================== UPDATING THE USER CREDENTIALS ===================

def update_user(user_id, name, email):
    cursor.execute("UPDATE users SET name = ?, email = ? WHERE id = ?", (name, email, user_id))
    conn.commit()

#=================== DELETING THE USER ===================

def delete_user(user_id):
    cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
    conn.commit()

#=================== SEARCHING WITH USER NAME ===================

def search_users_by_name(name):
    cursor.execute("SELECT id, name, email FROM users WHERE name LIKE ?", ('%' + name + '%',))
    return cursor.fetchall()

#=================== TRYING TO LOGIN WITH EMAIL AND PASSWORD OF THE USER ===================

def login_user(email, password):
    cursor.execute("SELECT id, password FROM users WHERE email = ?", (email,))
    user = cursor.fetchone()
    if user and bcrypt.checkpw(password.encode('utf-8'), user[1].encode('utf-8')):
        return user  # user[0] is id
    return None
