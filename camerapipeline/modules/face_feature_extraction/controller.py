from flask import Blueprint, request
from camerapipeline.shared.enums.http_verb import HttpVerbENUM
from .dto import FaceFeatureExtractionDTO
from .dto import FaceFeatureExtractionResponseDTO
from .service import FaceFeatureExtractionService

blueprint = Blueprint("FaceFeatureExtraction", __name__, url_prefix="/api/face-feature-extraction")

schema: FaceFeatureExtractionDTO = FaceFeatureExtractionDTO()
schemaResponse: FaceFeatureExtractionResponseDTO = FaceFeatureExtractionResponseDTO()

@blueprint.route('/', methods=[HttpVerbENUM.POST.value])
def face_feature_extraction(service: FaceFeatureExtractionService):

    face_feature_extraction = schema.load(request.json)

    resp = service.face_feature_extraction(dto=face_feature_extraction)

    return schemaResponse.dump(resp), 200, {'ContentType':'application/json'} 
