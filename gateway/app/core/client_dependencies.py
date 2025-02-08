import grpc
from app.grpc.generated import user_service_pb2_grpc

class ClientAdresses:
    USER_SERVICE: str = "localhost:50000"
    
async def get_user_grpc_client():
    channel = grpc.aio.insecure_channel(ClientAdresses.TODO_SERVICE)
    return user_service_pb2_grpc.TodoServiceStub(channel=channel)