API_BLUEPRINT = '/journey'
API_CAR_BLUEPRINT = '/cars'


def test_register_error(client, data_for_journey_error):
    """It should test the register endpoint with bad inputs"""
    for data in data_for_journey_error:
        res = client.post(API_BLUEPRINT, json=data)
        assert res.status_code == 400


def test_register_no_cars(client, data_for_journey):
    """It should test the register endpoint with no available cars"""
    for data in data_for_journey:
        res = client.post(API_BLUEPRINT, json=data)
        assert res.status_code == 202


def test_register(client, data_for_car_load, data_for_journey):
    """It should test the register endpoint with enough cars for every group"""
    res = client.put(API_CAR_BLUEPRINT, json=data_for_car_load)
    assert res.status_code == 200

    for data in data_for_journey:
        res = client.post(API_BLUEPRINT, json=data)
        assert res.status_code == 200
