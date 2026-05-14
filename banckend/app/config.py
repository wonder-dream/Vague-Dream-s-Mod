from pathlib import Path
from pydantic.v1 import BaseSettings

BASE_DIR = Path(__file__).resolve().parent.parent

class Settings(BaseSettings):
    DATABASE_URL: str
    SECRET_KEY: str

    class Config:
        env_file = BASE_DIR / ".env"
        env_file_encoding = "utf-8"