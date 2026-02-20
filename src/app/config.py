"""Settings for the app."""

import json
from enum import Enum
from typing import Any

from pydantic import field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Stage(Enum):
    """Represents the deployment stage."""

    LOCAL = "local"
    DEV = "dev"
    TEST = "test"
    PROD = "prod"


class CORSSettings(BaseSettings):
    """CORS settings."""

    model_config = SettingsConfigDict(env_prefix="CORS_")

    allow_origins: list[str] = ["*"]
    allow_credentials: bool = True
    allow_methods: list[str] = ["*"]
    allow_headers: list[str] = ["*"]


class RedisSettings(BaseSettings):
    """Settings for redis used in rate limiting."""

    model_config = SettingsConfigDict(env_prefix="REDIS_")

    url: str = "redis://localhost:6379/0"
    encoding: str = "utf-8"
    decode_responses: bool = True


class PathRateLimit(BaseSettings):
    """Defines a rate limit for a specific path."""

    path: str
    limit: int
    window_seconds: int


class RateLimitingSettings(BaseSettings):
    """Settings for rate limiting."""

    model_config = SettingsConfigDict(env_prefix="RATE_LIMITING_")

    default_limit: int = 100
    window_seconds: int = 3600
    redis: RedisSettings = RedisSettings()
    path_limits: list[PathRateLimit] = []

    @field_validator("path_limits", mode="before")
    @classmethod
    def parse_path_limits(cls, v: Any) -> Any:
        """Allow path_limits to be parsed from a JSON string."""
        if isinstance(v, str):
            try:
                return json.loads(v)
            except json.JSONDecodeError:
                # Let pydantic handle the error for a malformed string
                pass
        return v


class Settings(BaseSettings):
    """Application settings."""

    model_config = SettingsConfigDict(env_file=".env")

    title: str = "FastAPI App"
    summary: str = "FastAPI Template"
    description: str = "A template for implementing APIs with FastAPI"
    contact: dict = {"name": "Fabian Simon Hruby", "email": "fabian.hruby@gmail.com"}

    stage: Stage = Stage.LOCAL

    cors: CORSSettings = CORSSettings()

    rate_limiting: RateLimitingSettings = RateLimitingSettings()


settings = Settings()
