from flask.views import MethodView
from flask_smorest import Blueprint, abort

from src.exception.item_not_found import ItemNotFoundError
from src.exception.database_error import DatabaseError
from src.controller.shared_schemas import AuthorSchema, AuthorsQueryArgsSchema, BookSchema
from src.service.author_service import AuthorService
from src.service.book_service import BookService

blp = Blueprint('Authors', 'authors', url_prefix='/api/authors', description='Operations on authors')

author_service = AuthorService()
book_service = BookService()


@blp.route("/")
class Authors(MethodView):
    @blp.arguments(AuthorsQueryArgsSchema, location="query")
    @blp.response(200, AuthorSchema(many=True))
    def get(self, args):
        """List Authors"""
        return author_service.list(page=args.get('page'), rows_per_page=args.get('rows_per_page'),
                                   isbn=args.get('isbn'))

    @blp.arguments(AuthorSchema)
    @blp.response(201, AuthorSchema)
    def post(self, new_data):
        """Add a new Author"""
        try:
            return author_service.create(new_data)
        except DatabaseError as err:
            abort(400, message=str(err))


@blp.route("/<int:author_id>")
class AuthorsById(MethodView):
    @blp.response(200, AuthorSchema)
    def get(self, author_id):
        """Get Author by ID"""
        try:
            return author_service.retrieve(author_id)
        except ItemNotFoundError:
            abort(404, message="Item not found.")

    @blp.arguments(AuthorSchema)
    @blp.response(200, AuthorSchema)
    def put(self, update_data, author_id):
        """Update existing Author"""
        try:
            return author_service.update(author_id, update_data)
        except ItemNotFoundError:
            abort(404, message="Item not found.")
        except DatabaseError as err:
            abort(400, message=str(err))

    @blp.response(204)
    def delete(self, author_id):
        """Delete Author"""
        try:
            return author_service.delete(author_id)
        except ItemNotFoundError:
            abort(404, message="Item not found.")


@blp.route("/<int:author_id>/books", methods=['GET'])
@blp.response(200, BookSchema(many=True))
def get_books(author_id):
    """Get the books associated with a given author"""
    try:
        author = author_service.retrieve(author_id)
        return book_service.list(author=author)
    except ItemNotFoundError:
        abort(404, message="Item not found.")
