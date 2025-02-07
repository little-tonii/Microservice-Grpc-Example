import grpc
from common.dependencies import container
from common.exceptions.todo_not_found_exception import TodoNotFoundException
from domain.usecases.todo_usecases import TodoUsecases
from src.presentation.grpc.generated import todo_service_pb2, todo_service_pb2_grpc

class TodoSerivce(todo_service_pb2_grpc.TodoServiceServicer):
    todo_usecases: TodoUsecases
    
    def __init__(self):
        self.todo_usecases = container.todo_usecases()
        
    async def CreateTodo(self, request: todo_service_pb2.CreateTodoRequest, context) -> todo_service_pb2.CreateTodoResponse:
        try:
            todo_id = await self.todo_usecases.create_todo(title=request.title, description=request.description)
            return todo_service_pb2.CreateTodoResponse(id=todo_id)
        except Exception as e:
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details(str(e))
            return todo_service_pb2.CreateTodoResponse()
    
    async def GetTodo(self, request: todo_service_pb2.GetTodoRequest, context) -> todo_service_pb2.GetTodoResponse:
        try:
            todo = await self.todo_usecases.get_todo(id=request.id)
            return todo_service_pb2.GetTodoResponse(
                id=todo.id,
                title=todo.title,
                description=todo.description,
                completed=todo.completed
            )
        except TodoNotFoundException as e:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details(e.message)
            return todo_service_pb2.GetTodoResponse()
        except Exception as e:
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details(str(e))
            return todo_service_pb2.GetTodoResponse()
    
    async def UpdateTodo(self, request: todo_service_pb2.UpdateTodoRequest, context) -> todo_service_pb2.UpdateTodoResponse:
        try:
            updated_todo = await self.todo_usecases.update_todo(
                id=request.id,
                title=request.title,
                description=request.description,
                completed=request.completed
            )
            return todo_service_pb2.UpdateTodoResponse(id=updated_todo.id)
        except TodoNotFoundException as e:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details(e.message)
            return todo_service_pb2.UpdateTodoResponse()
        except Exception as e:
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details(str(e))
            return todo_service_pb2.UpdateTodoResponse()
    
    async def DeleteTodo(self, request: todo_service_pb2.DeleteTodoRequest, context) -> todo_service_pb2.DeleteTodoResponse:
        try:
            await self.todo_usecases.delete_todo(id=request.id)
            return todo_service_pb2.DeleteTodoResponse(id=request.id)
        except TodoNotFoundException as e:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details(e.message)
            return todo_service_pb2.DeleteTodoResponse()
        except Exception as e:
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details(str(e))
            return todo_service_pb2.DeleteTodoResponse()