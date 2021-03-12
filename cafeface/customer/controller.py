from flask import Blueprint, request, abort
from json import dump

customer = Blueprint("customer", __name__)

@customer.route("/customer/<customer_id>", methods = ['GET'])
def get(customer_id):
    return {"name": "order", "id": customer_id}, 200