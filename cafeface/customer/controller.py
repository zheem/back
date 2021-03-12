from flask import Blueprint, request, abort
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
        if customer == None:
            abort(404)
    except ValidationError:
        abort(400, "Bad id")
    return customer_schema.dump(customer)

@customer.route("/customers", methods = ['GET'])
def get_all():
    return {"customers": [customer_schema.dump(customer) for customer in Customer.objects.all()]}, 200

@customer.route("/customer/<customer_id>/dishes", methods = ['GET'])
def get_for_person(customer_id):
    orders = Order.objects(customer=customer_id).all()
    dishes = prepare_dishes(orders)
    return {"dishes": [dish_schema.dump(dish) for dish in dishes]}, 200