from marshmallow import Schema, fields

class CropImageDTO(Schema):
    image = fields.Str()
    width = fields.Number()
    height = fields.Number()
    position_x = fields.Number()
    position_y = fields.Number()

class CropFaceDTO(Schema):
    image = fields.Str()
    face_crops = fields.Dict(required=True, keys=fields.Integer(), values=fields.Dict())