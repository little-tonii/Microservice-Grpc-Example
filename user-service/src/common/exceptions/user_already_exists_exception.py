class UserAlreadyExistsException(Exception):
    message: str
    
    def __init__(self, email: str):
        self.message = f"Người dùng {email} đã tồn tại"
        super().__init__(self.message)