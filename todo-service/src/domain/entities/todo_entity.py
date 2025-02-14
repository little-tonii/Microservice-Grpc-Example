from dataclasses import dataclass
from typing import Optional


@dataclass
class TodoEntity:
    id: int
    title: str
    description: str
    completed: bool