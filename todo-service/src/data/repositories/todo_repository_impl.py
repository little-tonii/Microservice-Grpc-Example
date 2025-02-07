from typing import Optional

from sqlalchemy import select
from src.data.models.todo_model import TodoModel
from src.domain.entites.todo_entity import TodoEntity
from src.domain.repositories.todo_repository import TodoRepository
from sqlalchemy.orm import Session
from src.common.utils.data_mapper import TodoMapper
from sqlalchemy.ext.asyncio import AsyncSession

class TodoRepositoryImpl(TodoRepository):
    
    database: AsyncSession
    
    def __init__(self, database: AsyncSession):
        self.database = database
        
    async def create(self, todo: TodoEntity) -> TodoEntity:
        async with self.database as session:
            async with session.begin():
                todo_model = TodoMapper.entity_to_model(todo_entity=todo)
                session.add(todo_model)
            await session.refresh(todo_model)
            return TodoMapper.model_to_entity(todo_model=todo_model)
    
    async def get_by_id(self, id: int) -> Optional[TodoEntity]:
        async with self.database as session:
            result = await session.execute(
                select(TodoModel).filter(TodoModel.id == id)
            )
            todo_model = result.scalars().first()
            return TodoMapper.model_to_entity(todo_model=todo_model) if todo_model else None
    
    async def update(self, todo: TodoEntity) -> Optional[TodoEntity]:
        async with self.database as session:
            async with session.begin():
                result = await session.execute(
                    select(TodoModel).filter(TodoModel.id == todo.id)
                )
                existing_todo = result.scalars().first()
                if existing_todo:
                    existing_todo.title = todo.title
                    existing_todo.description = todo.description
                    existing_todo.completed = todo.completed
            await session.refresh(existing_todo)
            return TodoMapper.model_to_entity(existing_todo) if existing_todo else None
    
    async def delete(self, id: int) -> bool:
        async with self.database as session:
            async with session.begin():
                result = await session.execute(select(TodoModel).filter(TodoModel.id == id))
                todo = result.scalars().first()
                if todo:
                    await session.delete(todo)
                    return True
        return False