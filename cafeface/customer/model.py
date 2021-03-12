import mongoengine as me

class Customer(me.Document):
    name = me.StringField()
    image_url = me.URLField()