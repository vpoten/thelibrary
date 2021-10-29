import sqlite3
from flask_smorest import Blueprint, abort

from src.controller.shared_schemas import GroupIdSchema
from src.controller.utils import empty_response
from src.model.journey_group import JourneyGroup
from src.service.register_manager import RegisterManager

blp = Blueprint('dropoff', 'dropoff', url_prefix='/dropoff', description='Operations on dropoff')


@blp.route('', methods=['POST'])
@blp.arguments(GroupIdSchema, location='form', error_status_code=400)
@blp.response(200)
def drop_off(data):
    journey_group = JourneyGroup.get_by_id(data['ID'])
    if journey_group is None:
        abort(404, message='Not found')
    try:
        car, _ = RegisterManager.dropoff_journey(journey_group)
        if car is None:
            return empty_response(204)
    except sqlite3.Error as err:
        abort(400, message=str(err))
    return empty_response(200)
