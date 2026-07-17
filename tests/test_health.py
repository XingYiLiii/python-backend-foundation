"""Tests for health-check endpoints."""

from fastapi.testclient import TestClient


def test_live_health_check(client: TestClient) -> None:
    """The live endpoint reports a running API process."""
    response = client.get("/api/v1/health/live")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
