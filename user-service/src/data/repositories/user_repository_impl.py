from typing import Optional

from sqlalchemy import delete, select
from sqlalchemy.ext.asyncio import AsyncSession

from src.common.utils.data_mapper import UserMapper
from src.data.models.user_model import UserModel
from src.domain.entities.user_entity import UserEntity
from src.domain.repositories.user_repository import UserRepository

class UserRepositoryImpl(UserRepository):
    database_session: AsyncSession
    
    def __init__(self, database_session: AsyncSession):
        self.database_session = database_session

    async def get_by_id(self, id: int) -> Optional[UserEntity]:
        async with self.database_session as session:
            query = select(UserModel).where(UserModel.id == id)
            result = await session.execute(query)
            user_model = result.scalar_one_or_none()
            if not user_model:
                return None
            return UserMapper.map_to_entity(user_model=user_model)
    
    async def update(self, user_entity: UserEntity) -> UserEntity:
        async with self.database_session as session:
            async with session.begin(): 
                user_model = UserMapper.map_to_model(user_entity=user_entity)
                updated_model = await session.merge(user_model)
            return UserMapper.map_to_entity(user_model=updated_model)
    
    async def create(self, user_entity: UserEntity) -> UserEntity:
        async with self.database_session as session:
            async with session.begin():
                user_model = UserMapper.map_to_model(user_entity=user_entity)
                session.add(user_model)
            await session.refresh(user_model)
            user_entity.id = user_model.id
            return user_entity
    
    async def delete_by_id(self, id: int) -> bool:
        async with self.database_session as session:
            async with session.begin():
                query = delete(UserModel).where(UserModel.id == id)
                result = await session.execute(query)
            return result.rowcount > 0