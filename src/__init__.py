from flask import Flask
from flask_smorest import Api

import config.flask_config as flask_config
import config.db_config as db_config
import src.db.manager_db as manager_db
from src.controller.author_controller import blp as author_blp
from src.controller.book_controller import blp as book_blp
from src.controller.category_controller import blp as category_blp


def create_app(test_config=None):
    # create the flask App
    app = Flask(flask_config.APP_NAME)

    # create the Api
    app.config.update(flask_config.OPENAPI_CONFIG)
    api = Api(app)

    # initialize DB manager
    if test_config is None:
        app.config.update(db_config.DB_CONFIG)
    else:
        app.config.update(test_config['DB_CONFIG'])
    manager_db.init_app(app)

    # register controllers
    api.register_blueprint(author_blp)
    api.register_blueprint(book_blp)
    api.register_blueprint(category_blp)

    # Health check endpoint
    @app.route("/status", methods=['GET'])
    def status():
        """
        Health check
        :return: '', 200
        """
        return '', 200

    return app
