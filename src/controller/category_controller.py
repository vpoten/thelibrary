from flask.views import MethodView
from flask_smorest import Blueprint, abort

from src.exception.database_error import DatabaseError
from src.exception.item_not_found import ItemNotFoundError
from src.controller.shared_schemas import CategorySchema, CategoriesQueryArgsSchema, BookSchema
from src.service.book_service import BookService
from src.service.category_service import CategoryService

blp = Blueprint('Categories', 'categories', url_prefix='/api/categories', description='Operations on categories')

category_service = CategoryService()
book_service = BookService()


@blp.route("/")
class Categories(MethodView):
    @blp.arguments(CategoriesQueryArgsSchema, location="query")
    @blp.response(200, CategorySchema(many=True))
    def get(self, args):
        """List Categories"""
        return category_service.list(page=args.get('page'), rows_per_page=args.get('rows_per_page'),
                                     isbn=args.get('isbn'))

    @blp.arguments(CategorySchema)
    @blp.response(201, CategorySchema)
    def post(self, new_data):
        """Add a new Category"""
        try:
            return category_service.create(new_data)
        except DatabaseError as err:
            abort(400, message=str(err))


@blp.route("/<int:category_id>")
class CategoriesById(MethodView):
    @blp.response(200, CategorySchema)
    def get(self, category_id):
        """Get Category by ID"""
        try:
            return category_service.retrieve(category_id)
        except ItemNotFoundError:
            abort(404, message="Item not found.")

    @blp.arguments(CategorySchema)
    @blp.response(200, CategorySchema)
    def put(self, update_data, category_id):
        """Update existing Category"""
        try:
            return category_service.update(category_id, update_data)
        except ItemNotFoundError:
            abort(404, message="Item not found.")
        except DatabaseError as err:
            abort(400, message=str(err))

    @blp.response(204)
    def delete(self, category_id):
        """Delete Category"""
        try:
            return category_service.delete(category_id)
        except ItemNotFoundError:
            abort(404, message="Item not found.")


@blp.route("/<int:category_id>/books", methods=['GET'])
@blp.response(200, BookSchema(many=True))
def get_books(category_id):
    """Get the books included in a given category"""
    try:
        category = category_service.retrieve(category_id)
        return book_service.list(category=category)
    except ItemNotFoundError:
        abort(404, message="Item not found.")
