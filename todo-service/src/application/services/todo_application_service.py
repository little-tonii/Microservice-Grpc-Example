from src.application.commands.delete_todo_command import DeleteTodoCommand, DeleteTodoCommandHandler
from src.application.commands.update_todo_command import UpdateTodoCommand, UpdateTodoCommandHandler
from src.application.queries.get_all_todo_query import GetAllTodoQuery, GetAllTodoQueryHandler
from src.application.queries.get_todo_query import GetTodoQuery, GetTodoQueryHandler
from src.application.commands.create_todo_command import CreateTodoCommand, CreateTodoCommandHandler
from src.application.dtos.todo_dto import CreateTodoRequest, CreateTodoResponse, DeleteTodoRequest, DeleteTodoResponse, GetAllTodoRequest, GetAllTodoResponse, GetTodoRequest, GetTodoResponse, UpdateTodoRequest, UpdateTodoResponse


class TodoApplicationService:
    create_todo_command_handler: CreateTodoCommandHandler
    update_todo_command_handler: UpdateTodoCommandHandler
    delete_todo_command_handler: DeleteTodoCommandHandler
    get_all_todo_query_handler: GetAllTodoQueryHandler
    get_todo_query_handler: GetTodoQueryHandler
                
    def __init__(
        self,
        create_todo_command_handler: CreateTodoCommandHandler,
        update_todo_command_handler: UpdateTodoCommandHandler,
        delete_todo_command_handler: DeleteTodoCommandHandler,
        get_all_todo_query_handler: GetAllTodoQueryHandler,
        get_todo_query_handler: GetTodoQueryHandler
    ):
        self.create_todo_command_handler = create_todo_command_handler
        self.update_todo_command_handler = update_todo_command_handler
        self.delete_todo_command_handler = delete_todo_command_handler
        self.get_all_todo_query_handler = get_all_todo_query_handler
        self.get_todo_query_handler = get_todo_query_handler
        
    async def get_todo(self, request: GetTodoRequest) -> GetTodoResponse:
        return await self.get_todo_query_handler.handle(query=GetTodoQuery(id=request.id))
    
    async def get_all_todo(self, request: GetAllTodoRequest) -> GetAllTodoResponse:
        return await self.get_all_todo_query_handler.handle(query=GetAllTodoQuery())
    
    async def create_todo(self, request: CreateTodoRequest) -> CreateTodoResponse:
        return await self.create_todo_command_handler.handle(
            command=CreateTodoCommand(
                title=request.title,
                description=request.description
            )
        )
    
    async def update_todo(self, request: UpdateTodoRequest) -> UpdateTodoResponse:
        return await self.update_todo_command_handler.handle(
            command=UpdateTodoCommand(
                id=request.id,
                title=request.title,
                description=request.description,
                completed=request.completed
            )
        )
        
    async def delete_todo(self, request: DeleteTodoRequest) -> DeleteTodoResponse:
        return await self.mediator.send(DeleteTodoCommand(id=request.id))