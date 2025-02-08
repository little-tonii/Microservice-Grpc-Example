from typing import Annotated
from fastapi import Depends

class UserRepository:
    
    def __init__(self):
        pass
        
    def create_user(self, email: str, hased_password: str):
        pass
        
    def find_user_by_email(self, email: str):
        pass
    
    def find_user_by_id(self, id: int):
        pass
    
    def update_user(self):
        pass
        