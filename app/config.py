from pathlib import Path

from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict

# Anchored to this file so .env is found whichever folder the app starts from.
ENV_FILE = Path(__file__).resolve().parent.parent / ".env"


class Settings(BaseSettings):
    # env_ignore_empty: a blank value like ANTHROPIC_API_KEY= counts as not set.
    # Unknown keys in .env are rejected at startup, which catches misspellings.
    model_config = SettingsConfigDict(env_file=ENV_FILE, env_ignore_empty=True)

    # SecretStr hides the value in logs and repr().
    # Optional so the app and its tests can run without a key.
    anthropic_api_key: SecretStr | None = None
    anthropic_model: str = "claude-sonnet-5-5"
