from typing import Annotated

from fastapi import Depends
from app.core.client_dependencies import todo_grpc_client
from app.grpc.generated import todo_service_pb2
from app.grpc.generated.todo_service_pb2_grpc import TodoServiceStub


class TodoRepository:
    client: TodoServiceStub
    
    def __init__(self, client: Annotated[TodoServiceStub, Depends(todo_grpc_client)]):
        self.client = client
        
    async def create(self, title: str, description: str) -> int:
        request = todo_service_pb2.CreateTodoRequest(
            title=title,
            description=description
        )
        response = await self.client.CreateTodo(request)
        return 1