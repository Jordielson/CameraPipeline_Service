from marshmallow import Schema, fields, EXCLUDE

class FaceDetectionDTO(Schema):
    class Meta:
        unknown = EXCLUDE

    model_selection = fields.Bool(required=False, load_default=1)
    confidence = fields.Float(required=False, load_default=0.5)
    


FaceDetectionResponseDTO = Schema.from_dict({
    "face_crops": fields.Dict(required=True, keys=fields.Integer(), values=fields.Dict())
    }
)
