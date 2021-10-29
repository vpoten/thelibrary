from src.model.car import Car


API_BLUEPRINT = '/cars'


def test_load(client, data_for_car_load_error, data_for_car_load):
    """It should test the load endpoint"""
    res = client.put(API_BLUEPRINT, json={})
    assert res.status_code == 400

    res = client.put(API_BLUEPRINT, json=[])
    assert res.status_code == 200
    assert Car.count_rows() == 0

    res = client.put(API_BLUEPRINT, json=data_for_car_load_error)
    assert res.status_code == 400

    res = client.put(API_BLUEPRINT, json=data_for_car_load)
    assert res.status_code == 200
    assert Car.count_rows() == len(data_for_car_load)
    assert Car.get_by_id(data_for_car_load[0]['id']) is not None
    assert Car.get_by_id(1001) is None

    res = client.put(API_BLUEPRINT, json=[])
    assert res.status_code == 200
    assert Car.count_rows() == 0
