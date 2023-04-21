from marshmallow import Schema, fields

FaceFeatureExtractionDTO = Schema.from_dict({
    "face_crops": fields.Dict(required=True, keys=fields.Integer(), values=fields.Dict()),
})

