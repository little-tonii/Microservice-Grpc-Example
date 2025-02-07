from sqlalchemy import Boolean, Column, Integer, String
from data.datasource.todo_database import Base


class TodoModel(Base):
    __tablename__ = "todos"
    
    id=Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    completed = Column(Boolean, default=False)