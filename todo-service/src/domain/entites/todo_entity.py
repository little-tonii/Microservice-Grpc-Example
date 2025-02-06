from dataclasses import dataclass
from typing import Optional

@dataclass
class TodoEntity:
    id: Optional[int] = None
    title: str = ""
    description: str = ""
    completed: bool = False