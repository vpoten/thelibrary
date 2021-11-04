from copy import deepcopy
from tests.controller.conftest import call_create_endpoint

API_BLUEPRINT = '/api/books/'


def test_list(client, data_for_book):
    """It should test the list endpoint"""
    res = client.get(API_BLUEPRINT)
    assert res.status_code == 200
    assert len(res.json) == 0

    call_create_endpoint(client, API_BLUEPRINT, data_for_book)
    res = client.get(API_BLUEPRINT)
    assert res.status_code == 200
    assert len(res.json) == 1


def test_create(client, data_for_book):
    """It should test the create endpoint"""
    res = call_create_endpoint(client, API_BLUEPRINT, data_for_book)
    assert res.status_code == 201
    assert res.json['isbn'] == data_for_book['isbn']


def test_retrieve(client, data_for_book):
    """It should test the retrieve endpoint"""
    res = client.get(f'{API_BLUEPRINT}{data_for_book["isbn"]}')
    assert res.status_code == 404

    call_create_endpoint(client, API_BLUEPRINT, data_for_book)
    res = client.get(f'{API_BLUEPRINT}{data_for_book["isbn"]}')
    assert res.status_code == 200
    assert res.json['isbn'] == data_for_book['isbn']


def test_update(client, data_for_book):
    """It should test the update endpoint"""
    modified_data = deepcopy(data_for_book)
    modified_data['title'] = 'My new title'
    res = client.put(f'{API_BLUEPRINT}{data_for_book["isbn"]}', json=modified_data)
    assert res.status_code == 404

    call_create_endpoint(client, API_BLUEPRINT, data_for_book)
    res = client.put(f'{API_BLUEPRINT}{data_for_book["isbn"]}', json=modified_data)
    assert res.json['isbn'] == data_for_book['isbn']
    assert res.json['title'] == modified_data['title']


def test_delete(client, data_for_book):
    """It should test the delete endpoint"""
    res = client.delete(f'{API_BLUEPRINT}{data_for_book["isbn"]}')
    assert res.status_code == 404

    call_create_endpoint(client, API_BLUEPRINT, data_for_book)
    res = client.delete(f'{API_BLUEPRINT}{data_for_book["isbn"]}')
    assert res.status_code == 204
