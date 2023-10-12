from typing import List, Set
from pydantic import BaseSettings, AnyHttpUrl
from decouple import config


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    JWT_SECRET_KEY = config("JWT_SECRET_KEY", cast=str)
    JWT_REFRESH_SECRET_KEY = config("JWT_REFRESH_SECRET_KEY", cast=str)
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 999
    REFRESH_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = ["http://localhost:8000", "http://localhost",
                                              "https://crm-ais.web.app",
                                              "https://p02--react-front-1--qbjvdl5rjgvx.code.run"]
    ALLOWED_METHODS: Set[str] = {"*"}
    ALLOWED_HEADERS: Set[str] = {"*"}
    ALLOWED_CREDENTIALS: bool = True
    PROJECT_NAME: str = "Cotizador-AIS"
    SENDGRID_API_KEY = config("SENDGRID_API_KEY", cast=str)
    MONGO_CONNECTION_STRING = config("MONGO_CONNECTION_STRING", cast=str)

    class Config:
        case_sensitive = True


settings = Settings()
