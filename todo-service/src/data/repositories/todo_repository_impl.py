from typing import Optional
from data.models.todo_model import TodoModel
from domain.entites.todo_entity import TodoEntity
from domain.repositories.todo_repository import TodoRepository
from sqlalchemy.orm import Session
from src.common.utils.data_mapper import TodoMapper
from sqlalchemy.ext.asyncio import AsyncSession

class TodoRepositoryImpl(TodoRepository):
    
    database: AsyncSession
    
    def __init__(self, database: AsyncSession):
        self.database = database
        
    async def create(self, todo: TodoEntity) -> TodoEntity:
        todo_model = TodoMapper.entity_to_model(todo_entity=todo)
        self.database.add(todo_model)
        await self.database.commit()
        await self.database.refresh(todo_model)
        return TodoMapper.model_to_entity(todo_model=todo_model)
    
    async def get_by_id(self, id: int) -> Optional[TodoEntity]:
        todo_model = await self.database.query(TodoModel).filter(TodoModel.id == id).first()
        if todo_model is None:
            return None
        return TodoMapper.model_to_entity(todo_model=todo_model)
    
    async def update(self, todo: TodoEntity) -> TodoEntity:
        existing_todo = await self.database.query(TodoModel).filter(TodoModel.id == todo.id).first()
        if existing_todo:
            existing_todo.title = todo.title
            existing_todo.description = todo.description
            existing_todo.completed = todo.completed
            self.database.add(existing_todo)
            await self.database.commit()
            await self.database.refresh(existing_todo)
            return TodoMapper.model_to_entity(todo_model=existing_todo)
        return None
    
    async def delete(self, id: int) -> bool:
        todo = await self.database.query(TodoModel).filter(TodoModel.id == id).first()
        if todo:
            await self.database.delete(todo)
            await self.database.commit()
            return True
        return False