from abc import ABC, abstractmethod
from typing import Optional

from src.domain.entities.user_entity import UserEntity


class UserRepository(ABC):
    
    @abstractmethod
    async def get_by_id(self, id: int) -> Optional[UserEntity]:
        pass
    
    @abstractmethod
    async def update(self, user_entity: UserEntity) -> UserEntity:
        pass
    
    @abstractmethod
    async def create(self, user_entity: UserEntity) -> UserEntity:
        pass
    
    @abstractmethod
    async def delete_by_id(self, id: int) -> bool:
        pass