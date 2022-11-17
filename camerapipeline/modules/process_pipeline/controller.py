from flask import Blueprint, jsonify, request
from camerapipeline.shared.enums.http_verb import HttpVerbENUM
from .service import ProcessPipelineService
from .dto import ProcessPipelineSchema

blueprint = Blueprint("ProcessPipeline", __name__, url_prefix="/api/process-pipeline")

@blueprint.route('/', methods=[HttpVerbENUM.GET.value])
def get(service: ProcessPipelineService):
    dto: ProcessPipelineSchema = ProcessPipelineSchema()
    
    return jsonify(dto.dump(service.process_pipeline()))
