"""Configuration for logging."""

import logging

STAGE_LOG_LEVEL: dict[str, str | int] = {
    "local": logging.DEBUG,
    "dev": logging.INFO,
    "test": logging.WARNING,
    "prod": logging.INFO,
}


def configure_logging(settings) -> None:
    """Configure  logging based on the stage."""
    level: str | int = STAGE_LOG_LEVEL.get(settings.stage.lower(), "local")
    logging.basicConfig(level=level)
