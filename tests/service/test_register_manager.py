from src.service.register_manager import RegisterManager
from src.model.car import Car
from src.model.journey_group import JourneyGroup


def test_register_dropoff_journey(app):
    """It should test the register/dropoff service"""
    with app.app_context():
        # insert two cars
        car1 = Car(**{'id': 1, 'seats': 4})
        car1.insert(commit=True)
        car2 = Car(**{'id': 2, 'seats': 5})
        car2.insert(commit=True)

        # register a group that fits in the second car
        group = JourneyGroup(**{'id': 1, 'people': 5})
        assigned_car = RegisterManager.register_journey(group)
        assert assigned_car.id == car2.id
        assert group.car_id == car2.id
        assert group.registered is not None
        assert group.created < group.registered
        assert group.drop_off is None
        assert assigned_car.available == 0

        # dropoff group with no other groups on-wait
        drop_off_car, new_group = RegisterManager.dropoff_journey(group)
        assert new_group is None
        assert drop_off_car.id == car2.id
        assert drop_off_car.available == drop_off_car.seats
        assert drop_off_car.seats == 5
        assert group.car_id is None
        assert group.registered is not None
        assert group.drop_off is not None
        assert group.registered < group.drop_off


def test_register_dropoff_journey_with_wait(app):
    """It should test the register/drop-off service with waiting groups"""
    with app.app_context():
        # insert two cars
        car1 = Car(**{'id': 1, 'seats': 4})
        car1.insert(commit=True)
        car2 = Car(**{'id': 2, 'seats': 5})
        car2.insert(commit=True)

        # register a group that fits in the second car
        group1 = JourneyGroup(**{'id': 1, 'people': 5})
        group1.insert(commit=True)
        assigned_car = RegisterManager.register_journey(group1)
        assert assigned_car.id == car2.id
        assert group1.car_id == car2.id
        assert group1.registered is not None
        assert group1.created < group1.registered
        assert group1.drop_off is None
        assert assigned_car.available == 0

        # try to register a new group that should be on wait
        group2 = JourneyGroup(**{'id': 2, 'people': 5})
        group2.insert(commit=True)
        assigned_car = RegisterManager.register_journey(group2)
        assert assigned_car is None

        # try to drop-off the waiting group
        group2 = JourneyGroup.get_by_id(2)
        assert group2.registered is None
        assert group2.car_id is None
        assigned_car, _ = RegisterManager.dropoff_journey(group2)
        assert assigned_car is None

        # dropoff group with one group on-wait
        drop_off_car, new_group = RegisterManager.dropoff_journey(group1)
        assert new_group is not None
        assert drop_off_car.id == car2.id
        assert drop_off_car.available == 0
        assert drop_off_car.seats == 5
        assert group1.car_id is None
        assert group1.registered is not None
        assert group1.drop_off is not None
        assert new_group.id == 2
        assert new_group.registered is not None
        assert new_group.drop_off is None
