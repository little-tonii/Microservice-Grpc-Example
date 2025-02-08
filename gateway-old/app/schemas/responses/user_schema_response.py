from pydantic import BaseModel

class UserLoginResponse(BaseModel):
    refresh_token: str
    access_token: str
    token_type: str

class UserInforResponse(BaseModel):
    id: int
    email: str