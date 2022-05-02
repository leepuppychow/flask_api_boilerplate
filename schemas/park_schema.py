from marshmallow import fields, Schema


class ParkSchema(Schema):
    id = fields.Integer()
    name = fields.String(required=True)
    city = fields.String()
    state = fields.String()

park_schema = ParkSchema()
parks_schema = ParkSchema(many=True)
