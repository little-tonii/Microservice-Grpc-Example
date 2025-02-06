import grpc

from src.presentation.grpc.generated.todo_service_pb2_grpc import TodoService
from src.presentation.grpc.generated import todo_service_pb2_grpc

def serve():
    server = grpc.aio.server()
    todo_service_pb2_grpc.add_TodoServiceServicer_to_server(TodoService(), server)
    server.add_insecure_port('[::]:50051')
    return server