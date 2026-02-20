"""Configuration for logging."""

import logging

STAGE_LOG_LEVEL: dict[str, str | int] = {
    "local": logging.DEBUG,
    "dev": logging.DEBUG,
    "test": logging.WARNING,
    "prod": logging.INFO,
}


def configure_logging(settings) -> None:
    """Configure logging based on the stage."""
    level: str | int = STAGE_LOG_LEVEL.get(settings.stage.value, logging.DEBUG)
    logging.basicConfig(
        level=level,
        format="%(asctime)s %(levelname)s %(name)s %(message)s",
        force=True,
    )
    logging.getLogger("uvicorn.access").setLevel(logging.WARNING)
    logging.getLogger("watchfile.main").setLevel(logging.WARNING)
    logging.getLogger("httpx").setLevel(logging.WARNING)
