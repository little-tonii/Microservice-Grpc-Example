from dependency_injector import containers, providers

from src.application.commands.create_todo_command import CreateTodoCommand, CreateTodoCommandHandler
from src.application.commands.delete_todo_command import DeleteTodoCommand, DeleteTodoCommandHandler
from src.application.commands.update_todo_command import UpdateTodoCommand, UpdateTodoCommandHandler
from src.application.queries.get_all_todo_query import GetAllTodoQuery, GetAllTodoQueryHandler
from src.application.queries.get_todo_query import GetTodoQuery, GetTodoQueryHandler
from src.infastructure.config.database import async_engine
from src.application.services.todo_application_service import TodoApplicationService
from src.infastructure.config.mediator import Mediator
from src.infastructure.repositories.todo_repository_impl import TodoRepositoryImpl

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import sessionmaker

class Container(containers.DeclarativeContainer):
    session_factory = providers.Singleton(sessionmaker, bind=async_engine, class_=AsyncSession, expire_on_commit=False)
    todo_repository = providers.Singleton(TodoRepositoryImpl, session_factory=session_factory)
    mediator = providers.Singleton(
        Mediator, 
        handlers= {
            GetTodoQuery: providers.Factory(GetTodoQueryHandler, todo_repository=todo_repository),
            GetAllTodoQuery: providers.Factory(GetAllTodoQueryHandler, todo_repository=todo_repository),
            CreateTodoCommand: providers.Factory(CreateTodoCommandHandler, todo_repository=todo_repository),
            DeleteTodoCommand: providers.Factory(DeleteTodoCommandHandler, todo_repository=todo_repository),
            UpdateTodoCommand: providers.Factory(UpdateTodoCommandHandler, todo_repository=todo_repository),
        }
    )
    todo_application_service = providers.Singleton(TodoApplicationService, mediator=mediator)
    
container = Container()