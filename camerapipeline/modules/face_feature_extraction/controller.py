from flask import Blueprint, request
from camerapipeline.shared.enums.http_verb import HttpVerbENUM
from .service import FaceFeatureExtractionService

from camerapipeline.shared.process.process import process

blueprint = Blueprint("FaceFeatureExtraction", __name__, url_prefix="/api/face-feature-extraction")

@blueprint.route('/', methods=[HttpVerbENUM.POST.value])
def face_feature_extraction(service: FaceFeatureExtractionService):
    
    return process(request, service.face_feature_extraction)
