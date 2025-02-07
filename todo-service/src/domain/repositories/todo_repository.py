from abc import ABC, abstractmethod
from typing import Optional
from src.domain.entites.todo_entity import TodoEntity

class TodoRepository(ABC):
    
    @abstractmethod
    async def create(self, todo: TodoEntity) -> TodoEntity:
        pass
    
    @abstractmethod
    async def get_by_id(self, id: int) -> Optional[TodoEntity]:
        pass
    
    @abstractmethod
    async def update(self, todo: TodoEntity) -> Optional[TodoEntity]:
        pass
    
    @abstractmethod
    async def delete(self, id: int) -> bool:
        pass