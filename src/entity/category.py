from datetime import datetime
from dataclasses import dataclass


@dataclass
class Category:
    id: int
    name: str
    created: datetime
