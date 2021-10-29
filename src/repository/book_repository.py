from src.entity.book import Book
from src.repository.base_repository import BaseRepository


class BookRepository(BaseRepository):
    def _get_insert_parameters(self):
        # TODO example
        # sql = f'insert into {self.get_table()} (id, seats, available, created) values (?, ?, ?, ?)'
        # return sql, (self.id, self.seats, self.available, self.created)
        pass

    @classmethod
    def get_table(cls):
        return 'Book'

    @classmethod
    def get_dataclass(cls):
        return Book
