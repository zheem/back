import os
import urllib.parse

class Config(object):
    DEBUG = False
    MONGO_URI = os.environ.get("MONGO_URI", "mongodb://localhost:27017/cafe")
    MONGO_PASSWORD = urllib.parse.quote_plus(os.environ.get("MONGO_PASSWORD", "password"))
    MONGODB_SETTINGS = {
        "db": "cafe",
        "host": (lambda uri, password : uri.replace("<password>", password))(MONGO_URI, MONGO_PASSWORD),
    }