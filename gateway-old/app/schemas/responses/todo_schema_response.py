from pydantic import BaseModel


class CreateTodoResponse(BaseModel):
    id: int
    
class UpdateTodoResponse(BaseModel):
    id: int
    
class GetTodoResponse(BaseModel):
    id: int
    title: str
    description: str
    completed: bool
    
class DeleteTodoResponse(BaseModel):
    id: int