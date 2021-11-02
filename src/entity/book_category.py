from dataclasses import dataclass


@dataclass
class BookCategory:
    isbn: str
    category_id: int
