import mongoengine as me

class Dish(me.Document):
    name = me.StringField()
    image_url = me.URLField()