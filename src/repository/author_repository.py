from src.entity.author import Author
from src.repository.base_repository import BaseRepository


class AuthorRepository(BaseRepository):
    def _get_insert_parameters(self, author):
        sql = f'insert into {self.get_table()} (name, date_of_birth) values (?, ?)'
        return sql, (author.name, author.date_of_birth)

    @classmethod
    def get_table(cls):
        return 'Author'

    @classmethod
    def get_dataclass(cls):
        return Author
