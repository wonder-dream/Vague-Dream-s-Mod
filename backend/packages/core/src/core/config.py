from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # 运行环境
    app_env: str = 'dev'
    debug: bool = False

    # 数据库
    database_url: str = "postgres://postgres:postgres@localhost:5432/postgres"
    db_password: str = ''

    # 安全
    jwt_secret: str = "change_me"
    jwt_algorithm: str = "HS256"
    jwt_access_token_expires_minutes: int = 6000
    jwt_refresh_token_expires_days: int = 600

    # 服务器
    server_host: str = "127.0.0.1"
    server_port: int = 8080
    cors_origins: str = '*'

    # LLM
    deepseek_api_key: str = ''
    deepseek_base_url: str = ''

    # Embedding
    qwen_api_key: str = ''
    qwen_base_url: str = ''
    embedding_dimensions: int = 128
