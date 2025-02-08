import grpc
from grpc import ServicerContext
from src.common.exceptions.data_not_found_exception import DataNotFoundException
from src.common.exceptions.user_already_exists_exception import UserAlreadyExistsException
from src.domain.usecases.user_usecases import UserUsecases
from src.presentation.grpc.generated import user_service_pb2, user_service_pb2_grpc
from src.common.dependencies.dependency_container import container

class UserGrpcService(user_service_pb2_grpc.UserServiceServicer):
    user_usecases: UserUsecases
    
    def __init__(self):
        self.user_usecases = container.user_usecases()
        
    async def GetUserById(self, request, context: ServicerContext):
        try:
            user_entity = await self.user_usecases.get_user_by_id(id=request.id)
            return user_service_pb2.GetUserResponse(
                id=user_entity.id, 
                email=user_entity.email,
                hashed_password=user_entity.hashed_password,
                refresh_token=user_entity.refresh_token
            )
        except DataNotFoundException as e:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details(e.message)
            return user_service_pb2.GetUserResponse()
        except Exception as e:
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details(str(e))
            return user_service_pb2.GetUserResponse()
    
    async def UpdateUser(self, request, context: ServicerContext):
        try:
            updated_user = await self.user_usecases.update_user(
                request.id,
                hashed_password=request.hashed_password if request.HasField('hashed_password') else None,
                refresh_token=request.refresh_token if request.HasField('refresh_token') else None
            )
            return user_service_pb2.UpdateUserResponse(id=updated_user.id, email=updated_user.email)
        except DataNotFoundException as e:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details(e.message)
            return user_service_pb2.GetUserResponse()
        except Exception as e:
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details(str(e))
            return user_service_pb2.GetUserResponse()
    
    async def CreateUser(self, request, context: ServicerContext):
        try:
            new_user = await self.user_usecases.create_user(
                email=request.email,
                hashed_password=request.hashed_password,
            )
            return user_service_pb2.CreateUserResponse(id=new_user.id, email=new_user.email)
        except UserAlreadyExistsException as e:
            context.set_code(grpc.StatusCode.ALREADY_EXISTS)
            context.set_details(e.message)
            return user_service_pb2.GetUserResponse()
        except Exception as e:
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details(str(e))
            return user_service_pb2.GetUserResponse()
    
    async def DeleteUser(self, request, context: ServicerContext):
        try:
            success = await self.user_usecases.delete_user_by_id(id=request.id)
            return user_service_pb2.DeleteUserResponse(success=success) 
        except DataNotFoundException as e:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details(e.message)
            return user_service_pb2.DeleteUserResponse()
        except Exception as e:
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details(str(e))
            return user_service_pb2.DeleteUserResponse()