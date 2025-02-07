from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.asyncio import AsyncSession

engine = create_engine("sqlite:///./todos.db", connect_args={"check_same_thread": False})

AsyncSessionLocal = sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False
)

Base = declarative_base()

# def get_database():
#     database = AsyncSessionLocal()
#     try:
#         yield database
#     finally:
#         database.close()