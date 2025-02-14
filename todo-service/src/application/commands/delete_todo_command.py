from dataclasses import dataclass

from src.domain.exceptions.data_not_found_exception import DataNotFoundException
from src.application.dtos.todo_dto import DeleteTodoResponse
from src.domain.repositories.todo_repository import TodoRepository


@dataclass
class DeleteTodoCommand:
    id: int
    
class DeleteTodoCommandHandler:
    todo_repository: TodoRepository
    
    def __init__(self, todo_repository: TodoRepository):
        self.todo_repository = todo_repository

    async def handle(self, command: DeleteTodoCommand) -> DeleteTodoResponse:
        success =  await self.todo_repository.delete_by_id(id=command.id)
        if not success:
            raise DataNotFoundException(message="Todo không tồn tại")
        return DeleteTodoResponse(success=success)