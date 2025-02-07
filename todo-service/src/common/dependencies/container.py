from dependency_injector import containers, providers
from dependency_injector.containers import DeclarativeContainer

from src.data.datasource.todo_database import AsyncSessionLocal
from src.data.repositories.todo_repository_impl import TodoRepositoryImpl
from src.domain.usecases.todo_usecases import TodoUsecases

class Container(DeclarativeContainer):
    database = providers.Factory(AsyncSessionLocal)
    todo_repository = providers.Factory(TodoRepositoryImpl, database=database)
    todo_usecases = providers.Factory(TodoUsecases, todo_repository=todo_repository)
    
container = Container()
