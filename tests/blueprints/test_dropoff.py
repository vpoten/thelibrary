import random as rd

API_BLUEPRINT = '/dropoff'
API_JOURNEY_BLUEPRINT = '/journey'
API_CAR_BLUEPRINT = '/cars'


def test_drop_off_empty(client):
    """It should test the drop-off endpoint with no groups"""
    res = client.post(API_BLUEPRINT, data={'ID': 1})
    assert res.status_code == 404


def test_drop_off_error(client):
    """It should test the drop-off endpoint with bad input"""
    res = client.post(API_BLUEPRINT, data={'field': 1})
    assert res.status_code == 400

    res = client.post(API_BLUEPRINT, data={})
    assert res.status_code == 400


def test_drop_off_no_cars(client, data_for_journey):
    """It should test the drop-off endpoint with no available cars"""
    for data in data_for_journey:
        # register with no cars available
        res = client.post(API_JOURNEY_BLUEPRINT, json=data)
        assert res.status_code == 202

        # locate and get the 204 code corresponding for waiting
        res = client.post(API_BLUEPRINT, data={'ID': data['id']})
        assert res.status_code == 204


def test_drop_off_with_cars(client, data_for_car_load, data_for_journey):
    """It should test the drop-off endpoint with available cars"""
    # load cars
    res = client.put(API_CAR_BLUEPRINT, json=data_for_car_load)
    assert res.status_code == 200

    for data in data_for_journey:
        # register with cars available for all groups
        res = client.post(API_JOURNEY_BLUEPRINT, json=data)
        assert res.status_code == 200

        # drop-off and get the 200 code corresponding with disassociation
        res = client.post(API_BLUEPRINT, data={'ID': data['id']})
        assert res.status_code == 200


# def test_drop_off_massive(client):
#     """It should test the drop-off endpoint with massive amount of car/groups"""
#     # load cars
#     cars = [{'id': i, 'seats': rd.randrange(4, 7, 1)} for i in range(1, 500)]
#
#     res = client.put(API_CAR_BLUEPRINT, json=cars)
#     assert res.status_code == 200
#
#     journeys = [{'id': i, 'people': rd.randrange(1, 6, 1)} for i in range(1, 5000)]
#     accepted = []
#     waiting = []
#
#     for data in journeys:
#         # register with cars available for all groups
#         res = client.post(API_JOURNEY_BLUEPRINT, json=data)
#         assert res.status_code in (200, 202)
#
#         if res.status_code == 200:
#             accepted.append(data)
#         else:
#             waiting.append(data)
#
#     for data in accepted:
#         # drop-off and get the 200 code corresponding with disassociation
#         res = client.post(API_BLUEPRINT, data={'ID': data['id']})
#         assert res.status_code == 200
