"""Tests for application settings."""

import pytest
from pydantic import ValidationError

from app.core.config import Settings, get_settings


def test_settings_use_defaults(monkeypatch: pytest.MonkeyPatch) -> None:
    """Settings use documented defaults without environment overrides."""
    for variable in ("APP_NAME", "APP_ENV", "APP_DEBUG", "APP_API_V1_PREFIX"):
        monkeypatch.delenv(variable, raising=False)

    settings = Settings(_env_file=None)

    assert settings.app_name == "python-backend-foundation"
    assert settings.app_env == "development"
    assert settings.debug is False
    assert settings.api_v1_prefix == "/api/v1"


def test_settings_read_environment_overrides(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """Settings read supported values from environment variables."""
    monkeypatch.setenv("APP_ENV", "test")
    monkeypatch.setenv("APP_DEBUG", "true")

    settings = get_settings()

    assert settings.app_env == "test"
    assert settings.debug is True


def test_settings_reject_invalid_environment(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """Settings reject unsupported application environments."""
    monkeypatch.setenv("APP_ENV", "staging")

    with pytest.raises(ValidationError):
        get_settings()
