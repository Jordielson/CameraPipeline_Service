from marshmallow import Schema, fields, EXCLUDE

class DrawFaceDTO(Schema):     
    class Meta:
        unknown = EXCLUDE
           
    image = fields.Str(required=True)
    face_crops = fields.Dict(required=True, keys=fields.Integer(), values=fields.Dict())
    color = fields.Str(required=False, load_default="#FFFFFF")
    thickness = fields.Integer(required=False, load_default=2)
    
DrawFaceResponseDTO = Schema.from_dict({
    "image": fields.Str(required=True),
    "face_crops": fields.Dict(required=True, keys=fields.Integer(), values=fields.Dict())
    }
)
