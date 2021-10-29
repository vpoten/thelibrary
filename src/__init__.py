from flask import Flask
from flask_smorest import Api

import config.flask_config as flask_config
import config.db_config as db_config
import src.db.manager_db as manager_db
from src.blueprints.cars import blp as cars_blp
from src.blueprints.dropoff import blp as dropoff_blp
from src.blueprints.journey import blp as journey_blp
from src.blueprints.locate import blp as locate_blp


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

    # register blueprints
    api.register_blueprint(cars_blp)
    api.register_blueprint(dropoff_blp)
    api.register_blueprint(journey_blp)
    api.register_blueprint(locate_blp)

    # Health check endpoint
    @app.route("/status", methods=['GET'])
    def status():
        """
        Health check
        :return: '', 200
        """
        return '', 200

    return app
