import os

class Config(object):
    DEBUG = False
    MONGO_URI = "mongodb://localhost:27017/kino"
    MONGODB_SETTINGS = {
        "db": "cafe",
        "host": MONGO_URI,
    }