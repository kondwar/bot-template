import os

from dotenv import load_dotenv

load_dotenv()


def _required(name: str) -> str:
    value = os.getenv(name)
    if not value:
        raise RuntimeError(f"Missing required environment variable: {name}")
    return value


class Settings:
    BOT_TOKEN = _required("BOT_TOKEN")
    DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///data/data.db")
    AI_PROVIDER = os.getenv("AI_PROVIDER", "")
    AI_API_KEY = os.getenv("AI_API_KEY", "")
    AI_MODEL = os.getenv("AI_MODEL", "")
    ADMIN_IDS = [int(x) for x in os.getenv("ADMIN_IDS", "").split(",") if x.strip()]
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")


settings = Settings()
