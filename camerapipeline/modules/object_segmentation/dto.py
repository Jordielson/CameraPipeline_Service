from marshmallow import Schema, fields

class ObjectSegmentationSchema(Schema):
    image = fields.Str()
