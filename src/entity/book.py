from datetime import date
from dataclasses import dataclass, field
from typing import List

from src.entity.author import Author
from src.entity.category import Category


@dataclass
class Book:
    isbn: str
    title: str
    date_of_publication: date
    authors: List[Author] = field(default_factory=list)
    categories: List[Category] = field(default_factory=list)
