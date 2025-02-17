from asyncio import CancelledError
import asyncio
import grpc
from src.presentation.grpc.services.todo_grpc_service import TodoGrpcService
from src.infastructure.config.database import init_database
from src.presentation.grpc.generated import todo_service_pb2_grpc

SERVER_PORT = 50001

async def serve():
    server = grpc.aio.server()
    todo_service_pb2_grpc.add_TodoServiceServicer_to_server(
        servicer=TodoGrpcService(),
        server=server
    )
    server.add_insecure_port(f"[::]:{SERVER_PORT}")
    await server.start()
    print(f"Server is running on port {SERVER_PORT}")
    try:
        await server.wait_for_termination()
    except CancelledError:
        await server.stop(3)
        print("Server has been stopped.")


async def main():
    await init_database()
    await serve()
    
if __name__ == "__main__":
    asyncio.run(main=main())