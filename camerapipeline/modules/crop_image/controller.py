from flask import Blueprint, request
from camerapipeline.shared.enums.http_verb import HttpVerbENUM
from .service import CropImageService

blueprint = Blueprint("CropImage", __name__, url_prefix="/api/crop-image")

@blueprint.route('/', methods=[HttpVerbENUM.POST.value])
def crop_image(service: CropImageService):

    image = service.crop_image(dto=request.json)
    
    return image, 200, {'ContentType':'application/json'} 
