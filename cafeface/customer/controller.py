from flask import Blueprint, request, abort
from json import dump
from mongoengine.errors import ValidationError

from cafeface.order.model import Order
from cafeface.dish.controller import prepare_dishes, dish_schema
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

@customer.route("/customer/<customer_id>/dishes")
def get_for_person(customer_id):
    orders = Order.objects(customer=customer_id).all()
    dishes = prepare_dishes(orders)
    return {"dishes": [dish_schema.dump(dish) for dish in dishes]}, 200