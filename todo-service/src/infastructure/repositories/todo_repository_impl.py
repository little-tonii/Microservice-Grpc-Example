from typing import Optional

from sqlalchemy import select
from domain.entities.todo_entity import TodoEntity
from domain.repositories.todo_repository import TodoRepository

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import sessionmaker

from infastructure.models.todo_model import TodoModel

class TodoRepositoryImpl(TodoRepository):
    session_factory: sessionmaker[AsyncSession]
    
    def __init__(self, session_factory: sessionmaker):
        self.session_factory = session_factory
    
    async def get_by_id(self, id: int) -> Optional[TodoEntity]:
        async with self.session_factory() as session: 
            query = select(TodoModel).where(TodoModel.id == id)
            result = await session.execute(query)
            todo_mode = result.scalar_one_or_none()
            if not todo_mode:
                return None
            return TodoEntity(
                id=todo_mode.id,
                title=todo_mode.title,
                description=todo_mode.description,
                completed=todo_mode.completed
            )
    
    async def get_all(self) -> list[TodoEntity]:
        async with self.session_factory() as session:
            query = select(TodoModel)
            result = await session.execute(query)
            todo_models = result.scalars().all()
            return [
                TodoEntity(
                    id=todo_model.id,
                    title=todo_model.title,
                    description=todo_model.description,
                    completed=todo_model.completed
                )
                for todo_model in todo_models
            ]
    
    async def delete_by_id(self, id: int) -> bool: 
        async with self.session_factory() as session:
            query = select(TodoModel).where(TodoModel.id == id)
            result = await session.execute(query)
            todo_model = result.scalar_one_or_none()
            if not todo_model:
                return False
            await session.delete(todo_model)
            await session.commit()
            return True
    
    async def create(self, title: str, description: str) -> TodoEntity:
        async with self.session_factory() as session:
            todo_model = TodoModel(title=title, description=description)
            session.add(todo_model)
            await session.commit()
            return TodoEntity(
                id=todo_model.id,
                title=todo_model.title,
                description=todo_model.description,
                completed=todo_model.completed
            )
    
    async def update(self, id: int, title: str, description: str, completed: str) -> TodoEntity:
        async with self.session_factory() as session:
            query = select(TodoModel).where(TodoModel.id == id)
            result = await session.execute(query)
            todo_model = result.scalar_one()
            todo_model.title = title
            todo_model.description = description
            todo_model.completed = completed
            await session.commit()
            return TodoEntity(
                id=todo_model.id,
                title=todo_model.title,
                description=todo_model.description,
                completed=todo_model.completed
            )