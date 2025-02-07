import asyncio
from asyncio import CancelledError
import logging
from src.data.datasource.todo_database import Base, async_engine
from src.presentation.grpc.server import SERVER_PORT, serve

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def run_server():
    server = serve()
    await server.start()
    print(f"Server is running on port {SERVER_PORT}...")

    try:
        await server.wait_for_termination()
    except CancelledError:
        await server.stop(3)
        print("Server has been stopped.")
        
async def init_database():
    async with async_engine.begin() as connection:
        await connection.run_sync(Base.metadata.create_all)

async def main():
    await init_database()
    await run_server()

if __name__ == "__main__":
    asyncio.run(main())