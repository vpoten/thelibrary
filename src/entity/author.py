from datetime import date, datetime
from dataclasses import dataclass


@dataclass
class Author:
    name: str
    date_of_birth: date
    id: int = None
    created: datetime = None
