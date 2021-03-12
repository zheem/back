import mongoengine as me

class Dish(me.Document):
    name = me.StringField()
    image_url = me.URLField()

    def __eq__(self, other):
        return int(str(self.id), 16) == int(str(self.id), 16)

    def __hash__(self):
        return int(str(self.id), 16)