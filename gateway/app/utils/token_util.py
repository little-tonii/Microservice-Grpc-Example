from datetime import datetime, timedelta, timezone

from app.core.enviroment_variable import settings
from jose import jwt

class TokenKey:
    ID: str = "id"
    EXPIRES: str = "exp"

def create_access_token(user_id: int) -> str:
    encode = { TokenKey.ID: user_id }
    expires = datetime.now(timezone.utc) + timedelta(minutes=settings.access_token_expires)
    encode.update({ TokenKey.EXPIRES: expires })
    return jwt.encode(claims=encode, key=settings.secret_key, algorithm=settings.hash_algorithm)

def create_refresh_token(user_id: int) -> str:
    encode = { TokenKey.ID: user_id }
    expires = datetime.now(timezone.utc) + timedelta(minutes=settings.refresh_token_expires)
    encode.update({ TokenKey.EXPIRES: expires })
    return jwt.encode(claims=encode, key=settings.secret_key, algorithm=settings.hash_algorithm)