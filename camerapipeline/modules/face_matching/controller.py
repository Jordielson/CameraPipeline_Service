from flask import Blueprint, request
from camerapipeline.shared.enums.http_verb import HttpVerbENUM
from .service import FaceMatchingService

from camerapipeline.shared.process.process import process

blueprint = Blueprint("FaceMatching", __name__, url_prefix="/api/face-matching")

@blueprint.route('/', methods=[HttpVerbENUM.POST.value])
def face_matching(service: FaceMatchingService):

    return process(request, service.face_matching) 

@blueprint.route('/register', methods=[HttpVerbENUM.POST.value])
def register_face(service: FaceMatchingService):

    return process(request, service.register_face_matching) 
