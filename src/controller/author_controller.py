from flask.views import MethodView
from flask_smorest import Blueprint, abort

from src.exception.item_not_found import ItemNotFoundError
from src.controller.shared_schemas import AuthorSchema, AuthorsQueryArgsSchema
from src.service.author_service import AuthorService

blp = Blueprint('authors', 'authors', url_prefix='/api/authors', description='Operations on authors')


@blp.route("/")
class Authors(MethodView):
    service = AuthorService()

    @blp.arguments(AuthorsQueryArgsSchema, location="query")
    @blp.response(200, AuthorSchema(many=True))
    def get(self, args):
        """List Authors"""
        return self.service.list(page=args.get('page'), rows_per_page=args.get('rows_per_page'), isbn=args.get('isbn'))

    @blp.arguments(AuthorSchema)
    @blp.response(201, AuthorSchema)
    def post(self, new_data):
        """Add a new Author"""
        return self.service.create(new_data)


@blp.route("/<int:author_id>")
class AuthorsById(MethodView):
    service = AuthorService()

    @blp.response(200, AuthorSchema)
    def get(self, author_id):
        """Get Author by ID"""
        try:
            return self.service.retrieve(author_id)
        except ItemNotFoundError:
            abort(404, message="Item not found.")

    @blp.arguments(AuthorSchema)
    @blp.response(200, AuthorSchema)
    def put(self, update_data, author_id):
        """Update existing Author"""
        try:
            return self.service.update(author_id, update_data)
        except ItemNotFoundError:
            abort(404, message="Item not found.")

    @blp.response(204)
    def delete(self, author_id):
        """Delete Author"""
        try:
            return self.service.delete(author_id)
        except ItemNotFoundError:
            abort(404, message="Item not found.")
