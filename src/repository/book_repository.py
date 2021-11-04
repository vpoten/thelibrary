from src.entity.book import Book
from src.repository.base_repository import BaseRepository
from src.repository.book_author_repository import BookAuthorRepository
from src.repository.book_category_repository import BookCategoryRepository


class BookRepository(BaseRepository):
    def _get_insert_parameters(self, book):
        return '(isbn, title, date_of_publication) values (?, ?, ?)', (book.isbn, book.title, book.date_of_publication)

    def _get_update_parameters(self, book):
        return 'title=?, date_of_publication=?', (book.title, book.date_of_publication)

    @classmethod
    def get_table(cls):
        return 'Book'

    @classmethod
    def get_dataclass(cls):
        return Book

    def get_id_field_name(self):
        return 'isbn'

    def get_books_by_category_id(self, category_id):
        book_categories = BookCategoryRepository(self.get_db()).get_book_categories(None, category_id=category_id)
        return [self.get_by_id(bc.isbn) for bc in book_categories]

    def get_books_by_author_id(self, author_id):
        book_authors = BookAuthorRepository(self.get_db()).get_book_authors(None, author_id=author_id)
        return [self.get_by_id(ba.isbn) for ba in book_authors]
