from repositories.todo_repository import TodoRepository
from entites.todo_entity import TodoEntity
from src.common.exceptions.todo_not_found_exception import TodoNotFoundException

class TodoUsecases:
    todo_repository: TodoRepository
    
    def __init__(self, todo_repository: TodoRepository):
        self.todo_repository = todo_repository
        
    async def create_todo(self, title: str, description: str):
        todo = TodoEntity(title=title, description=description)
        todo_model =  await self.todo_repository.create(todo=todo)
        return todo_model.id
    
    async def get_todo(self, id: int):
        todo = await self.todo_repository.get_by_id(id=id)
        if todo is None:
            raise TodoNotFoundException(id=id)
        return todo

    async def delete_todo(self, id: int):
        return await self.todo_repository.delete(id=id)
    
    async def update_todo(self, id: int, title: str, description: str, completed: bool):
        todo = await self.todo_repository.get_by_id(id=id)
        if todo is None:
            raise TodoNotFoundException(id=id)
        if title:
            todo.title = title
        if description:
            todo.description = description
        if completed:
            todo.completed = completed
        return await self.todo_repository.update(todo=todo)