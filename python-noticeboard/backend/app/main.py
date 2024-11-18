from fastapi import FastAPI
from app.api.v1.routers import router as api_router

app = FastAPI()

# API 라우터 등록
app.include_router(api_router)