from flask import Blueprint, request
from camerapipeline.shared.enums.http_verb import HttpVerbENUM
from .dto import FaceDetectionDTO
from .dto import FaceDetectionResponseDTO
from .service import FaceDetectionService

blueprint = Blueprint("FaceDetection", __name__, url_prefix="/api/face-detection")

schema: FaceDetectionDTO = FaceDetectionDTO()
resp_schema: FaceDetectionResponseDTO = FaceDetectionResponseDTO()

@blueprint.route('/', methods=[HttpVerbENUM.POST.value])
def face_detection(service: FaceDetectionService):
    face_detection = schema.load(request.json)

    resp = service.face_detection(dto=face_detection)
    
    return resp_schema.dump(resp), 200, {'ContentType':'application/json'} 
