from flask import Blueprint, request, abort
from json import dump

order = Blueprint("order", __name__)

@order.route("/orders")
def get():
    return {"name": "order"}, 200