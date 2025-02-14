from dataclasses import dataclass
from typing import Optional

from src.domain.exceptions.data_not_found_exception import DataNotFoundException
from src.application.dtos.todo_dto import UpdateTodoResponse
from src.domain.repositories.todo_repository import TodoRepository


@dataclass
class UpdateTodoCommand:
    id: int
    title: Optional[str]
    description: Optional[str]
    completed: Optional[bool]
    
class UpdateTodoCommandHandler:
    
    todo_repository: TodoRepository
    
    def __init__(self, todo_repository: TodoRepository):
        self.todo_repository = todo_repository
        
    async def handle(self, command: UpdateTodoCommand) -> UpdateTodoResponse:
        todo_entity = await self.todo_repository.get_by_id(id=command.id)
        if not todo_entity:
            raise DataNotFoundException(message="Todo không tồn tại")
        if command.title is not None:
            todo_entity.title = command.title
        if command.description is not None:
            todo_entity.description = command.description
        if command.completed is not None:
            todo_entity.completed = command.completed
        updated_todo = await self.todo_repository.update(
            id=todo_entity.id,
            title=todo_entity.title,
            description=todo_entity.description,
            completed=todo_entity.completed
        )
        return UpdateTodoResponse(
            id=updated_todo.id,
            title=updated_todo.title,
            description=updated_todo.description,
            completed=updated_todo.completed
        )