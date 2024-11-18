## Python Noticeboard

간단한 게시판 애플리케이션입니다. 이 프로젝트는 FastAPI를 사용한 백엔드와 React를 사용한 프론트엔드로 구성되어 있으며, 회원가입 기능을 포함하고 있습니다.

### 목차

1. 환경 설정
1. 디렉토리 구조
1. 백엔드 구동 방법
1. 프론트엔드 구동 방법
1. 주의 사항
1. 라이선스

### 환경 설정

### 시스템 환경

	Python 버전: 3.10 (Pyenv로 관리)
	가상환경: Pyenv 가상환경 사용
	Node.js 버전: 14 이상
	데이터베이스: MySQL 8 (로컬호스트)
	호스트: localhost
	포트: 3306 (기본 포트)
	사용자명: root
	비밀번호: root
	데이터베이스명: your_database_name (실제 데이터베이스 이름으로 변경하세요)

### 개발 도구

	백엔드: FastAPI, Pydantic, mysql.connector
	프론트엔드: React, JavaScript

### 디렉토리 구조
```
python-noticeboard/
├── backend/
│   ├── app/
│   │   ├── api/
│   │   │   └── v1/
│   │   │       └── endpoints/
│   │   │           └── user.py
│   │   ├── core/
│   │   │   ├── config.py
│   │   │   └── security.py
│   │   ├── crud/
│   │   │   └── user.py
│   │   ├── db/
│   │   │   ├── init_db.py
│   │   │   └── session.py
│   │   ├── schemas/
│   │   │   ├── __init__.py
│   │   │   └── user.py
│   │   └── main.py
│   └── requirements.txt
├── frontend/
│   ├── package.json
│   ├── public/
│   │   └── index.html
│   └── src/
│       ├── App.js
│       └── components/
│           └── UserForm.js
└── README.md
```

### 백엔드 구동 방법

1. #### 데이터베이스 설정

	•	MySQL에 your_database_name이라는 데이터베이스를 생성합니다. 실제 사용할 데이터베이스 이름으로 변경하세요.
```sql
CREATE DATABASE your_database_name;
```

2. #### 환경 설정
```bash
cd python-noticeboard/backend
pyenv install 3.10.0
pyenv virtualenv 3.10.0 noticeboard-env
pyenv local noticeboard-env
pyenv activate noticeboard-env
pip install -r requirements.txt
```
3. #### 환경 변수 설정 
	•	backend/app/core/config.py 파일에서 데이터베이스 설정을 실제 환경에 맞게 수정합니다.
  ```
  from pydantic_settings import BaseSettings

  class Settings(BaseSettings):
      DB_HOST: str = "localhost"
      DB_USER: str = "root"
      DB_PASSWORD: str = "root"
      DB_NAME: str = "your_database_name"  # 실제 데이터베이스 이름으로 변경하세요
      DB_PORT: int = 3306

  settings = Settings()
  ```

4. #### 서버 실행
	•	Uvicorn을 사용하여 FastAPI 서버를 실행합니다.
  ```
  uvicorn app.main:app --reload
  ```

### 프론트엔드 구동 방법

```
cd python-noticeboard/frontend
npm install
npm start
```