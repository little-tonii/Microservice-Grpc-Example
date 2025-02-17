from dataclasses import dataclass
from typing import Optional

from src.domain.entities.todo_entity import TodoEntity

@dataclass
class UpdateTodoRequest:
    id: int
    title: Optional[str]
    description: Optional[str]
    completed: Optional[bool]

@dataclass
class UpdateTodoResponse:
    id: int
    title: str
    description: str
    completed: bool

@dataclass
class DeleteTodoRequest:
    id: int
    
@dataclass
class DeleteTodoResponse:
    success: bool

@dataclass
class CreateTodoRequest:
    title: str
    description: str
    
@dataclass
class CreateTodoResponse:
    id: int
    title: str
    description: str
    completed: bool
    
@dataclass
class GetTodoRequest:
    id: int
    
@dataclass
class GetTodoResponse:
    id: int
    title: str
    description: str
    completed: bool
    
@dataclass
class GetAllTodoRequest:
    pass

@dataclass
class GetAllTodoResponse:
    todos: list[TodoEntity]