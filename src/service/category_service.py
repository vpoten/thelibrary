from src.repository.category_repository import CategoryRepository
from src.service.base_service import BaseService


class CategoryService(BaseService):
    def __init__(self, repository: CategoryRepository):
        super().__init__(repository)

    def list(self, page=0, rows_per_page=100, isbn=None):
        if isbn is not None:
            return self.repository.get_categories_by_isbn(isbn)
        return self.repository.list(page=page, rows_per_page=rows_per_page)
