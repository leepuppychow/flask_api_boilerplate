from marshmallow import fields, Schema


class SampleSchema(Schema):
    id = fields.Integer()
    name = fields.String(required=True)

sample_schema = SampleSchema()
samples_schema = SampleSchema(many=True)