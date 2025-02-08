from typing import Annotated
from fastapi import Depends, HTTPException
from app.repositories.user_repository import UserRepository
from app.schemas.requests.user_schema_request import UserLoginRequest, UserRegisterRequest
from passlib.context import CryptContext
from starlette import status
from app.utils.token_util import create_access_token, create_refresh_token
from app.schemas.responses.user_schema_response import UserInforResponse, UserLoginResponse
from app.core.security_gaurd import TokenClaims, verify_access_token
class UserService:
    user_repository: UserRepository
    bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

    def init(self, user_repository: Annotated[UserRepository, Depends()]):
        self.user_repository = user_repository
        
    def register_user(self, user_register: UserRegisterRequest) -> None:
        if self.user_repository.find_user_by_email(user_register.email) is not None:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email đã được sử dụng")
        self.user_repository.create_user(
            email=user_register.email, 
            hased_password=self.bcrypt_context.hash(user_register.password)
        )
        
    def login_user(self, user_login: UserLoginRequest) -> UserLoginResponse:
        user_model = self.user_repository.find_user_by_email(email=user_login.email)
        if user_model is None:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email hoặc mật khẩu không chính xác")
        if not self.bcrypt_context.verify(user_login.password, user_model.hashed_password):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email hoặc mật khẩu không chính xác")
        refresh_token = create_refresh_token(user_id=user_model.id)
        access_token = create_access_token(user_id=user_model.id)
        user_model.refresh_token = refresh_token
        self.user_repository.update_user(user_model)
        return UserLoginResponse(access_token=access_token, refresh_token=refresh_token, token_type='bearer')
    
    def get_user_infor(self, id: int) -> UserInforResponse:
        user_model = self.user_repository.find_user_by_id(id=id)
        return UserInforResponse(id=user_model.id, email=user_model.email)