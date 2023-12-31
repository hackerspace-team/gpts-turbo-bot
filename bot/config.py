import os
from pathlib import Path
from typing import ClassVar, List

from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import SecretStr


class Settings(BaseSettings):
    BASE_DIR: ClassVar[Path] = Path(__file__).resolve().parent.parent

    USER_BATCH_SIZE: int = 500
    LIMIT_BETWEEN_REQUESTS_SECONDS: int = 30
    ADMIN_CHAT_IDS: List[str] = ["354543567", "6078317830"]

    BOT_TOKEN: SecretStr
    YOOKASSA_TOKEN: SecretStr

    CERTIFICATE_NAME: SecretStr
    STORAGE_NAME: SecretStr

    OPENAI_API_KEY: SecretStr
    REPLICATE_API_TOKEN: SecretStr

    model_config = SettingsConfigDict(env_file=str(BASE_DIR / f'.env.{os.getenv("ENVIRONMENT", "testing")}'),
                                      env_file_encoding='utf-8')


config = Settings()