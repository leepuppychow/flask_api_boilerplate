from marshmallow import Schema, fields


class ToySchema(Schema):
    id = fields.Integer()
    dog_id = fields.Integer(nullable=False)
    name = fields.String(required=True)
    description = fields.String()

toy_schema = ToySchema()
toys_schema = ToySchema(many=True)
