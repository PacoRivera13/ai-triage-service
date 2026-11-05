from pathlib import Path

import pytest
from pydantic import ValidationError

from app.config import ENV_FILE, Settings


@pytest.fixture(autouse=True)
def clean_environment(monkeypatch: pytest.MonkeyPatch) -> None:
    """Stop real env vars on the machine from affecting these tests."""
    monkeypatch.delenv("ANTHROPIC_API_KEY", raising=False)
    monkeypatch.delenv("ANTHROPIC_MODEL", raising=False)


def write_env_file(folder: Path, content: str) -> Path:
    env_file = folder / ".env"
    env_file.write_text(content, encoding="utf-8")
    return env_file


def test_default_model() -> None:
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


def test_values_load_from_env_file(tmp_path: Path) -> None:
    env_file = write_env_file(
        tmp_path,
        "ANTHROPIC_API_KEY=not-a-real-key\nANTHROPIC_MODEL=some-other-model\n",
    )

    settings = Settings(_env_file=env_file)

    assert settings.anthropic_api_key is not None
    assert settings.anthropic_api_key.get_secret_value() == "not-a-real-key"
    assert settings.anthropic_model == "some-other-model"


def test_blank_values_count_as_not_set(tmp_path: Path) -> None:
    env_file = write_env_file(tmp_path, "ANTHROPIC_API_KEY=\nANTHROPIC_MODEL=\n")

    settings = Settings(_env_file=env_file)

    assert settings.anthropic_api_key is None
    assert settings.anthropic_model == "claude-sonnet-5-5"


def test_misspelled_key_is_rejected(tmp_path: Path) -> None:
    env_file = write_env_file(tmp_path, "ANTHROPIC_MODLE=some-other-model\n")

    with pytest.raises(ValidationError):
        Settings(_env_file=env_file)


def test_env_file_path_does_not_depend_on_working_directory() -> None:
    assert Settings.model_config["env_file"] == ENV_FILE
    assert ENV_FILE.is_absolute()
    assert (ENV_FILE.parent / "pyproject.toml").exists()
