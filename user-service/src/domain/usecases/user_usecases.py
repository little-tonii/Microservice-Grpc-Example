from typing import Optional
from src.common.exceptions.data_not_found_exception import DataNotFoundException
from src.common.exceptions.user_already_exists_exception import UserAlreadyExistsException
from src.domain.entities.user_entity import UserEntity
from src.domain.repositories.user_repository import UserRepository


class UserUsecases:
    user_repository: UserRepository
    
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository
        
    async def get_user_by_id(self, id: int) -> UserEntity:
        user_entity = await self.user_repository.get_by_id(id=id)
        if not user_entity:
            raise DataNotFoundException(message="Không tìm thấy người dùng")
        return user_entity
    
    async def update_user(self, id: int, hashed_password: Optional[str], refresh_token: Optional[str]) -> int:
        user_entity = await self.user_repository.get_by_id(id=id)
        if not user_entity:
            raise DataNotFoundException("Không tìm thấy người dùng")
        if hashed_password:
            user_entity.hashed_password = hashed_password
        if refresh_token:
            user_entity.refresh_token = refresh_token
        return await self.user_repository.update(user_entity=user_entity)
    
    async def create_user(self, email: str, hashed_password: str) -> int:
        existed_user = await self.user_repository.get_by_email(email=email)
        if existed_user:
            raise UserAlreadyExistsException(email=email)
        new_user = UserEntity(email=email, hashed_password=hashed_password)
        return await self.user_repository.create(user_entity=new_user)
    
    async def delete_user_by_id(self, id: int) -> bool:
        existed_user = await self.user_repository.get_by_id(id=id)
        if not existed_user:
            raise DataNotFoundException("Không tìm thấy người dùng")
        return await self.user_repository.delete_by_id(id=id)