from typing import Annotated

from fastapi import Depends, HTTPException
from grpc.aio import AioRpcError
from app.repositories.todo_repository import TodoRepository
from app.schemas.requests.todo_schema_request import CreateTodoRequest, DeleteTodoRequest, GetTodoRequest, UpdateTodoRequest
from app.schemas.responses.todo_schema_response import CreateTodoResponse, DeleteTodoResponse, GetTodoResponse, UpdateTodoResponse
from app.core.exception_handler import handle_grpc_exception

class TodoService:
    todo_repository: TodoRepository
    
    def __init__(self, todo_repository: Annotated[TodoRepository, Depends()]):
        self.todo_repository = todo_repository
        
    async def create_todo(self, create_todo_request: CreateTodoRequest)-> CreateTodoResponse:
        try:
            index = await self.todo_repository.create(title=create_todo_request.title, description=create_todo_request.description)
            return CreateTodoResponse(id=index)
        except AioRpcError  as e:
            handle_grpc_exception(exception=e)
    
    async def update_todo(self, id: int, update_todo_request: UpdateTodoRequest) -> UpdateTodoResponse:
        try:
            pass
        except AioRpcError  as e:
            handle_grpc_exception(exception=e)

    async def get_todo(self, get_todo_request: GetTodoRequest) -> GetTodoResponse:
        try:
            pass
        except AioRpcError  as e:
            handle_grpc_exception(exception=e)
        
    async def delete_todo(self, delete_todo_request: DeleteTodoRequest) -> DeleteTodoResponse:
        try:
            pass
        except AioRpcError  as e:
            handle_grpc_exception(exception=e)