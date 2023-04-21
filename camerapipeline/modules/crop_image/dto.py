from marshmallow import Schema, fields, EXCLUDE

class CropImageDTO(Schema):
    class Meta:
        unknown = EXCLUDE

    width = fields.Integer()
    height = fields.Integer()
    position_x = fields.Integer()
    position_y = fields.Integer()

class CropFaceDTO(Schema):
    class Meta:
        unknown = EXCLUDE
    
    face_crops = fields.Dict(required=True, keys=fields.Integer(), values=fields.Dict())