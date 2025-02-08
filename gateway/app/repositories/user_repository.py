from typing import Annotated, Optional
from fastapi import Depends

from app.core.client_dependencies import get_user_grpc_client
from app.entities.user_entity import UserEntity
from app.grpc.generated.user_service_pb2_grpc import UserServiceStub
from app.grpc.generated import user_service_pb2
class UserRepository:
    user_grpc_client: UserServiceStub
    
    def __init__(self, user_grpc_client: Annotated[UserServiceStub, Depends(get_user_grpc_client)]):
        self.user_grpc_client = user_grpc_client
    
    async def get_by_id(self, id: int) -> UserEntity:
        request = user_service_pb2.GetUserByIdRequest(id=id)
        response = await self.user_grpc_client.GetUserById(request)
        return UserEntity(id=response.id, email=response.email)
        
    async def get_by_email(self, email: str) -> UserEntity:
        request = user_service_pb2.GetUserByEmailRequest(email=email)
        response = await self.user_grpc_client.GetUserByEmail(request)
        return UserEntity(id=response.id, email=response.email)
        
    async def update(self, id: int, hashed_password: Optional[str], refresh_token: Optional[str]) -> UserEntity:
        request = user_service_pb2.UpdateUserRequest(id=id)
        if hashed_password:
            request.hashed_password = hashed_password
        if refresh_token:
            request.refresh_token = refresh_token
        response = await self.user_grpc_client.UpdateUser(request)
        return UserEntity(id=response.id, email=response.email)

    async def create(self, email: str, hashed_password:str, refresh_token: str) -> UserEntity:
        request = user_service_pb2.CreateUserRequest(
            email=email,
            hashed_password=hashed_password,
            refresh_token=refresh_token
        )
        response = await self.user_grpc_client.CreateUser(request)
        return UserEntity(id=response.id, email=response.email)
    
    async def delete(self, id: int) -> bool:
        request = user_service_pb2.DeleteUserRequest(id=id)
        response = self.user_grpc_client.DeleteUser(request)
        return response.success