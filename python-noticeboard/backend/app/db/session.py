import mysql.connector
from contextlib import contextmanager
from app.core.config import settings

# 데이터베이스 설정
DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "root",
    "database": "notidashboard"
}

@contextmanager
def get_db():
    connection = mysql.connector.connect(**DB_CONFIG)
    cursor = connection.cursor(dictionary=True)  # 결과를 딕셔너리로 반환
    try:
        yield cursor
    finally:
        cursor.close()
        connection.close()