from src.model.journey_group import JourneyGroup
from src.model.car import Car


class RegisterManager(object):

    @classmethod
    def register_journey(cls, group: JourneyGroup, car: Car = None):
        # look for an available car with enough room for the given group
        if car is None:
            car = Car.get_by_availability(group.people)

        if car is None or group.drop_off is not None:
            # no car available or already drop-off
            return None

        # assign group to Car
        car.update_availability(-group.people)
        group.register(car.id)

        # returns the car where the group is registered
        return car

    @classmethod
    def dropoff_journey(cls, group: JourneyGroup):
        if group.drop_off is not None:
            # already dropped off
            return None, None

        car_id = group.car_id

        if car_id is None:
            # the group stills on wait
            return None, None

        car = Car.get_by_id(car_id)
        # un-assign group to Car
        car.update_availability(group.people)
        group.dropoff()

        # register the first waiting group (in arrival order) that fits in the released car
        waiting_group = JourneyGroup.get_first_waiting(car.available)

        if waiting_group is not None:
            car = cls.register_journey(waiting_group, car=car)

        # return the dropped off car and the new registered group
        return car, waiting_group
