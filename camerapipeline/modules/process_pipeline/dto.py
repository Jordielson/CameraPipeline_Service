from marshmallow import Schema, fields

class ProcessPipelineSchema(Schema):
    id = fields.Number()
    description = fields.Str()
    name = fields.Str()
    amount = fields.Number()
    created_at = fields.Date()