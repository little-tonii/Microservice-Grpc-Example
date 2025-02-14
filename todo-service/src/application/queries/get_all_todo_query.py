from dataclasses import dataclass
from src.application.dtos.todo_dto import GetAllTodoResponse
from src.domain.repositories.todo_repository import TodoRepository

@dataclass
class GetAllTodoQuery:
    pass

class GetAllTodoQueryHandler:
    todo_repository: TodoRepository
    
    def __init__(self, todo_repository: TodoRepository):
        self.todo_repository = todo_repository
        
    async def handle(self, query: GetAllTodoQuery) -> GetAllTodoResponse:
        todo_entities = await self.todo_repository.get_all()
        return GetAllTodoResponse(todos=todo_entities)