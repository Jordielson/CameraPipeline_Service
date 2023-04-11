from flask import Blueprint, request
from camerapipeline.shared.enums.http_verb import HttpVerbENUM
from .service import FaceMatchingService
from .dto import FaceMatchingDTO
from .dto import FaceMatchingRegistryDTO

blueprint = Blueprint("FaceMatching", __name__, url_prefix="/api/face-matching")

schema: FaceMatchingDTO = FaceMatchingDTO()
register_schema: FaceMatchingRegistryDTO = FaceMatchingRegistryDTO()

@blueprint.route('/', methods=[HttpVerbENUM.POST.value])
def face_matching(service: FaceMatchingService):
    face_matching = schema.load(request.json)

    resp = service.face_matching(dto=face_matching)
    
    return schema.dump(resp), 200, {'ContentType':'application/json'} 

@blueprint.route('/register', methods=[HttpVerbENUM.POST.value])
def register_face(service: FaceMatchingService):
    face_record = register_schema.load(request.json)

    resp = service.register_face_matching(dto=face_record)
    
    return register_schema.dump(resp), 200, {'ContentType':'application/json'} 
