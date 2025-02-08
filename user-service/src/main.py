import asyncio

import grpc
from src.data.datasource.database import init_database
from src.presentation.service.user_grpc_service import UserGrpcService
from src.presentation.grpc.generated import user_service_pb2_grpc
from asyncio import CancelledError

SERVER_PORT = 50000

async def serve():
    server = grpc.aio.server()
    user_service_pb2_grpc.add_UserServiceServicer_to_server(servicer=UserGrpcService(), server=server)
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