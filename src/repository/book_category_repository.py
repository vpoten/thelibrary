from src.entity.book_category import BookCategory
from src.repository.base_repository import BaseRepository


class BookCategoryRepository(BaseRepository):
    def _get_insert_parameters(self, book_category):
        return '(isbn, category_id) values (?, ?)', (book_category.isbn, book_category.category_id)

    def _get_update_parameters(self, book_category):
        raise NotImplementedError

    @classmethod
    def get_table(cls):
        return 'BookCategory'

    @classmethod
    def get_dataclass(cls):
        return BookCategory

    def get_id_field_name(self):
        raise NotImplementedError

    def get_book_categories(self, isbn, category_id=None):
        """
        Get the BookCategory list associated to the given isbn
        :param isbn:
        :param category_id:
        :return: list of BookCategory instances
        """
        search_fields = {'isbn': isbn, 'category_id': category_id}
        return self.filter_by_search_fields(search_fields)

    def delete(self, book_category):
        """
        Deletes a BookCategory relationship
        :param book_category:
        :return:
        """
        sql = f'delete from {self.get_table()} where isbn=? and category_id=?'
        self._execute(sql, (book_category.isbn, book_category.category_id))
