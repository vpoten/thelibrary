from flask.views import MethodView
from flask_smorest import Blueprint, abort

import sqlite3

from src.exception.item_not_found import ItemNotFoundError
from src.controller.shared_schemas import CategorySchema, CategoriesQueryArgsSchema

blp = Blueprint('categories', 'categories', url_prefix='/api/categories', description='Operations on categories')


@blp.route("/")
class Categories(MethodView):
    @blp.arguments(CategoriesQueryArgsSchema, location="query")
    @blp.response(200, CategorySchema(many=True))
    def get(self, args):
        """List Categories"""
        # TODO
        return []

    @blp.arguments(CategorySchema)
    @blp.response(201, CategorySchema)
    def post(self, new_data):
        """Add a new Category"""
        # TODO
        return None


@blp.route("/<int:category_id>")
class CategoriesById(MethodView):
    @blp.response(200, CategorySchema)
    def get(self, category_id):
        """Get Category by ID"""
        try:
            # TODO
            pass
        except ItemNotFoundError:
            abort(404, message="Item not found.")
        return None

    @blp.arguments(CategorySchema)
    @blp.response(200, CategorySchema)
    def put(self, update_data, category_id):
        """Update existing Category"""
        try:
            # TODO
            pass
        except ItemNotFoundError:
            abort(404, message="Item not found.")
        # TODO
        return None

    @blp.response(204)
    def delete(self, category_id):
        """Delete Category"""
        try:
            # TODO
            pass
        except ItemNotFoundError:
            abort(404, message="Item not found.")
