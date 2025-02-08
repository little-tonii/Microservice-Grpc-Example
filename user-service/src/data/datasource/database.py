from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

async_engine = create_async_engine(
    url="sqlite+aiosqlite:///./user_service.db",
    echo=True,
    future=True,
    connect_args={"check_same_thread": False}
)

AsyncSessionLocal = sessionmaker(
    bind=async_engine,
    class_=AsyncSession,
    expire_on_commit=False
)

BaseModel = declarative_base()

async def init_database():
    async with async_engine.begin() as connection:
        await connection.run_sync(BaseModel.metadata.create_all)