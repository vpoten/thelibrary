import pytest


@pytest.fixture
def data_for_car_load():
    return [
        {'id': 1, 'seats': 4},
        {'id': 2, 'seats': 5},
        {'id': 3, 'seats': 4},
        {'id': 4, 'seats': 6},
    ]


@pytest.fixture
def data_for_car_load_error():
    return [
        {'id': 1, 'seats': 8},
        {'id': 2, 'bad-field': 5},
        {'id': 3, 'seats': 4}
    ]


@pytest.fixture
def data_for_journey():
    return [
        {"id": 1, "people": 4},
        {"id": 2, "people": 6},
        {"id": 3, "people": 1},
        {"id": 4, "people": 3},
    ]


@pytest.fixture
def data_for_journey_error():
    return [
        {"id": 5, "people": 0},
        {"id": 6, "people": -1},
        {"id": 7, "people": 7},
        {"id": 8, "people": 8},
    ]
