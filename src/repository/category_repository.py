from src.entity.category import Category
from src.repository.base_repository import BaseRepository
from src.repository.book_category_repository import BookCategoryRepository


class CategoryRepository(BaseRepository):
    def _get_insert_parameters(self, category):
        return '(name) values (?)', (category.name,)

    def _get_update_parameters(self, category):
        return 'name=?', (category.name,)

    @classmethod
    def get_table(cls):
        return 'Category'

    @classmethod
    def get_dataclass(cls):
        return Category

    def get_categories_by_isbn(self, isbn):
        book_categories = BookCategoryRepository(self.get_db()).get_book_categories(isbn=isbn)
        return [self.get_by_id(bc.category_id) for bc in book_categories]
