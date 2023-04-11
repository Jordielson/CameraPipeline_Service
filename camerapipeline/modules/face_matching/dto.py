from marshmallow import Schema, fields, EXCLUDE

FaceMatchingDTO = Schema.from_dict({
    "image": fields.Str(required=True),
    "face_crops": fields.Dict(required=True, keys=fields.Integer(), values=fields.Dict()),
    "threshold": fields.Float(required=False, load_default=0.5, dump_default=0.5),
})

class FaceMatchingRegistryDTO(Schema):
    class Meta:
        unknown = EXCLUDE

    image = fields.Str(required=False)
    name = fields.Str(required=True)
    face_crops = fields.Dict(required=True, keys=fields.Integer(), values=fields.Dict())

