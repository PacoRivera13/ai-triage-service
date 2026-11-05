import pytest

from app.config import Settings


def test_default_model(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("ANTHROPIC_MODEL", raising=False)

    settings = Settings(_env_file=None)

    assert settings.anthropic_model == "claude-sonnet-5-5"


def test_model_comes_from_environment(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("ANTHROPIC_MODEL", "some-other-model")

    settings = Settings(_env_file=None)

    assert settings.anthropic_model == "some-other-model"


def test_api_key_is_hidden_when_printed(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("ANTHROPIC_API_KEY", "not-a-real-key")

    settings = Settings(_env_file=None)

    assert "not-a-real-key" not in repr(settings)
