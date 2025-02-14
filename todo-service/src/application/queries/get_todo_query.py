from dataclasses import dataclass

from src.domain.exceptions.data_not_found_exception import DataNotFoundException
from src.application.dtos.todo_dto import GetTodoResponse
from src.domain.repositories.todo_repository import TodoRepository


@dataclass
class GetTodoQuery:
    id: int
    
class GetTodoQueryHandler:
    todo_repository: TodoRepository
    
    def __init__(self, todo_repository: TodoRepository):
        self.todo_repository = todo_repository
        
    async def handle(self, query: GetTodoQuery) -> GetTodoResponse:
        todo_entity = await self.todo_repository.get_by_id(id=query.id)
        if not todo_entity:
            raise DataNotFoundException(message="Todo không tồn tại")
        return GetTodoResponse(
            id=todo_entity.id,
            title=todo_entity.title,
            description=todo_entity.description,
            completed=todo_entity.completed
        )