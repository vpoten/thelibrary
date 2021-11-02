from flask.views import MethodView
from flask_smorest import Blueprint, abort

from src.exception.item_not_found import ItemNotFoundError
from src.controller.shared_schemas import CategorySchema, CategoriesQueryArgsSchema
from src.repository.category_repository import CategoryRepository
from src.service.base_service import BaseService
from src.service.category_service import CategoryService

blp = Blueprint('categories', 'categories', url_prefix='/api/categories', description='Operations on categories')


@blp.route("/")
class Categories(MethodView):
    service = CategoryService(CategoryRepository())

    @blp.arguments(CategoriesQueryArgsSchema, location="query")
    @blp.response(200, CategorySchema(many=True))
    def get(self, args):
        """List Categories"""
        return self.service.list(page=args.get('page'), rows_per_page=args.get('rows_per_page'), isbn=args.get('isbn'))

    @blp.arguments(CategorySchema)
    @blp.response(201, CategorySchema)
    def post(self, new_data):
        """Add a new Category"""
        return self.service.create(new_data)


@blp.route("/<int:category_id>")
class CategoriesById(MethodView):
    service = BaseService(CategoryRepository())

    @blp.response(200, CategorySchema)
    def get(self, category_id):
        """Get Category by ID"""
        try:
            return self.service.retrieve(category_id)
        except ItemNotFoundError:
            abort(404, message="Item not found.")

    @blp.arguments(CategorySchema)
    @blp.response(200, CategorySchema)
    def put(self, update_data, category_id):
        """Update existing Category"""
        try:
            return self.service.update(category_id, update_data)
        except ItemNotFoundError:
            abort(404, message="Item not found.")

    @blp.response(204)
    def delete(self, category_id):
        """Delete Category"""
        try:
            return self.service.delete(category_id)
        except ItemNotFoundError:
            abort(404, message="Item not found.")
