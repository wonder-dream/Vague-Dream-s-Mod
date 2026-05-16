from anyio.functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8"
    )

    # 运行环境
    app_env: str = "dev"
    debug: bool = True

    # 数据库
    database_url: str = "postgresql+asyncpg://toolkit:toolkit@localhost:5432/toolkit"

    # 安全
    jwt_secret: str = "change_me"
    jwt_algorithm: str = "HS256"
    jwt_access_token_expire_minutes: int = 15
    jwt_refresh_token_expire_days: int = 7

    # 服务器
    server_host: str = "0.0.0.0"
    server_port: int = 8000
    cors_origins: str = "http://localhost:5173,http://localhost:1420"

    # LLM
    deepseek_api_key: str = ""
    deepseek_base_url: str = "https://api.deepseek.com/v1"

    # Embedding
    qwen_api_key: str = ""
    qwen_base_url: str = "https://api.siliconflow.cn/v1"
    embedding_dimensions: int = 1536

    # 存储
    data_path: str = "./data"
    notes_storage_path: str = "./data/notes"

    # 备份
    backup_dir: str = "./data/backups"
    backup_retention_days: int = 7
    backup_schedule_hour: int = 3

    # 前端
    frontend_api_base_url: str = "http://localhost:8000"

@lru_cache
def get_settings() -> Settings:
    return Settings()
