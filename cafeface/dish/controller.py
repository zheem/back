from flask import Blueprint, request, abort
from json import dump
from mongoengine.errors import ValidationError

from .model import Dish
from .schema import DishSchema

dish = Blueprint("dish", __name__)
dish_schema = DishSchema()

@dish.route("/")
def get_all():
    return {"name": "dish"}, 200

@dish.route("/dish/<dish_id>")
def get(dish_id):
    try:
        dish = Dish.objects(id=dish_id).first()
    except ValidationError:
        abort(404)
    if dish == None:
        abort(404)
    return dish_schema.dump(dish)