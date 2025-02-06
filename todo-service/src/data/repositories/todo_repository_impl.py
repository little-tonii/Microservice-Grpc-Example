from typing import Optional
from data.models.todo_model import TodoModel
from domain.entites.todo_entity import TodoEntity
from domain.repositories.todo_repository import TodoRepository
from sqlalchemy.orm import Session
from src.common.utils.data_mapper import TodoMapper

class TodoRepositoryImpl(TodoRepository):
    
    database: Session
    
    def __init__(self, database: Session):
        self.database = database
        
    async def create(self, todo: TodoEntity) -> TodoEntity:
        todo_model = TodoMapper.entity_to_model(todo_entity=todo)
        self.database.add(todo_model)
        self.database.commit()
        self.database.refresh(todo_model)
        return todo_model
    
    async def get_by_id(self, id: int) -> Optional[TodoEntity]:
        return self.database.query(TodoModel).filter(TodoModel.id == id).first()
    
    async def update(self, todo: TodoEntity) -> TodoEntity:
        existing_todo = self.database.query(TodoModel).filter(TodoModel.id == todo.id).first()
        if existing_todo:
            existing_todo.title = todo.title
            existing_todo.description = todo.description
            existing_todo.completed = todo.completed
            self.database.add(existing_todo)
            self.database.commit()
        return existing_todo
    
    async def delete(self, id: int) -> bool:
        todo = self.database.query(TodoModel).filter(TodoModel.id == id).first()
        if todo:
            self.database.delete(todo)
            self.database.commit()
            return True
        return False