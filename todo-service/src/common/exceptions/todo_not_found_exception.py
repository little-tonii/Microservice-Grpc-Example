class TodoNotFoundException(Exception):
    message: str
    
    def __init__(self, id: int):
        self.message = f"Không tìm thấy todo với id {id}"
        super().__init__(self.message)
        
    def __str__(self):
        return self.message