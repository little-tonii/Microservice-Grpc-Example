from typing import Type, TypeVar

from src.application.commands.create_todo_command import CreateTodoCommand, CreateTodoCommandHandler
from src.application.commands.delete_todo_command import DeleteTodoCommand, DeleteTodoCommandHandler
from src.application.commands.update_todo_command import UpdateTodoCommand, UpdateTodoCommandHandler
from src.application.queries.get_all_todo_query import GetAllTodoQuery, GetAllTodoQueryHandler
from src.application.queries.get_todo_query import GetTodoQuery, GetTodoQueryHandler
from src.infastructure.config.container import container


T = TypeVar("T")
R = TypeVar("R")

class Mediator:
    handlers: dict[Type, object]
    
    def __init__(self):
        self.handlers = {}
        
    def register(self, request_type: Type[T], handler: object):
        self.handlers[request_type] = handler
    
    async def send(self, request: T) -> R:
        handler = self.handlers.get(type(request))
        if handler is None:
            raise Exception(f"Chưa đăng ký handler cho {type(request)}")
        return await handler.handle(request)