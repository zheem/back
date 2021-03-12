from flask import Flask, jsonify
from flask_cors import CORS
from flask_mongoengine import MongoEngine
from flask_marshmallow import Marshmallow

from .settings import Config

def create_app(config_object=Config):
    """An application factory:
    :param config_object: The configuration object to use.
    """
    app = Flask(__name__)
    app.config.from_object(config_object)
    CORS(app)
    db = MongoEngine(app)
    ma = Marshmallow(app)

    #register_blueprints(app)

    @app.route("/")
    def test():
        return jsonify({"Hello": "World"})

    return app