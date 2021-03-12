from flask import Blueprint, request, abort
from json import dump
from mongoengine.errors import ValidationError

from .model import Customer
from .schema import CustomerSchema

customer = Blueprint("customer", __name__)
customer_schema = CustomerSchema()

@customer.route("/customer/<customer_id>", methods = ['GET'])
def get(customer_id):
    try:
        customer = Customer.objects(id=customer_id).first()
    except ValidationError:
        abort(404)
    if customer == None:
        abort(404)
    return customer_schema.dump(customer)