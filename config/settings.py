from pydantic import BaseModel
from typing import List, Optional
import os


class Settings(BaseModel):
    # Basic settings
    PROJECT_NAME: str = "FastAPI Template"
    PROJECT_DESCRIPTION: str = "Production ready FastAPI template"
    VERSION: str = "1.0.0"
    ENVIRONMENT: str = "development"

    # API settings
    API_V1_STR: str = "/v1"

    # Security
    SECRET_KEY: str = 'askldjfhlkajh'
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    ALGORITHM: str = "HS256"

    # CORS
    ALLOWED_HOSTS: List[str] = ["*"]

    def assemble_cors_origins(cls, v):
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)

    # Database
    DATABASE_URL: Optional[str] = None

    # Logging
    LOG_LEVEL: str = "INFO"
    LOG_FORMAT: str = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"

    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()
