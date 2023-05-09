from flask import Blueprint, request
from app.shared.enums.http_verb import HttpVerbENUM
from .service import CropImageService

from app.shared.process.process import process

blueprint = Blueprint("CropImage", __name__, url_prefix="/api/crop-image")

@blueprint.route('/', methods=[HttpVerbENUM.POST.value])
def crop_image(service: CropImageService):    
    
    return process(request, service.crop)