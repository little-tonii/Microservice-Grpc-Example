
from dataclasses import dataclass


@dataclass
class UserEntity:
    id: int
    email: str
    hashed_password: str
    refresh_token: str