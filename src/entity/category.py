from datetime import datetime
from dataclasses import dataclass


@dataclass
class Category:
    name: str
    id: int = None
    created: datetime = None
