import grpc

from app.grpc.generated import todo_service_pb2_grpc


class ClientAdresses:
    TODO_SERVICE: str = "localhost:50051"


async def todo_grpc_client():
    channel = grpc.aio.insecure_channel(ClientAdresses.TODO_SERVICE)
    return todo_service_pb2_grpc.TodoServiceStub(channel=channel)