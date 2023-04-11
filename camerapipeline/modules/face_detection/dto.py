from marshmallow import Schema, fields

FaceDetectionDTO = Schema.from_dict({
    "image": fields.Str(required=True),
    "model_selection": fields.Bool(required=False, load_default=1),
    "confidence": fields.Float(required=False, load_default=0.5),
    }
)

FaceDetectionResponseDTO = Schema.from_dict({
    "image": fields.Str(required=True),
    "face_crops": fields.Dict(required=True, keys=fields.Integer(), values=fields.Dict())
    }
)
