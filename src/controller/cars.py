from flask_smorest import Blueprint, abort
import sqlite3

from src.controller.shared_schemas import CarSchema
from src.controller.utils import empty_response
from src.model.car import Car
from src.model.journey_group import JourneyGroup

blp = Blueprint('cars', 'cars', url_prefix='/cars', description='Operations on cars')


@blp.route('', methods=['PUT'])
@blp.arguments(CarSchema(many=True), error_status_code=400)
@blp.response(200)
def load(data):
    try:
        Car.clear_table()
        JourneyGroup.clear_table()
        Car.insert_many(data)
    except sqlite3.Error as err:
        abort(400, message=str(err))
    return empty_response(200)
