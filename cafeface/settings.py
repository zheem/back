import os
from urllib.parse import quote

class Config(object):
    DEBUG = False
    MONGO_URI = "mongodb://localhost:27017/cafe"
    MONGODB_SETTINGS = {
        "db": "cafe",
        "host": MONGO_URI,
    }

class DevConfig(Config):
    DEBUG = True

class ProdConfig(Config):
    MONGO_URI = os.environ.get(
        "MONGO_URI", "mongodb://localhost:27017/cafe"
    ).replace("<password>", quote(os.environ.get("MONGO_PASSWORD")))
    MONGODB_SETTINGS = {
        "db": "cafe",
        "host": MONGO_URI,
    }