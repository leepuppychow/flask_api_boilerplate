from marshmallow import fields, Schema

from models.dog import Dog


class DogSchema(Schema):
    class Meta:
        model = Dog

    id = fields.Integer()
    name = fields.String(required=True)
    age = fields.Integer()
    description = fields.String()

dog_schema = DogSchema()
dogs_schema = DogSchema(many=True)
