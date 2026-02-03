"""Core application entry point."""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from core.logging import configure_logging

from .middleware.logging import LoggingMiddleware
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

    return app
