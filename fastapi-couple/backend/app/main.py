# app/main.py

from fastapi import FastAPI
from app.api.v1.endpoints import auth, users, diaries, calendars
from app.core.config import settings

# 태그 메타데이터 정의 (선택 사항)
tags_metadata = [
    {
        "name": "auth",
        "description": "인증 관련 API",
    },
    {
        "name": "users",
        "description": "사용자 관리 API",
    },
    {
        "name": "diaries",
        "description": "다이어리 관리 API",
    },
    {
        "name": "calendars",
        "description": "캘린더 관리 API",
    },
]

app = FastAPI(
    title="커플 다이어리 및 캘린더 API",
    description="커플을 위한 다이어리 및 캘린더 서비스의 API 문서입니다.",
    version="1.0.0",
    openapi_tags=tags_metadata,
    docs_url="/docs",           # Swagger UI 경로 설정
    redoc_url="/redoc",         # ReDoc 경로 설정
    openapi_url="/openapi.json" # OpenAPI 스키마 경로 설정
)

# 라우터 등록
app.include_router(auth.router, prefix="/api/v1/auth", tags=["auth"])
app.include_router(users.router, prefix="/api/v1/users", tags=["users"])
app.include_router(diaries.router, prefix="/api/v1/diaries", tags=["diaries"])
app.include_router(calendars.router, prefix="/api/v1/calendars", tags=["calendars"])