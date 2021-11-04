from copy import deepcopy
from tests.controller.conftest import call_create_endpoint

API_BLUEPRINT = '/api/categories/'


def test_list(client, data_for_category):
    """It should test the list endpoint"""
    res = client.get(API_BLUEPRINT)
    assert res.status_code == 200
    assert len(res.json) == 0

    call_create_endpoint(client, API_BLUEPRINT, data_for_category)
    res = client.get(API_BLUEPRINT)
    assert res.status_code == 200
    assert len(res.json) == 1


def test_create(client, data_for_category):
    """It should test the create endpoint"""
    res = call_create_endpoint(client, API_BLUEPRINT, data_for_category)
    assert res.status_code == 201
    assert res.json['id'] > 0
    assert res.json['name'] == data_for_category['name']


def test_retrieve(client, data_for_category):
    """It should test the retrieve endpoint"""
    res = client.get(f'{API_BLUEPRINT}1')
    assert res.status_code == 404

    data_id = call_create_endpoint(client, API_BLUEPRINT, data_for_category).json['id']
    res = client.get(f'{API_BLUEPRINT}{data_id}')
    assert res.status_code == 200
    assert res.json['id'] == data_id


def test_update(client, data_for_category):
    """It should test the update endpoint"""
    modified_data = deepcopy(data_for_category)
    modified_data['name'] = 'Category2'
    res = client.put(f'{API_BLUEPRINT}1', json=modified_data)
    assert res.status_code == 404

    data_id = call_create_endpoint(client, API_BLUEPRINT, data_for_category).json['id']
    res = client.put(f'{API_BLUEPRINT}{data_id}', json=modified_data)
    assert res.json['id'] == data_id
    assert res.json['name'] == modified_data['name']


def test_delete(client, data_for_category):
    """It should test the delete endpoint"""
    res = client.delete(f'{API_BLUEPRINT}1')
    assert res.status_code == 404

    data_id = call_create_endpoint(client, API_BLUEPRINT, data_for_category).json['id']
    res = client.delete(f'{API_BLUEPRINT}{data_id}')
    assert res.status_code == 204


def test_get_books(client, data_for_category):
    """It should test the get books endpoint"""
    data_id = call_create_endpoint(client, API_BLUEPRINT, data_for_category).json['id']

    res = client.get(f'{API_BLUEPRINT}{data_id}/books')
    assert res.status_code == 200
    assert len(res.json) == 0
