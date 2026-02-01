"""Core application entry point."""

from fastapi import FastAPI

from .routers.health import core_router


def create_app(app_settings) -> FastAPI:
    """Create a FastAPI App with health and live check endpoints."""
    app = FastAPI(
        title=app_settings.title,
        summary=app_settings.summary,
        description=app_settings.description,
        contact=app_settings.contact,
    )
    app.include_router(router=core_router)

    return app
