import bcrypt
from db import query_db

def register_user(username, password):
    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    try:
        query_db("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed))
        return True, "User registered."
    except Exception as e:
        return False, str(e)

def authenticate_user(username, password):
    result = query_db("SELECT password FROM users WHERE username = ?", (username,), fetch=True)
    if result:
        stored_password = result[0][0]
        if bcrypt.checkpw(password.encode(), stored_password):
            return True
    return False
