import pytest
import os
import tempfile

from src import create_app
from src.db.manager_db import init_db


@pytest.fixture
def app():
    """
    Returns the flask app
    """
    db_fd, db_path = tempfile.mkstemp()

    test_config = {
        'TESTING': True,
        'DB_CONFIG': {
            'DATABASE': db_path
        }
    }

    app = create_app(test_config)

    with app.app_context():
        init_db()
    yield app

    os.close(db_fd)
    os.unlink(db_path)


@pytest.fixture
def client():
    """
    Returns the flask client for blueprint testing
    :return:
    """
    db_fd, db_path = tempfile.mkstemp()

    test_config = {
        'TESTING': True,
        'DB_CONFIG': {
            'DATABASE': db_path
        }
    }

    app = create_app(test_config)

    with app.test_client() as client:
        with app.app_context():
            init_db()
        yield client

    os.close(db_fd)
    os.unlink(db_path)
