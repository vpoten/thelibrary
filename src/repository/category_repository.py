from src.entity.category import Category
from src.repository.base_repository import BaseRepository


class CategoryRepository(BaseRepository):
    def _get_insert_parameters(self):
        # TODO
        pass

    @classmethod
    def get_table(cls):
        return 'Category'

    @classmethod
    def get_dataclass(cls):
        return Category
