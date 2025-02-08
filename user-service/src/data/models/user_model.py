from sqlalchemy import Column, Integer, String
from src.data.datasource.database import BaseModel


class UserModel(BaseModel):
    __tablename__ = "users"
    
    id: int =  Column(Integer, primary_key=True, index=True)
    email: str = Column(String, unique=True, index=True)
    hashed_password = Column(String, nullable=False)
    refresh_token = Column(String, nullable=True)