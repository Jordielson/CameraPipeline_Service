from marshmallow import Schema, fields

class DigitalProcessSchema(Schema):
    id = fields.Number()
    name = fields.Str()
    url = fields.Str()
    category = fields.Str()

class ParametersSchema(Schema):
    id = fields.Number()
    name = fields.Str()
    type = fields.Str()
    required = fields.Bool()

class ValueParametersSchema(Schema):
    value = fields.Str()
    parameter = fields.Nested(ParametersSchema)

class ServiceSchema(Schema):
    id = fields.Number()
    index = fields.Number()
    digitalProcess = fields.Nested(DigitalProcessSchema)
    children = fields.List(fields.String())
    valueParameters = fields.Nested(ValueParametersSchema, many=True)

class PipelineSchema(DigitalProcessSchema):
    id = fields.Number()
    description = fields.Str()
    active = fields.Bool()
    pdilist = fields.Nested(ServiceSchema, many=True)

class ProcessPipelineSchema(Schema):
    input = fields.Str()
    pipeline = fields.Nested(PipelineSchema)