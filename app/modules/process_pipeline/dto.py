from marshmallow import Schema, fields, EXCLUDE

class DigitalProcessSchema(Schema):
    class Meta:
        unknown = EXCLUDE

    id = fields.Number()
    name = fields.Str()
    url = fields.Str()
    category = fields.Str()

class ParametersSchema(Schema):
    class Meta:
        unknown = EXCLUDE

    id = fields.Number()
    name = fields.Str()
    type = fields.Str()
    required = fields.Bool()

class ValueParametersSchema(Schema):
    class Meta:
        unknown = EXCLUDE

    value = fields.Str()
    parameter = fields.Nested(ParametersSchema)

class ServiceSchema(Schema):
    class Meta:
        unknown = EXCLUDE

    id = fields.Number()
    index = fields.Number()
    digitalProcess = fields.Nested(DigitalProcessSchema)
    children = fields.List(fields.Int())
    valueParameters = fields.Nested(ValueParametersSchema, many=True)

class PipelineSchema(DigitalProcessSchema):
    class Meta:
        unknown = EXCLUDE

    id = fields.Number()
    description = fields.Str()
    active = fields.Bool()
    pdilist = fields.Nested(ServiceSchema, many=True)

class ProcessPipelineSchema(Schema):
    class Meta:
        unknown = EXCLUDE

    input = fields.Str(required=True)
    pipeline = fields.Nested(PipelineSchema, required=True)
    input_type = fields.Str(load_default='IMAGE', required=False)