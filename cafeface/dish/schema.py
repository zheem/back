from marshmallow import Schema, fields

class DishSchema(Schema):
    id = fields.String(dump_only=True)
    name = fields.String(dump_only=True)
    image_url = fields.String(dump_only=True)
    count = fields.Integer(dump_only=True, default=0)