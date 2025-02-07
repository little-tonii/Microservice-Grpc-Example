from dependency_injector import containers, providers
from dependency_injector.containers import DeclarativeContainer

from data.datasource.todo_database import AsyncSessionLocal, get_database
from data.repositories.todo_repository_impl import TodoRepositoryImpl
from domain.usecases.todo_usecases import TodoUsecases

class Container(DeclarativeContainer):
    database = providers.Singleton(AsyncSessionLocal)
    todo_repository = providers.Factory(TodoRepositoryImpl, database=database)
    todo_usecases = providers.Factory(TodoUsecases, todo_repository=todo_repository)
    
container = Container()