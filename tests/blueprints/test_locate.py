API_BLUEPRINT = '/locate'
API_JOURNEY_BLUEPRINT = '/journey'
API_CAR_BLUEPRINT = '/cars'


def test_locate_empty(client):
    """It should test the locate endpoint with no groups"""
    res = client.post(API_BLUEPRINT, data={'ID': 1})
    assert res.status_code == 404


def test_locate_errors(client):
    """It should test the locate endpoint with bad inputs"""
    res = client.post(API_BLUEPRINT, data={'field': 1})
    assert res.status_code == 400

    res = client.post(API_BLUEPRINT, data={})
    assert res.status_code == 400


def test_locate_no_cars(client, data_for_journey):
    """It should test the locate endpoint with no available cars"""
    for data in data_for_journey:
        # register with no cars available
        res = client.post(API_JOURNEY_BLUEPRINT, json=data)
        assert res.status_code == 202

        # locate and get the 204 code corresponding for waiting
        res = client.post(API_BLUEPRINT, data={'ID': data['id']})
        assert res.status_code == 204


def test_locate_with_cars(client, data_for_car_load, data_for_journey):
    """It should test the locate endpoint with available cars"""
    cars_associated = {car['id']: [] for car in data_for_car_load}
    cars_dict = {car['id']: car for car in data_for_car_load}

    # load cars
    res = client.put(API_CAR_BLUEPRINT, json=data_for_car_load)
    assert res.status_code == 200

    for data in data_for_journey:
        # register with cars available
        res = client.post(API_JOURNEY_BLUEPRINT, json=data)
        assert res.status_code == 200

        # locate and get the 200 code corresponding for assigned to car
        res = client.post(API_BLUEPRINT, data={'ID': data['id']})
        assert res.status_code == 200

        # keep track of car association
        cars_associated[res.json['id']].append(data)

    for car_id, groups in cars_associated.items():
        # check that car capacity is never exceeded
        assert cars_dict[car_id]['seats'] >= sum([g['people'] for g in groups])
