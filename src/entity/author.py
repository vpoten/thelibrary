from datetime import date
from dataclasses import dataclass


@dataclass
class Author:
    id: int
    name: str
    date_of_birth: date
