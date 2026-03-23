"""Rate limiting models."""

from pydantic import BaseModel


class PathRateLimit(BaseModel):
    """Defines a rate limit for a specific path."""

    path: str
    limit: int
    window_seconds: int
