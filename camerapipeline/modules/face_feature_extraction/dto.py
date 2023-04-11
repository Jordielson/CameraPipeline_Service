from marshmallow import Schema, fields

FaceFeatureExtractionDTO = Schema.from_dict({
    "face_crops": fields.Dict(required=True, keys=fields.Integer(), values=fields.Dict()),
    "image": fields.Str(required=True),
})

FaceFeatureExtractionResponseDTO = Schema.from_dict({
    "image": fields.Str(required=True),
    "face_crops": fields.Dict(required=True, keys=fields.Integer(), values=fields.Dict()),
})

