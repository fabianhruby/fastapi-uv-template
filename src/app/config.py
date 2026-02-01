"""Settings for the app."""

from pydantic_settings import BaseSettings, SettingsConfigDict


class AppSettings(BaseSettings):
    """FastAPI App Settings."""

    title: str = "FastAPI App"
    summary: str = "FastAPI Template"
    description: str = "A template for implementing APIs with FastAPI"
    contact: dict = {"name": "Fabian Simon Hruby", "email": "fabian.hruby@gmail.com"}


class Settings(BaseSettings):
    """Application settings."""

    model_config = SettingsConfigDict(env_file=".env")


app_settings = AppSettings()
settings = Settings()
