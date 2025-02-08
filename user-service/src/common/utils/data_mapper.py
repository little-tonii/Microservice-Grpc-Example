from src.data.models.user_model import UserModel
from src.domain.entities.user_entity import UserEntity


class UserMapper:
    
    @staticmethod
    def map_to_model(user_entity: UserEntity) -> UserModel:
        return UserModel(
            id=user_entity.id,
            email=user_entity.email,
            hashed_password=user_entity.hashed_password,
            refresh_token=user_entity.refresh_token
        )
    
    @staticmethod
    def map_to_entity(user_model: UserModel) -> UserEntity:
        return UserEntity(
            id=user_model.id,
            email=user_model.email,
            hashed_password=user_model.hashed_password,
            refresh_token=user_model.refresh_token
        )