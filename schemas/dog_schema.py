from marshmallow import fields, Schema


class DogSchema(Schema):
    id = fields.Integer()
    name = fields.String(required=True)
    age = fields.Integer()
    description = fields.String()

dog_schema = DogSchema()
dogs_schema = DogSchema(many=True)
