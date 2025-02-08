from dataclasses import dataclass
from typing import Optional

@dataclass
class UserEntity:
    id: Optional[int] = None
    email: str = ""
    hashed_password: str = ""
    refresh_token: Optional[str] = None