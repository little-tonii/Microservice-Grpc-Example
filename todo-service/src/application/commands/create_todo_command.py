from dataclasses import dataclass

from src.application.dtos.todo_dto import CreateTodoResponse
from src.domain.repositories.todo_repository import TodoRepository


@dataclass
class CreateTodoCommand:
    title: str
    description: str
    
class CreateTodoCommandHandler:
    todo_repository: TodoRepository
    
    def __init__(self, todo_repository: TodoRepository):
        self.todo_repository = todo_repository
        
    async def handle(self, command: CreateTodoCommand) -> CreateTodoResponse:
        created_todo = await self.todo_repository.create(title=command.title, description=command.description)
        return CreateTodoResponse(
            id=created_todo.id,
            title=created_todo.title,
            description=created_todo.description,
            completed=created_todo.completed
        )