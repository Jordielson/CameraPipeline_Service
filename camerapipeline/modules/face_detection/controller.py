from flask import Blueprint, request
from camerapipeline.shared.enums.http_verb import HttpVerbENUM
from .service import FaceDetectionService

from camerapipeline.shared.process.process import process

blueprint = Blueprint("FaceDetection", __name__, url_prefix="/api/face-detection")

@blueprint.route('/', methods=[HttpVerbENUM.POST.value])
def face_detection(service: FaceDetectionService):

    return process(request, service.find)
