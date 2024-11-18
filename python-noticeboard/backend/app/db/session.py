import mysql.connector
from mysql.connector import pooling
from app.core.config import settings

dbconfig = {
    "host": settings.DB_HOST,
    "user": settings.DB_USER,
    "password": settings.DB_PASSWORD,
    "database": settings.DB_NAME,
    "port": settings.DB_PORT,
}

# 커넥션 풀 생성
connection_pool = pooling.MySQLConnectionPool(pool_name="notidashboard_pool_name",
                                              pool_size=5,
                                              **dbconfig)

def get_db():
    conn = connection_pool.get_connection()
    cursor = conn.cursor(dictionary=True)
    try:
        yield conn, cursor
    finally:
        cursor.close()
        conn.close()