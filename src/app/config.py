"""Settings for the app."""

from typing import Literal

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings."""

    model_config = SettingsConfigDict(env_file=".env")

    title: str = "FastAPI App"
    summary: str = "FastAPI Template"
    description: str = "A template for implementing APIs with FastAPI"
    contact: dict = {"name": "Fabian Simon Hruby", "email": "fabian.hruby@gmail.com"}

    stage: Literal["local", "dev", "test", "prod"] = "local"


settings = Settings()
