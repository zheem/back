import os

class Config(object):
    DEBUG = False
    MONGO_URI = "mongodb://localhost:27017/cafe"
    MONGODB_SETTINGS = {
        "db": "cafe",
        "host": MONGO_URI,
    }