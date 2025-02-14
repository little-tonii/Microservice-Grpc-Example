from abc import ABC, abstractmethod
from typing import Optional

from src.domain.entities.todo_entity import TodoEntity


class TodoRepository(ABC):
    
    @abstractmethod
    async def get_by_id(self, id: int) -> Optional[TodoEntity]:
        pass
    
    @abstractmethod
    async def get_all(self) -> list[TodoEntity]:
        pass
    
    @abstractmethod
    async def delete_by_id(self, id: int) -> bool: 
        pass
    
    @abstractmethod
    async def create(self, title: str, description: str) -> TodoEntity:
        pass
    
    @abstractmethod
    async def update(self, id: int, title: str, description: str, completed: str) -> TodoEntity:
        pass