"""Settings for the app."""

from enum import Enum

from pydantic_settings import BaseSettings, SettingsConfigDict


class Stage(Enum):
    """Represents the deployment stage."""

    LOCAL = "local"
    DEV = "dev"
    TEST = "test"
    PROD = "prod"


class Settings(BaseSettings):
    """Application settings."""

    model_config = SettingsConfigDict(env_file=".env")

    title: str = "FastAPI App"
    summary: str = "FastAPI Template"
    description: str = "A template for implementing APIs with FastAPI"
    contact: dict = {"name": "Fabian Simon Hruby", "email": "fabian.hruby@gmail.com"}

    stage: Stage = Stage.LOCAL


settings = Settings()
