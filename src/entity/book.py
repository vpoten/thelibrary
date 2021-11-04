from datetime import date, datetime
from dataclasses import dataclass, field
from typing import List

from src.entity.author import Author
from src.entity.category import Category


@dataclass
class Book:
    isbn: str
    title: str
    date_of_publication: date
    id: int = None
    created: datetime = None
