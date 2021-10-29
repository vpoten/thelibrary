from src.entity.author import Author
from src.repository.base_repository import BaseRepository


class AuthorRepository(BaseRepository):
    def _get_insert_parameters(self):
        # TODO
        pass

    @classmethod
    def get_table(cls):
        return 'Author'

    @classmethod
    def get_dataclass(cls):
        return Author
