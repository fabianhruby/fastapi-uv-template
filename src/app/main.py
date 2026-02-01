"""Main entry point for the app."""

from fastapi import FastAPI

from core.app import create_app

from .config import settings

app: FastAPI = create_app(settings=settings)
