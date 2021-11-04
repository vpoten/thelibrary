from flask.views import MethodView
from flask_smorest import Blueprint, abort

from src.exception.database_error import DatabaseError
from src.exception.item_not_found import ItemNotFoundError
from src.controller.shared_schemas import BookSchema, BooksQueryArgsSchema, AuthorSchema, CategorySchema
from src.service.book_service import BookService
from src.service.category_service import CategoryService
from src.service.author_service import AuthorService

blp = Blueprint('Books', 'books', url_prefix='/api/books', description='Operations on books')

book_service = BookService()
category_service = CategoryService()
author_service = AuthorService()


@blp.route("/")
class Books(MethodView):
    @blp.arguments(BooksQueryArgsSchema, location="query")
    @blp.response(200, BookSchema(many=True))
    def get(self, args):
        """List Books"""
        return book_service.list(args.get('page'), args.get('rows_per_page'))

    @blp.arguments(BookSchema)
    @blp.response(201, BookSchema)
    def post(self, new_data):
        """Add a new Book"""
        try:
            return book_service.create(new_data)
        except DatabaseError as err:
            abort(400, message=str(err))


@blp.route("/<isbn>")
class BooksById(MethodView):
    @blp.response(200, BookSchema)
    def get(self, isbn):
        """Get Book by ID"""
        try:
            return book_service.retrieve(isbn)
        except ItemNotFoundError:
            abort(404, message="Item not found.")

    @blp.arguments(BookSchema)
    @blp.response(200, BookSchema)
    def put(self, update_data, isbn):
        """Update existing Book"""
        try:
            return book_service.update(isbn, update_data)
        except ItemNotFoundError:
            abort(404, message="Item not found.")
        except DatabaseError as err:
            abort(400, message=str(err))

    @blp.response(204)
    def delete(self, isbn):
        """Delete Book"""
        try:
            return book_service.delete(isbn)
        except ItemNotFoundError:
            abort(404, message="Item not found.")


@blp.route("/<isbn>/categories", methods=['GET'])
@blp.response(200, CategorySchema(many=True))
def get_categories(isbn):
    """Get Book categories"""
    try:
        book = book_service.retrieve(isbn)
        return category_service.list(isbn=book.isbn)
    except ItemNotFoundError:
        abort(404, message="Item not found.")


@blp.route("/<isbn>/categories/<int:category_id>", methods=['POST'])
@blp.response(201, CategorySchema)
def add_category(isbn, category_id):
    """Associate category to Book"""
    try:
        book = book_service.retrieve(isbn)
        category = category_service.retrieve(category_id)
        book_service.add_category(book, category)
        return category
    except ItemNotFoundError:
        abort(404, message="Item not found.")
    except DatabaseError as err:
        abort(400, message=str(err))


@blp.route("/<isbn>/authors", methods=['GET'])
@blp.response(200, AuthorSchema(many=True))
def get_authors(isbn):
    """Get Book authors"""
    try:
        book = book_service.retrieve(isbn)
        return author_service.list(isbn=book.isbn)
    except ItemNotFoundError:
        abort(404, message="Item not found.")


@blp.route("/<isbn>/authors/<int:author_id>", methods=['POST'])
@blp.response(201, AuthorSchema)
def add_author(isbn, author_id):
    """Add author to Book"""
    try:
        book = book_service.retrieve(isbn)
        author = author_service.retrieve(author_id)
        book_service.add_author(book, author)
        return author
    except ItemNotFoundError:
        abort(404, message="Item not found.")
    except DatabaseError as err:
        abort(400, message=str(err))
