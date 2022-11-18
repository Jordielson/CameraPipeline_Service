from marshmallow import Schema, fields

class EffectImageSchema(Schema):
    image = fields.Str()
    effect = fields.Str()


