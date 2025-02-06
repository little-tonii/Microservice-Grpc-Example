from data.models.todo_model import TodoModel
from domain.entites.todo_entity import TodoEntity

class TodoMapper:

    @staticmethod
    def model_to_entity(todo_model: TodoModel) -> TodoEntity:
        return TodoEntity(
            id=todo_model.id,
            title=todo_model.title,
            description=todo_model.description,
            completed=todo_model.completed
        )
    
    @staticmethod
    def entity_to_model(todo_entity: TodoEntity) -> TodoModel:
        return TodoModel(
            id=todo_entity.id,
            title=todo_entity.title,
            description=todo_entity.description,
            completed=todo_entity.completed
        )