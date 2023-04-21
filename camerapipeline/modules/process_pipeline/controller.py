import json
from flask import Blueprint, request
from werkzeug.utils import secure_filename
from camerapipeline.shared.enums.http_verb import HttpVerbENUM
from .service import ProcessPipelineService
from .dto import ProcessPipelineSchema
from .dto import PipelineSchema
from camerapipeline.shared.request_tools.encode_factory import *
from camerapipeline.shared.process.process import check_input_content

blueprint = Blueprint("ProcessPipeline", __name__, url_prefix="/api/process-pipeline")

schema: ProcessPipelineSchema = ProcessPipelineSchema()
pipeline_schema: PipelineSchema = PipelineSchema()

@blueprint.route('/', methods=[HttpVerbENUM.POST.value])
def process_pipeline(service: ProcessPipelineService):
    encoder: Encode = check_input_content(request=request)
    return service.process(encoder).encode_data()
    # if request.content_type == 'application/json':
    #     req: dict = schema.load(request.json)
    #     if req['input_type'] == 'IMAGE':
    #         encoder = EncodeFactory.factory(request.content_type)
    #         encoder.add_value('frame', req['input'])
    #         return service.process_image(pipeline=req['pipeline'], encode=encoder).encode_data()
    #     else:
    #         return "Not a valid input type", 400
    # else:
    #     if 'file' not in request.files:
    #         return "No file part", 400
        
    #     file = request.files['file']

    #     if file.filename == '':
    #         return "No selected file", 400
        
    #     if file:
    #         pipeline = json.loads(dict(request.form)['pipeline'])
    #         filename = secure_filename(file.filename)
    #         return service.process_file(pipeline=pipeline, file=file.read(), filename=filename)
    #     else:
    #         return "Not a valid file", 400
