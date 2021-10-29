from flask_smorest import Blueprint

from src.controller.shared_schemas import GroupIdSchema, CarSchema
from src.controller.utils import empty_response
from src.model.car import Car
from src.model.journey_group import JourneyGroup

blp = Blueprint('locate', 'locate', url_prefix='/locate', description='Operations on locate')


@blp.route('', methods=['POST'])
@blp.arguments(GroupIdSchema, location='form', error_status_code=400)
@blp.response(200, schema=CarSchema)
def locate(data):
    journey_group = JourneyGroup.get_by_id(data['ID'])
    if journey_group is None:
        return empty_response(404)
    if journey_group.car_id is None:
        return empty_response(204)
    car = Car.get_by_id(journey_group.car_id)
    return {'id': car.id, 'seats': car.seats}
