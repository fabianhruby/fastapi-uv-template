"""Rate limiting middleware."""

import logging
from collections.abc import Awaitable
from typing import cast

from fastapi import Request, Response
from fastapi.responses import JSONResponse
from redis.asyncio import Redis
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint

from core.middleware.rate_limiting.models import PathRateLimit

logger = logging.getLogger(__name__)

# Atomically increments the key and sets expiry on first access.
_INCR_EXPIRE_SCRIPT = """
local current = redis.call('INCR', KEYS[1])
if current == 1 then
    redis.call('EXPIRE', KEYS[1], ARGV[1])
end
return current
"""


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
        self.path_limits: dict[str, PathRateLimit] = {
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

        path_limit: PathRateLimit | None = self.path_limits.get(path)
        if path_limit:
            limit: int = path_limit.limit
            window: int = path_limit.window_seconds
        else:
            limit = self.default_limit
            window = self.window_seconds

        key = f"rate_limit:{path}:{client_ip}"

        try:
            current = await cast(
                Awaitable[int],
                self.redis_client.eval(_INCR_EXPIRE_SCRIPT, 1, key, window),
            )
        except Exception:
            logger.exception("Redis unavailable, returning 503")
            return JSONResponse(
                status_code=503,
                content={"detail": "Service temporarily unavailable"},
            )

        if current > limit:
            return JSONResponse(
                status_code=429,
                content={"detail": "Rate limit exceeded"},
            )

        return await call_next(request)
