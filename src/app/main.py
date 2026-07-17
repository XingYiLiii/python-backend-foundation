"""FastAPI application entry point."""

from fastapi import FastAPI

from app.api.v1.router import v1_router
from app.core.config import get_settings


def create_app() -> FastAPI:
    """Create and configure the FastAPI application."""
    settings = get_settings()
    application = FastAPI(title=settings.app_name, debug=settings.debug)
    application.include_router(v1_router, prefix=settings.api_v1_prefix)
    return application


app = create_app()
