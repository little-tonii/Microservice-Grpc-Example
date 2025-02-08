from dependency_injector import providers
from dependency_injector.containers import DeclarativeContainer
from sqlalchemy.ext.asyncio import AsyncSession

from src.data.datasource.database import AsyncSessionLocal
from src.data.repositories.user_repository_impl import UserRepositoryImpl
from src.domain.repositories.user_repository import UserRepository
from src.domain.usecases.user_usecases import UserUsecases

class Container(DeclarativeContainer):
    database_session: AsyncSession = providers.Factory(AsyncSessionLocal)
    user_repository: UserRepository = providers.Factory(UserRepositoryImpl, database_session=database_session)
    user_usecases: UserUsecases = providers.Factory(UserUsecases, user_repository=user_repository)
    
container = Container()