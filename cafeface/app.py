from flask import Flask, jsonify
from flask_cors import CORS
from flask_mongoengine import MongoEngine
from flask_marshmallow import Marshmallow

from .settings import Config
from cafeface.customer.controller import customer
from cafeface.dish.controller import dish
from cafeface.order.controller import order

def create_app(config_object=Config):
    """An application factory:
    :param config_object: The configuration object to use.
    """
    app = Flask(__name__)
    app.config.from_object(config_object)
    CORS(app)
    db = MongoEngine(app)
    ma = Marshmallow(app)

    register_blueprints(app)

    return app

def register_blueprints(app: Flask):
    """Register flask blueprints
    :param app: The api object to register routes."""
    app.register_blueprint(customer)
    app.register_blueprint(dish)
    app.register_blueprint(order)