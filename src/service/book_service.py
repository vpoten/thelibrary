from src.entity.author import Author
from src.entity.book import Book
from src.entity.book_author import BookAuthor
from src.entity.book_category import BookCategory
from src.entity.category import Category
from src.repository.book_author_repository import BookAuthorRepository
from src.repository.book_category_repository import BookCategoryRepository
from src.repository.book_repository import BookRepository
from src.service.base_service import BaseService


class BookService(BaseService):
    def __init__(self):
        super().__init__(BookRepository())

    def add_author(self, book: Book, author: Author):
        """
        Associate an author with a book
        :param book:
        :param author:
        :return:
        """
        book_authors = BookAuthorRepository(self.repository.get_db())
        book_authors.insert(BookAuthor(isbn=book.isbn, author_id=author.id), True)

    def add_category(self, book: Book, category: Category):
        """
        Associate a category with a book
        :param book:
        :param category:
        :return:
        """
        book_categories = BookCategoryRepository(self.repository.get_db())
        book_categories.insert(BookCategory(isbn=book.isbn, category_id=category.id), True)
