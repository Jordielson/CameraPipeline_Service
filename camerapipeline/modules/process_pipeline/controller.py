from flask import Blueprint, request
from camerapipeline.shared.enums.http_verb import HttpVerbENUM
from .service import ProcessPipelineService

blueprint = Blueprint("ProcessPipeline", __name__, url_prefix="/api/process-pipeline")

@blueprint.route('/', methods=[HttpVerbENUM.POST.value])
def process_pipeline(service: ProcessPipelineService):

    img = service.process_pipeline(dto=request.json)
    
    return img, 200, {'ContentType':'application/json'} 
