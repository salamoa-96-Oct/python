from app.schemas.user import UserCreate
from mysql.connector import Error

def create_user(db, user: UserCreate):
    try:
        db.execute(
            "INSERT INTO users (name, email) VALUES (%s, %s)",
            (user.name, user.email)
        )
        db.connection.commit()
        return {"id": db.lastrowid, "name": user.name, "email": user.email}
    except Error as e:
        print(f"Error: {e}")
        return None

def get_user(db, user_id: int):
    db.execute("SELECT * FROM users WHERE id = %s", (user_id,))
    return db.fetchone()

def get_user_by_email(db, email: str):
    db.execute("SELECT * FROM users WHERE email = %s", (email,))
    return db.fetchone()

def get_users(db, skip: int = 0, limit: int = 10):
    db.execute("SELECT * FROM users LIMIT %s, %s", (skip, limit))
    return db.fetchall()