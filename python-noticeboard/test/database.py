import mysql.connector

# 데이터베이스 설정
DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "root",
    "database": "notidashboard",
}

def get_connection():
    """MySQL 데이터베이스 연결 생성"""
    connection = mysql.connector.connect(**DB_CONFIG)
    print("✅ MySQL 데이터베이스 연결 성공!")
    return connection

def create_tables():
    """제목 및 내용 테이블 생성"""
    connection = get_connection()
    cursor = connection.cursor()

    try:
        # 제목 테이블 생성
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS subjects (
            id INT AUTO_INCREMENT PRIMARY KEY,
            title VARCHAR(200) NOT NULL,
            create_date DATETIME DEFAULT CURRENT_TIMESTAMP
        )
        """)

        # 내용 테이블 생성
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS contents (
            id INT AUTO_INCREMENT PRIMARY KEY,
            subject_id INT NOT NULL,
            content TEXT NOT NULL,
            create_date DATETIME DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (subject_id) REFERENCES subjects (id) ON DELETE CASCADE
        )
        """)

        print("✅ 제목 및 내용 테이블 생성 완료!")

    finally:
        cursor.close()
        connection.close()

def insert_subject(title):
    """제목 데이터 삽입"""
    connection = get_connection()
    cursor = connection.cursor()

    try:
        cursor.execute("INSERT INTO subjects (title) VALUES (%s)", (title,))
        connection.commit()
        print(f"✅ 제목 추가 완료! ID: {cursor.lastrowid}")
        return cursor.lastrowid
    finally:
        cursor.close()
        connection.close()

def insert_content(subject_id, content):
    """내용 데이터 삽입"""
    connection = get_connection()
    cursor = connection.cursor()

    try:
        cursor.execute("INSERT INTO contents (subject_id, content) VALUES (%s, %s)", (subject_id, content))
        connection.commit()
        print(f"✅ 내용 추가 완료! ID: {cursor.lastrowid}")
        return cursor.lastrowid
    finally:
        cursor.close()
        connection.close()

def fetch_subjects():
    """모든 제목 조회"""
    connection = get_connection()
    cursor = connection.cursor(dictionary=True)

    try:
        cursor.execute("SELECT * FROM subjects")
        return cursor.fetchall()
    finally:
        cursor.close()
        connection.close()

def fetch_contents(subject_id):
    """특정 제목에 속한 내용 조회"""
    connection = get_connection()
    cursor = connection.cursor(dictionary=True)

    try:
        cursor.execute("SELECT * FROM contents WHERE subject_id = %s", (subject_id,))
        return cursor.fetchall()
    finally:
        cursor.close()
        connection.close()