from marshmallow import Schema, fields

class CustomerSchema(Schema):
    id = fields.String(dump_only=True)
    name = fields.String(dump_only=True)
    image_url = fields.String(dump_only=True)