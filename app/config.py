from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    database_url: str = "postgresql+asyncpg://postgres:postgres@db:5432/postgres"

    class Config:
        env_file = ".env"

settings = Settings()