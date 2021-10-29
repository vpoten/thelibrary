import pytest

from src import create_app
from src.db.manager_db import init_db


@pytest.fixture
def app():
    """
    Returns the flask app
    """

    test_config = {
        'TESTING': True,
        'DB_CONFIG': {
            'DATABASE': ':memory:'
        }
    }

    app = create_app(test_config)

    with app.app_context():
        init_db()
    return app


@pytest.fixture
def client():
    """
    Returns the flask client for blueprint testing
    :return:
    """

    test_config = {
        'TESTING': True,
        'DB_CONFIG': {
            'DATABASE': ':memory:'
        }
    }

    app = create_app(test_config)

    with app.test_client() as client:
        with app.app_context():
            init_db()
        return client
