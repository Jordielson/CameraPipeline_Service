from marshmallow import Schema, fields

class CropImageSchema(Schema):
    image = fields.Str()
    width = fields.Number()
    height = fields.Number()
    position_x = fields.Number()
    position_y = fields.Number()
