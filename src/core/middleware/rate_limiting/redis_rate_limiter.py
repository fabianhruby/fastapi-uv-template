"""Rate limiting middleware."""

from fastapi import HTTPException, Request, Response
from redis.asyncio import Redis
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint

from app.config import PathRateLimit


class RedisRateLimitingMiddleware(BaseHTTPMiddleware):
    """Middleware for rate limiting using a redis db."""

    def __init__(
        self,
        app,
        redis_client: Redis,
        default_limit: int,
        window_seconds: int,
        path_limits: list[PathRateLimit],
    ):
        super().__init__(app)
        self.redis_client: Redis = redis_client
        self.default_limit: int = default_limit
        self.window_seconds: int = window_seconds
        self.path_limits: list[dict[str, str | int | float]] = {
            limit.path: limit for limit in path_limits
        }

    async def dispatch(
        self,
        request: Request,
        call_next: RequestResponseEndpoint,
    ) -> Response:
        """Apply the rate limiting to every request."""
        client_ip: str = request.client.host if request.client else "unknown"
        path = request.url.path

        # Check if there is a limit for a specific path
        path_limit: dict[str, str | int | float] = self.path_limits.get(path)
        if path_limit:
            limit: int | float = path_limit.limit
            window: int | float = path_limit.window_seconds

        else:
            limit: int | float = self.default_limit
            window: int | float = self.window_seconds

        key = f"rate_limit:{path}:{client_ip}"

        current = await self.redis_client.incr(key)
        if current == 1:
            await self.redis_client.expire(key, window)

        if current > limit:
            raise HTTPException(status_code=429, detail="Rate limit exceeded")

        return await call_next(request)
