from flask import Blueprint, request, abort
from json import dump
from mongoengine.errors import ValidationError
from typing import List, Set

from cafeface.order.model import Order
from .model import Dish
from .schema import DishSchema

dish = Blueprint("dish", __name__)
dish_schema = DishSchema()

@dish.route("/")
def get_all():
    orders = Order.objects.all()
    dishes = prepare_dishes(orders)
    return {"dishes": [dish_schema.dump(dish) for dish in dishes]}, 200

@dish.route("/dish/<dish_id>")
def get(dish_id):
    try:
        dish = Dish.objects(id=dish_id).first()
    except ValidationError:
        abort(404)
    if dish == None:
        abort(404)
    return dish_schema.dump(dish)

def prepare_dishes(orders: List[Order]) -> Set[Dish]:
    """[summary]

    Args:
        orders (List[Order]): list of order objects

    Returns:
        Set[Dish]: set of dish objects with count applied
    """
    all_dishes = []
    for order in orders:
        all_dishes.extend(order.dishes)
    dishes = set(all_dishes)
    for dish in dishes:
        dish.count = all_dishes.count(dishes)
    return dishes