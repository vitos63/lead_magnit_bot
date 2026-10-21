from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=Path(__file__).parent.parent / ".env", extra="ignore")

    DATABASE_URL: str
    BOT_TOKEN: str
    BOT_USERNAME: str
    ADMIN_TG_ID: int
    CHANNEL_ID: str
    WEBAPP_URL: str
    OPENROUTER_API_KEY: str


settings = Settings()
