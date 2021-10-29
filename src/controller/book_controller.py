from flask.views import MethodView
from flask_smorest import Blueprint, abort
import sqlite3

from src.exception.item_not_found import ItemNotFoundError
from src.controller.shared_schemas import BookSchema, BookQueryArgsSchema

blp = Blueprint('books', 'books', url_prefix='/api/books', description='Operations on books')


@blp.route("/")
class Books(MethodView):
    @blp.arguments(BookQueryArgsSchema, location="query")
    @blp.response(200, BookSchema(many=True))
    def get(self, args):
        """List Books"""
        # TODO
        return []

    @blp.arguments(BookSchema)
    @blp.response(201, BookSchema)
    def post(self, new_data):
        """Add a new Book"""
        # TODO
        return None


@blp.route("/<isbn>")
class BooksById(MethodView):
    @blp.response(200, BookSchema)
    def get(self, isbn):
        """Get Book by ID"""
        try:
            # TODO
            pass
        except ItemNotFoundError:
            abort(404, message="Item not found.")
        return None

    @blp.arguments(BookSchema)
    @blp.response(200, BookSchema)
    def put(self, update_data, isbn):
        """Update existing Book"""
        try:
            # TODO
            pass
        except ItemNotFoundError:
            abort(404, message="Item not found.")
        # TODO
        return None

    @blp.response(204)
    def delete(self, isbn):
        """Delete Book"""
        try:
            # TODO
            pass
        except ItemNotFoundError:
            abort(404, message="Item not found.")
