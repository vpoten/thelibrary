from src.entity.author import Author
from src.repository.base_repository import BaseRepository


class AuthorRepository(BaseRepository):
    def _get_insert_parameters(self, author):
        return '(name, date_of_birth) values (?, ?)', (author.name, author.date_of_birth)

    def _get_update_parameters(self, author):
        return 'name=?, date_of_birth=?', (author.name, author.date_of_birth)

    @classmethod
    def get_table(cls):
        return 'Author'

    @classmethod
    def get_dataclass(cls):
        return Author
