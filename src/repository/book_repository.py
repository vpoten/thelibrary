from src.entity.book import Book
from src.repository.base_repository import BaseRepository


class BookRepository(BaseRepository):
    def _get_insert_parameters(self, book):
        sql = f'insert into {self.get_table()} (isbn, title, date_of_publication) values (?, ?, ?)'
        return sql, (book.isbn, book.title, book.date_of_publication)

    @classmethod
    def get_table(cls):
        return 'Book'

    @classmethod
    def get_dataclass(cls):
        return Book

    def get_id_field_name(self):
        return 'isbn'
