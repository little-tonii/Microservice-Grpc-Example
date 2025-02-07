import grpc

from src.presentation.service.todo_service import TodoService
from src.presentation.grpc.generated import todo_service_pb2_grpc

SERVER_PORT = 50051

def serve():
    server = grpc.aio.server()
    todo_service = TodoService()
    todo_service_pb2_grpc.add_TodoServiceServicer_to_server(todo_service, server)
    server.add_insecure_port(f'[::]:{SERVER_PORT}')
    return server