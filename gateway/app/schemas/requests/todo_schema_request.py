from pydantic import BaseModel, field_validator, model_validator


class CreateTodoRequest(BaseModel):
    title: str
    description: str
    
    @field_validator("title")
    @classmethod
    def validate_title(cls, value: str):
        if not value.strip():
            raise ValueError("Tiêu đề không được để trống")
        return value
    
    @field_validator("description")
    @classmethod
    def validate_description(cls, value: str):
        if not value.strip():
            raise ValueError("Mô tả không được để trống")
        return value
    
    @model_validator(mode="before")
    @classmethod
    def check_missing_fields(cls, values):
        if not values:  # Kiểm tra nếu payload là {}
            raise ValueError("Dữ liệu đầu vào không được để trống")

        required_fields = ["title"]
        missing_fields = [field for field in required_fields if field not in values]

        if missing_fields:
            raise ValueError(f"Thiếu trường bắt buộc: {', '.join(missing_fields)}")

        return values
    
class UpdateTodoRequest(BaseModel):
    title: str
    description: str
    completed: bool
    
    @field_validator("title")
    @classmethod
    def validate_title(cls, value: str):
        if not value.strip():
            raise ValueError("Tiêu đề không được để trống")
        return value
    
    @field_validator("description")
    @classmethod
    def validate_description(cls, value: str):
        if not value.strip():
            raise ValueError("Mô tả không được để trống")
        return value
    
    @model_validator(mode="before")
    @classmethod
    def check_missing_fields(cls, values):
        if not values:  # Kiểm tra nếu payload là {}
            raise ValueError("Dữ liệu đầu vào không được để trống")

        required_fields = ["id, title, description, completed"]
        missing_fields = [field for field in required_fields if field not in values]

        if missing_fields:
            raise ValueError(f"Thiếu trường bắt buộc: {', '.join(missing_fields)}")

        return values
    
class GetTodoRequest(BaseModel):
    id: int
    
    @model_validator(mode="before")
    @classmethod
    def check_missing_fields(cls, values):
        if not values:  # Kiểm tra nếu payload là {}
            raise ValueError("Dữ liệu đầu vào không được để trống")

        required_fields = ["id"]
        missing_fields = [field for field in required_fields if field not in values]

        if missing_fields:
            raise ValueError(f"Thiếu trường bắt buộc: {', '.join(missing_fields)}")

        return values
    
class DeleteTodoRequest(BaseModel):
    id: int
    
    @model_validator(mode="before")
    @classmethod
    def check_missing_fields(cls, values):
        if not values:  # Kiểm tra nếu payload là {}
            raise ValueError("Dữ liệu đầu vào không được để trống")

        required_fields = ["id"]
        missing_fields = [field for field in required_fields if field not in values]

        if missing_fields:
            raise ValueError(f"Thiếu trường bắt buộc: {', '.join(missing_fields)}")

        return values