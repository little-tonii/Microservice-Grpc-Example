from src.application.dtos.todo_dto import CreateTodoRequest, DeleteTodoRequest, GetAllTodoRequest, GetTodoRequest, UpdateTodoRequest
from src.domain.exceptions.data_not_found_exception import DataNotFoundException
from src.application.services.todo_application_service import TodoApplicationService
from src.presentation.grpc.generated import todo_service_pb2, todo_service_pb2_grpc
from src.infastructure.config.container import container
from grpc import ServicerContext, StatusCode

class TodoGrpcService(todo_service_pb2_grpc.TodoServiceServicer):
    todo_application_service: TodoApplicationService
    
    def __init__(self):
        self.todo_application_service = container.todo_application_service()
        
    async def CreateTodo(self, request, context: ServicerContext):
        try:
            response = await self.todo_application_service.create_todo(
                request=CreateTodoRequest(
                    title=request.title,
                    description=request.description
                )
            )
            return todo_service_pb2.CreateTodoResponse(
                id=response.id,
                title=response.title,
                description=response.description,
                completed=response.completed
            )
        except Exception as e:
            context.set_code(StatusCode.INTERNAL)
            context.set_details(str(e)) 
            return todo_service_pb2.CreateTodoResponse()
    
    async def GetTodo(self, request, context: ServicerContext):
        try:
            response = await self.todo_application_service.get_todo(
                request=GetTodoRequest(id=request.id)
            )
            return todo_service_pb2.GetTodoResponse(
                id=response.id,
                title=response.title,
                description=response.description,
                completed=response.completed
            )
        except DataNotFoundException as e:
            context.set_code(StatusCode.NOT_FOUND)
            context.set_details(e.message)
            return todo_service_pb2.GetTodoResponse()
        except Exception as e:
            context.set_code(StatusCode.INTERNAL)
            context.set_details(str(e)) 
            return todo_service_pb2.GetTodoResponse()
    
    async def UpdateTodo(self, request, context: ServicerContext):
        try:
            response = await self.todo_application_service.update_todo(
                request=UpdateTodoRequest(
                    id=request.id,
                    title=request.title if request.HasField('title') else None,
                    description=request.description if request.HasField('description') else None,
                    completed=request.completed if request.HasField('completed') else None
                )
            )
            return todo_service_pb2.UpdateTodoResponse(
                id=response.id,
                title=response.title,
                description=response.description,
                completed=response.completed
            )
        except DataNotFoundException as e:
            context.set_code(StatusCode.NOT_FOUND)
            context.set_details(e.message)
            return todo_service_pb2.UpdateTodoResponse()
        except Exception as e:
            context.set_code(StatusCode.INTERNAL)
            context.set_details(str(e)) 
            return todo_service_pb2.UpdateTodoResponse()
    
    async def DeleteTodo(self, request, context: ServicerContext):
        try:
            response = await self.todo_application_service.delete_todo(
                request=DeleteTodoRequest(id=request.id)
            )
            return todo_service_pb2.DeleteTodoResponse(
                success=response.success
            )
        except DataNotFoundException as e:
            context.set_code(StatusCode.NOT_FOUND)
            context.set_details(e.message)
            return todo_service_pb2.DeleteTodoResponse()
        except Exception as e:
            context.set_code(StatusCode.INTERNAL)
            context.set_details(str(e)) 
            return todo_service_pb2.DeleteTodoResponse()
    
    async def GetAllTodos(self, request, context: ServicerContext):
        try:
            response = await self.todo_application_service.get_all_todo(
                request=GetAllTodoRequest()
            )
            todos = [
                todo_service_pb2.Todo(
                    id=todo.id,
                    title=todo.title,
                    description=todo.description,
                    completed=todo.completed
                )
                for todo in response.todos
            ]
            return todo_service_pb2.GetAllTodoResponse(todos=todos)
        except Exception as e:
            context.set_code(StatusCode.INTERNAL)
            context.set_details(str(e)) 
            return todo_service_pb2.GetAllTodoResponse()