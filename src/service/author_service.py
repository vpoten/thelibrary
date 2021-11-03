from src.repository.author_repository import AuthorRepository
from src.service.base_service import BaseService


class AuthorService(BaseService):
    def __init__(self):
        super().__init__(AuthorRepository())

    def list(self, page=0, rows_per_page=100, isbn=None):
        if isbn is not None:
            return self.repository.get_authors_by_isbn(isbn)
        return self.repository.list(page=page, rows_per_page=rows_per_page)
