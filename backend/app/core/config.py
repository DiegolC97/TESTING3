from pydantic_settings import BaseSettings
from typing import List
import os


class Settings(BaseSettings):
    # Project
    PROJECT_NAME: str = "TESTEST"
    VERSION: str = "0.1.0"
    API_V1_STR: str = "/api/v1"
    
    # Environment
    ENVIRONMENT: str = "development"
    
    # Security
    SECRET_KEY: str = "change-this-in-production"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8  # 8 days
    
    # Database
    DATABASE_URL: str = "postgresql://postgres:postgres@localhost:5432/testest_db"
    
    # CORS
    CORS_ORIGINS: List[str] = ["http://localhost:3000"]
    
    class Config:
        env_file = ".env"
        case_sensitive = True

    @property
    def async_database_url(self) -> str:
        """Convert sync DATABASE_URL to async version"""
        return self.DATABASE_URL.replace("postgresql://", "postgresql+asyncpg://")


settings = Settings()
