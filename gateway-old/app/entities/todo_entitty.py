
from dataclasses import dataclass
from typing import Optional


@dataclass
class TodoEntity:
    id: Optional[int]
    title: str
    description: str
    completed: bool = False