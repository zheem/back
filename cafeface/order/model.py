import mongoengine as me

class Order(me.Document):
    customer = me.ReferenceField('Customer')
    dishes = me.ListField(me.ReferenceField('Dish'))