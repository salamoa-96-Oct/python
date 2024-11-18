from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DB_HOST: str = "localhost"
    DB_USER: str = "root"
    DB_PASSWORD: str = "root"
    DB_NAME: str = "notidashboard"
    DB_PORT: int = 3306

settings = Settings()