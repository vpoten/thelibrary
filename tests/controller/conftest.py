import pytest


def call_create_endpoint(client, url, data):
    return client.post(url, json=data)


@pytest.fixture()
def data_for_book():
    return {
        "date_of_publication": "2021-11-04",
        "title": "My book 1",
        "isbn": "123456"
    }


@pytest.fixture()
def data_for_author():
    return {
        "name": "John Doe",
        "date_of_birth": "1980-01-01"
    }


@pytest.fixture()
def data_for_category():
    return {
        "name": "Good category",
    }
