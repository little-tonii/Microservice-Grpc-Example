from application.commands.delete_todo_command import DeleteTodoCommand
from application.commands.update_todo_command import UpdateTodoCommand
from application.queries.get_all_todo_query import GetAllTodoQuery
from src.application.queries.get_todo_query import GetTodoQuery
from src.application.commands.create_todo_command import CreateTodoCommand
from src.application.dtos.todo_dto import CreateTodoRequest, CreateTodoResponse, DeleteTodoRequest, DeleteTodoResponse, GetAllTodoRequest, GetAllTodoResponse, GetTodoRequest, GetTodoResponse, UpdateTodoRequest, UpdateTodoResponse
from infastructure.config.mediator import Mediator


class TodoApplicationService:
    mediator: Mediator
    
    def __init__(self, mediator: Mediator):
        self.mediator = mediator
        
    async def get_todo(self, request: GetTodoRequest) -> GetTodoResponse:
        return await self.mediator.send(GetTodoQuery(id=request.id))
    
    async def get_all_todo(self, request: GetAllTodoRequest) -> GetAllTodoResponse:
        return await self.mediator.send(GetAllTodoQuery())
    
    async def create_todo(self, request: CreateTodoRequest) -> CreateTodoResponse:
        return await self.mediator.send(CreateTodoCommand(title=request.title, description=request.description))
    
    async def update_todo(self, request: UpdateTodoRequest) -> UpdateTodoResponse:
        return await self.mediator.send(UpdateTodoCommand(
            id=request.id,
            title=request.title,
            description=request.description,
            completed=request.completed
        ))
        
    async def delete_todo(self, request: DeleteTodoRequest) -> DeleteTodoResponse:
        return await self.mediator.send(DeleteTodoCommand(id=request.id))