"""FastAPI application entry point."""

from fastapi import FastAPI

from app.core.config import get_settings


def create_app() -> FastAPI:
    """Create and configure the FastAPI application."""
    settings = get_settings()
    return FastAPI(title=settings.app_name, debug=settings.debug)


app = create_app()
