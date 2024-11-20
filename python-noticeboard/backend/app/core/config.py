from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DB_HOST: str
    DB_USER: str
    DB_PASSWORD: str
    DB_NAME: str
    DB_PORT: int

    class Config:
        # .env 파일 경로 설정 (기본적으로 프로젝트 루트)
        env_file = "app/core/.env"
        env_file_encoding = "utf-8"

settings = Settings()

# # 확인
# print(f"DB_HOST: {settings.DB_HOST}")
# print(f"DB_USER: {settings.DB_USER}")
# print(f"DB_PASSWORD: {settings.DB_PASSWORD}")
# print(f"DB_NAME: {settings.DB_NAME}")
# print(f"DB_PORT: {settings.DB_PORT}")