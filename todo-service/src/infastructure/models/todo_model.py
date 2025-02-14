from sqlalchemy import Boolean, Column, Integer, String
from src.infastructure.config.database import BaseModel


class TodoModel(BaseModel):
    __tablename__ = "todos"
    
    id: int = Column(Integer, primary_key=True, index=True)
    title: str = Column(String, nullable=False)
    description: str = Column(String, nullable=False)
    completed: bool = Column(Boolean, default=False, nullable=False)