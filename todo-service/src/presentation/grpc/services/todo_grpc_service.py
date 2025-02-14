from src.application.services.todo_application_service import TodoApplicationService
from src.presentation.grpc.generated import todo_service_pb2, todo_service_pb2_grpc
from src.infastructure.config.container import container

class TodoGrpcService(todo_service_pb2_grpc.TodoServiceServicer):
    todo_application_service: TodoApplicationService
    
    def __init__(self):
        self.todo_application_service = container.todo_application_service()
        
    async def CreateTodo():
        pass
    
    async def GetTodo():
        pass
    
    async def UpdateTodo():
        pass
    
    async def DeleteTodo():
        pass
    
    async def GetAllTodos():
        pass