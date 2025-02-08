from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from starlette import status

from app.core.security_gaurd import TokenClaims, verify_access_token
from app.schemas.requests.user_schema_request import UserLoginRequest, UserRegisterRequest
from app.schemas.responses.user_schema_response import UserInforResponse, UserLoginResponse
from app.services.user_service import UserService

router = APIRouter(prefix="/user", tags=["User"])

# @router.post(path="/register", status_code=status.HTTP_201_CREATED)
# async def register(user_register: UserRegisterRequest, user_service: Annotated[UserService, Depends()]):
#     return user_service.register_user(user_register)

# @router.post(path="/login", status_code=status.HTTP_200_OK, response_model=UserLoginResponse)
# async def login(login_form: Annotated[OAuth2PasswordRequestForm, Depends()], user_service: Annotated[UserService, Depends()]):
#     return user_service.login_user(UserLoginRequest(email=login_form.username, password=login_form.password))

# @router.get(path="/infor", status_code=status.HTTP_200_OK, response_model=UserInforResponse)
# async def infor(claims: Annotated[TokenClaims | None, Depends(verify_access_token)],user_service: Annotated[UserService, Depends()]):
#     if claims is None:
#         raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token đã hết hạn")
#     return user_service.get_user_infor(claims.id)