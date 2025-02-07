from typing import Annotated
from fastapi import APIRouter, Depends
from starlette import status

from app.schemas.requests.todo_schema_request import CreateTodoRequest, DeleteTodoRequest, GetTodoRequest, UpdateTodoRequest
from app.schemas.responses.todo_schema_response import CreateTodoResponse, DeleteTodoResponse, GetTodoResponse, UpdateTodoResponse
from app.services.todo_service import TodoService

router = APIRouter(prefix="/todo", tags=["Todo"])

@router.get(path="/{id}", status_code=status.HTTP_200_OK, response_model=GetTodoResponse)
async def get_todo(id: int, todo_service: Annotated[TodoService, Depends()]):
    return await todo_service.get_todo(get_todo_request=GetTodoRequest(id=id))

@router.post(path="/", status_code=status.HTTP_201_CREATED, response_model=CreateTodoResponse)
async def create_todo(create_todo_request: CreateTodoRequest, todo_service: Annotated[TodoService, Depends()]):
    return await todo_service.create_todo(create_todo_request=create_todo_request)

@router.put(path="/{id}", status_code=status.HTTP_200_OK, response_model=UpdateTodoResponse)
async def update_todo(id: int, update_todo_request: UpdateTodoRequest, todo_service: Annotated[TodoService, Depends()]):
    return await todo_service.update_todo(id=id, update_todo_request=update_todo_request)

@router.delete(path="/{id}", status_code=status.HTTP_200_OK, response_model=DeleteTodoResponse)
async def delete_todo(id: int, todo_service: Annotated[TodoService, Depends()]):
    return await todo_service.delete_todo(DeleteTodoRequest(id=id))