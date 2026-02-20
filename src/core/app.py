"""Core application entry point."""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from core.middleware.logging.config import configure_logging

from .middleware.logging.logging import LoggingMiddleware
from .middleware.rate_limiting.redis_client import get_redis_client
from .middleware.rate_limiting.redis_rate_limiter import RedisRateLimitingMiddleware
from .routers.health import core_router


def create_app(settings) -> FastAPI:
    """Create a FastAPI App with health and live check endpoints."""
    configure_logging(settings=settings)

    app = FastAPI(
        title=settings.title,
        summary=settings.summary,
        description=settings.description,
        contact=settings.contact,
    )

    app.include_router(router=core_router)
    app.add_middleware(LoggingMiddleware)  # ty:ignore
    app.add_middleware(
        CORSMiddleware,  # ty:ignore
        allow_origins=settings.cors.allow_origins,
        allow_credentials=settings.cors.allow_credentials,
        allow_methods=settings.cors.allow_methods,
        allow_headers=settings.cors.allow_headers,
    )
    app.add_middleware(
        RedisRateLimitingMiddleware,  # ty:ignore
        redis_client=get_redis_client(settings=settings.rate_limiting.redis),
        default_limit=settings.rate_limiting.default_limit,
        window_seconds=settings.rate_limiting.window_seconds,
        path_limits=settings.rate_limiting.path_limits,
    )

    return app
