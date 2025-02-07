from datetime import datetime, timezone
from typing import Annotated
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from fastapi import HTTPException
from starlette import status
from app.core.enviroment_variable import settings
from app.repositories.user_repository import UserRepository
from app.utils.token_util import TokenKey

oauth2_bearer = OAuth2PasswordBearer(tokenUrl='user/login')        

class TokenClaims:
    id: int
    
    def __init__(self, id: str):
        self.id = id

async def verify_access_token(
        user_repository: Annotated[UserRepository, Depends()],
        token: Annotated[OAuth2PasswordBearer, Depends(oauth2_bearer)]) -> TokenClaims | None:
    try:
        payload = jwt.decode(token=token, key=settings.secret_key, algorithms=[settings.hash_algorithm])
        user_id: int = payload.get(TokenKey.ID)
        expires: int = payload.get(TokenKey.EXPIRES)
        if user_id is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Token không hợp lệ')
        if expires and datetime.now(timezone.utc).timestamp() > expires:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Token không hợp lệ')
        if user_repository.find_user_by_id(id=user_id) is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Token không hợp lệ')    
        return TokenClaims(id=user_id)
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Token không hợp lệ')