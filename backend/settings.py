from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=Path(__file__).parent / ".env")

    DATABASE_URL: str
    BOT_TOKEN: str
    WEBAPP_URL: str


settings = Settings()
