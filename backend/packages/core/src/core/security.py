from datetime import datetime, timedelta, timezone
import jwt
from passlib.context import CryptContext

pwd_context = CryptContext(
    schemas=["bcrypt"],
    deprecated="auto",
)

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def create_access_token(data: dict, secret: str, expires_delta: timedelta) -> str:
    """创建许可 Token
    Args:
        data: 数据字典
        secret: 签名密钥
        expires_delta: Token 有效期

    Returns:
        返回混淆后的许可令牌 Token
    """
    data_copy = data.copy()
    data_copy["exp"] = datetime.now(timezone.utc) + expires_delta
    data_copy["type"] = "access"
    encode = jwt.encode(data_copy, secret, algorithm="HS256")
    return encode

def create_refresh_token(data: dict, secret: str, expires_delta: timedelta) -> str:
    """创建长期 Token
    Args:
        data: 数据字典
        secret: 签名密钥
        expires_delta: Token 有效期

    Returns:
        返回混淆后的长期令牌 Token
    """
    data_copy = data.copy()
    data_copy["exp"] = datetime.now(timezone.utc) + expires_delta
    data_copy["type"] = "refresh"
    encode = jwt.encode(data_copy, secret, algorithm="HS256")
    return encode

def decode_token(token: str, secret: str) -> dict | None:
    """对 Token 进行解码
    Args:
        token: 令牌 Token
        secret: 签名密钥

    Returns:
        原始数据字典
    """
    try:
        return jwt.decode(token, secret, algorithms=["HS256"])
    except jwt.JWTError:
        return None