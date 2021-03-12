from flask import Blueprint, request, abort
from json import dump

dish = Blueprint("dish", __name__)

@dish.route("/")
def get():
    return {"name": "dish"}, 200