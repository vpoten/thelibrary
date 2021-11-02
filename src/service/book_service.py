from src.repository.book_repository import BookRepository
from src.service.base_service import BaseService


class BookService(BaseService):
    def __init__(self, repository: BookRepository):
        super().__init__(repository)

    def create(self, data):
        super().create(data)
        # TODO
        pass

    def update(self, item_id, data):
        super().update(item_id, data)
        # TODO
        pass
