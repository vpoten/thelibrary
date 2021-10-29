from flask_smorest import Blueprint, abort
import sqlite3

from src.controller.shared_schemas import GroupSchema
from src.controller.utils import empty_response
from src.model.journey_group import JourneyGroup
from src.service.register_manager import RegisterManager

blp = Blueprint('journey', 'journey', url_prefix='/journey', description='Operations on journey')


@blp.route('', methods=['POST'])
@blp.arguments(GroupSchema, error_status_code=400)
@blp.response(200)
def register(data):
    journey_group = JourneyGroup(**data)
    try:
        journey_group.insert(commit=True)
        car = RegisterManager.register_journey(journey_group)
        if car is None:
            return empty_response(202)
    except sqlite3.Error as err:
        abort(400, message=str(err))
    return empty_response(200)
