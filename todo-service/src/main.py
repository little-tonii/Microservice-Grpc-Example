import asyncio
from asyncio import CancelledError
from src.presentation.grpc.server import serve

async def run_server():
    server = serve()
    await server.start()
    print("Server is running on port 50051...")

    try:
        await server.wait_for_termination()
    except CancelledError:
        await server.stop(3)
        print("Server has been stopped.")

if __name__ == "__main__":
    asyncio.run(run_server())