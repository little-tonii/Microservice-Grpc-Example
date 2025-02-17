from dependency_injector import containers, providers

from src.application.commands.create_todo_command import CreateTodoCommandHandler
from src.application.commands.delete_todo_command import DeleteTodoCommandHandler
from src.application.commands.update_todo_command import UpdateTodoCommandHandler
from src.application.queries.get_all_todo_query import GetAllTodoQueryHandler
from src.application.queries.get_todo_query import GetTodoQueryHandler
from src.infastructure.config.database import async_engine
from src.application.services.todo_application_service import TodoApplicationService
from src.infastructure.repositories.todo_repository_impl import TodoRepositoryImpl

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import sessionmaker

class Container(containers.DeclarativeContainer):
    session_factory = providers.Resource(
        lambda: sessionmaker(bind=async_engine, class_=AsyncSession, expire_on_commit=False)
    )
    
    todo_repository = providers.Singleton(
        TodoRepositoryImpl, session_factory=session_factory)
    
    create_todo_command_handler = providers.Factory(
        CreateTodoCommandHandler, todo_repository=todo_repository)
    
    update_todo_command_handler = providers.Factory(
        UpdateTodoCommandHandler, todo_repository=todo_repository)
    
    delete_todo_command_handler = providers.Factory(
        DeleteTodoCommandHandler, todo_repository=todo_repository)
    
    get_all_todo_query_handler = providers.Factory(
        GetAllTodoQueryHandler, todo_repository=todo_repository)
    
    get_todo_query_handler = providers.Factory(
        GetTodoQueryHandler, todo_repository=todo_repository)
    
    todo_application_service = providers.Singleton(
        TodoApplicationService,
        create_todo_command_handler=create_todo_command_handler,
        update_todo_command_handler=update_todo_command_handler,
        delete_todo_command_handler=delete_todo_command_handler,
        get_all_todo_query_handler=get_all_todo_query_handler,      
        get_todo_query_handler=get_todo_query_handler
    )
    
container = Container()