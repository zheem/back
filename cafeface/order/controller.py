from flask import Blueprint, request, abort
from json import dump

from .model import Order

order = Blueprint("order", __name__)

@order.route("/orders")
def get():
    order = Order.objects.first()
    return {"dish": order.dishes[0]}, 200