from mysql.connector import connection
from app.schemas.user import UserCreate
from app.core.security import get_password_hash

def get_user_by_email(conn: connection.MySQLConnection, cursor, email: str):
    query = "SELECT * FROM users WHERE email = %s"
    cursor.execute(query, (email,))
    user = cursor.fetchone()
    return user

def create_user(conn: connection.MySQLConnection, cursor, user_in: UserCreate):
    hashed_password = get_password_hash(user_in.password)
    query = """
    INSERT INTO users (email, hashed_password, full_name)
    VALUES (%s, %s, %s)
    """
    cursor.execute(query, (user_in.email, hashed_password, user_in.full_name))
    conn.commit()
    user_id = cursor.lastrowid
    return {
        "id": user_id,
        "email": user_in.email,
        "full_name": user_in.full_name,
    }