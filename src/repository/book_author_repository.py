from src.entity.book_author import BookAuthor
from src.repository.base_repository import BaseRepository


class BookAuthorRepository(BaseRepository):
    def _get_insert_parameters(self, book_author):
        return '(isbn, author_id) values (?, ?)', (book_author.isbn, book_author.author_id)

    def _get_update_parameters(self, book_author):
        raise NotImplementedError

    @classmethod
    def get_table(cls):
        return 'BookAuthor'

    @classmethod
    def get_dataclass(cls):
        return BookAuthor

    def get_id_field_name(self):
        raise NotImplementedError

    def get_lastrowid_field_name(self):
        return None

    def get_book_authors(self, isbn, author_id=None):
        """
        Get the BookAuthor list associated to the given isbn
        :param isbn:
        :param author_id:
        :return: list of BookAuthor instances
        """
        search_fields = {'isbn': isbn, 'author_id': author_id}
        return self.filter_by_search_fields(search_fields)

    def delete(self, book_author, commit=True):
        """
        Deletes a BookAuthor relationship
        :param commit:
        :param book_author:
        :return:
        """
        search_fields = {'isbn': book_author.isbn, 'author_id': book_author.author_id}
        self.delete_by_search_fields(search_fields, commit=commit)
