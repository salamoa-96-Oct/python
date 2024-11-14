# 커플 다이어리 및 커플 캘린더 애플리케이션

## 소개

이 프로젝트는 **FastAPI**와 **React**를 사용하여 커플들이 함께 사용할 수 있는 다이어리 및 캘린더 애플리케이션입니다. 커플은 일상을 공유하고, 중요한 날짜를 함께 관리할 수 있습니다.

## 기술 스택

- **백엔드**
  - Python 3.x
  - FastAPI
  - SQLAlchemy
  - Alembic (데이터베이스 마이그레이션)
  - JWT 인증
- **프론트엔드**
  - React
  - Axios (API 통신)
  - React Router
- **데이터베이스**
  - PostgreSQL (또는 선택에 따라 다른 RDBMS)
- **환경 설정 및 배포**
  - Docker & Docker Compose
  - GitHub Actions (CI/CD)

## 디렉토리 구조
project/
├── backend/
│   ├── app/
│   │   ├── init.py
│   │   ├── main.py
│   │   ├── core/
│   │   │   ├── init.py
│   │   │   ├── config.py
│   │   │   ├── security.py
│   │   │   └── database.py
│   │   ├── models/
│   │   │   ├── init.py
│   │   │   ├── user.py
│   │   │   ├── diary.py
│   │   │   └── calendar.py
│   │   ├── schemas/
│   │   │   ├── init.py
│   │   │   ├── user.py
│   │   │   ├── diary.py
│   │   │   └── calendar.py
│   │   ├── crud/
│   │   │   ├── init.py
│   │   │   ├── user.py
│   │   │   ├── diary.py
│   │   │   └── calendar.py
│   │   ├── api/
│   │   │   ├── init.py
│   │   │   ├── deps.py
│   │   │   └── v1/
│   │   │       ├── init.py
│   │   │       ├── endpoints/
│   │   │           ├── init.py
│   │   │           ├── auth.py
│   │   │           ├── users.py
│   │   │           ├── diaries.py
│   │   │           └── calendars.py
│   │   ├── tests/
│   │       ├── init.py
│   │       └── test_main.py
│   ├── alembic/
│   │   └── … (Alembic 관련 파일들)
│   ├── alembic.ini
│   ├── requirements.txt
│   └── README.md
├── frontend/
│   ├── public/
│   │   └── index.html
│   ├── src/
│   │   ├── components/
│   │   │   └── … (재사용 가능한 컴포넌트들)
│   │   ├── pages/
│   │   │   ├── HomePage.jsx
│   │   │   ├── DiaryPage.jsx
│   │   │   └── CalendarPage.jsx
│   │   ├── App.jsx
│   │   ├── index.js
│   │   └── routes/
│   │       └── index.js
│   ├── package.json
│   ├── .env
│   └── README.md
└── README.md
## 기능 개요

### 사용자 인증 및 관리

- 회원가입 및 로그인
- JWT를 활용한 인증
- 프로필 조회 및 수정
- 커플 연동 및 해제

### 다이어리 기능

- 일기 작성, 수정, 삭제
- 이미지 및 파일 첨부
- 커플 간 일기 공유 옵션
- 일기 목록 및 상세 조회

### 캘린더 기능

- 일정 추가, 수정, 삭제
- 기념일 및 이벤트 관리
- 커플 공동 캘린더
- 일정 알림 기능

## 개발 환경 설정

### 전제 조건

- **Python 3.8 이상**
- **Node.js 14.x 이상**
- **Docker (선택 사항)**
- **PostgreSQL (또는 다른 RDBMS)**

### 백엔드 설정

1. **가상환경 생성 및 활성화**

   ```bash
   cd project/backend
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # macOS/Linux
   source venv/bin/activate

2.	패키지 설치
 - pip install -r requirements.txt