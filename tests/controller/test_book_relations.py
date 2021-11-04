from copy import deepcopy
from tests.controller.conftest import call_create_endpoint

BOOKS_BLUEPRINT = '/api/books/'
AUTHORS_BLUEPRINT = '/api/authors/'
CATEGORIES_BLUEPRINT = '/api/categories/'


def test_book_with_author_and_category(client, data_for_book, data_for_author, data_for_category):
    """It should test the relationship among books, author and category"""
    book_id = call_create_endpoint(client, BOOKS_BLUEPRINT, data_for_book).json['isbn']
    author_id = call_create_endpoint(client, AUTHORS_BLUEPRINT, data_for_author).json['id']
    category_id = call_create_endpoint(client, CATEGORIES_BLUEPRINT, data_for_category).json['id']

    # no entities associated with the book
    res = client.get(f'{BOOKS_BLUEPRINT}{book_id}/categories')
    assert res.status_code == 200
    assert len(res.json) == 0

    res = client.get(f'{BOOKS_BLUEPRINT}{book_id}/authors')
    assert res.status_code == 200
    assert len(res.json) == 0

    # associate entities
    res = client.post(f'{BOOKS_BLUEPRINT}{book_id}/categories/{category_id}')
    assert res.status_code == 201
    assert res.json['id'] == category_id

    res = client.post(f'{BOOKS_BLUEPRINT}{book_id}/authors/{author_id}')
    assert res.status_code == 201
    assert res.json['id'] == author_id

    # there are entities associated with the book
    res = client.get(f'{BOOKS_BLUEPRINT}{book_id}/categories')
    assert res.status_code == 200
    assert len(res.json) == 1

    res = client.get(f'{BOOKS_BLUEPRINT}{book_id}/authors')
    assert res.status_code == 200
    assert len(res.json) == 1
