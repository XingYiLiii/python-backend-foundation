"""Health check endpoints."""

from fastapi import APIRouter

health_router = APIRouter()


@health_router.get("/health/live")
def health_live() -> dict[str, str]:
    """Return the application's liveness status."""
    return {"status": "ok"}
