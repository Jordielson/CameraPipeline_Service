from flask import Blueprint, request
from camerapipeline.shared.enums.http_verb import HttpVerbENUM
from .service import CropImageService
from .dto import CropImageDTO
from .dto import CropFaceDTO

blueprint = Blueprint("CropImage", __name__, url_prefix="/api/crop-image")

schema: CropImageDTO = CropImageDTO()
schema_tlbr: CropFaceDTO = CropFaceDTO()

@blueprint.route('/', methods=[HttpVerbENUM.POST.value])
def crop_image(service: CropImageService):
    resp = None
    if 'face_crops' not in request.json:
        resp = service.crop_image(dto=schema.load(request.json))
    else:
        resp = service.crop_face(dto=schema_tlbr.load(request.json))
    
    return resp, 200, {'ContentType':'application/json'} 
