from flask.views import MethodView
from flask_smorest import Blueprint, abort

from src.exception.item_not_found import ItemNotFoundError
from src.controller.shared_schemas import BookSchema, BooksQueryArgsSchema, AuthorSchema, CategorySchema
from src.repository.book_repository import BookRepository
from src.service.book_service import BookService

blp = Blueprint('books', 'books', url_prefix='/api/books', description='Operations on books')


@blp.route("/")
class Books(MethodView):
    service = BookService(BookRepository())

    @blp.arguments(BooksQueryArgsSchema, location="query")
    @blp.response(200, BookSchema(many=True))
    def get(self, args):
        """List Books"""
        return self.service.list(args.get('page'), args.get('rows_per_page'))

    @blp.arguments(BookSchema)
    @blp.response(201, BookSchema)
    def post(self, new_data):
        """Add a new Book"""
        return self.service.create(new_data)


@blp.route("/<isbn>")
class BooksById(MethodView):
    service = BookService(BookRepository())

    @blp.response(200, BookSchema)
    def get(self, isbn):
        """Get Book by ID"""
        try:
            return self.service.retrieve(isbn)
        except ItemNotFoundError:
            abort(404, message="Item not found.")

    @blp.arguments(BookSchema)
    @blp.response(200, BookSchema)
    def put(self, update_data, isbn):
        """Update existing Book"""
        try:
            return self.service.update(isbn, update_data)
        except ItemNotFoundError:
            abort(404, message="Item not found.")

    @blp.response(204)
    def delete(self, isbn):
        """Delete Book"""
        try:
            return self.service.delete(isbn)
        except ItemNotFoundError:
            abort(404, message="Item not found.")


@blp.route("/<isbn>/categories")
class BooksCategories(MethodView):
    @blp.response(200, AuthorSchema(many=True))
    def get(self, isbn):
        """Get Book categories"""
        try:
            pass
        except ItemNotFoundError:
            abort(404, message="Item not found.")

    @blp.arguments(AuthorSchema)
    @blp.response(201, AuthorSchema)
    def post(self, new_data):
        try:
            pass
        except ItemNotFoundError:
            abort(404, message="Item not found.")


@blp.route("/<isbn>/authors")
class BooksAuthors(MethodView):
    @blp.response(200, CategorySchema(many=True))
    def get(self, isbn):
        """Get Book authors"""
        try:
            pass
        except ItemNotFoundError:
            abort(404, message="Item not found.")

    @blp.arguments(CategorySchema)
    @blp.response(201, CategorySchema)
    def post(self, new_data):
        try:
            pass
        except ItemNotFoundError:
            abort(404, message="Item not found.")
