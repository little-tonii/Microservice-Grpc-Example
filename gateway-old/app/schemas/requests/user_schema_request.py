from pydantic import BaseModel, field_validator
from email_validator import validate_email, EmailNotValidError

class UserRegisterRequest(BaseModel):
    email: str
    password: str
    
    @field_validator("email")
    @classmethod
    def validate_email(cls, value: str):
        if not value.strip():
            raise ValueError("Mật khẩu không được để trống")
        try:
            email_infor = validate_email(value, check_deliverability=True)
            return email_infor.normalized
        except EmailNotValidError:
            raise ValueError(f"Email {value} không hợp lệ")
    
    @field_validator("password")
    @classmethod
    def validate_password(cls, value: str):
        if not value.strip():
            raise ValueError("Mật khẩu không được để trống")
        if len(value) < 6:
            raise ValueError("Mật khẩu phải có ít nhất 6 ký tự")
        return value
class UserLoginRequest(BaseModel):
    email: str
    password: str 
    
    @field_validator("email")
    @classmethod
    def validate_email(cls, value):
        try:
            email_infor = validate_email(value, check_deliverability=True)
            return email_infor.normalized
        except EmailNotValidError:
            raise ValueError(f"Email {value} không hợp lệ")