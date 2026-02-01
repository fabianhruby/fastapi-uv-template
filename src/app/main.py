"""Main entry point for the app."""

from fastapi import FastAPI

from core.app import create_app

from .config import app_settings

app: FastAPI = create_app(app_settings=app_settings)
