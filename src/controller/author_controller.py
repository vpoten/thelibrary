from flask.views import MethodView
from flask_smorest import Blueprint, abort
import sqlite3

from src.exception.item_not_found import ItemNotFoundError
from src.controller.shared_schemas import AuthorSchema, AuthorsQueryArgsSchema

blp = Blueprint('authors', 'authors', url_prefix='/api/authors', description='Operations on authors')


@blp.route("/")
class Authors(MethodView):
    @blp.arguments(AuthorsQueryArgsSchema, location="query")
    @blp.response(200, AuthorSchema(many=True))
    def get(self, args):
        """List Authors"""
        # TODO
        return []

    @blp.arguments(AuthorSchema)
    @blp.response(201, AuthorSchema)
    def post(self, new_data):
        """Add a new Author"""
        # TODO
        return None


@blp.route("/<int:author_id>")
class AuthorsById(MethodView):
    @blp.response(200, AuthorSchema)
    def get(self, author_id):
        """Get Author by ID"""
        try:
            # TODO
            pass
        except ItemNotFoundError:
            abort(404, message="Item not found.")
        return None

    @blp.arguments(AuthorSchema)
    @blp.response(200, AuthorSchema)
    def put(self, update_data, author_id):
        """Update existing Author"""
        try:
            # TODO
            pass
        except ItemNotFoundError:
            abort(404, message="Item not found.")
        # TODO
        return None

    @blp.response(204)
    def delete(self, author_id):
        """Delete Author"""
        try:
            # TODO
            pass
        except ItemNotFoundError:
            abort(404, message="Item not found.")
