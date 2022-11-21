from flask import Blueprint, request
from camerapipeline.shared.enums.http_verb import HttpVerbENUM
from .service import ObjectSegmentationService

blueprint = Blueprint("ObjectSegmentation", __name__, url_prefix="/api/object-segmentation")

@blueprint.route('/', methods=[HttpVerbENUM.POST.value])
def object_segmentation(service: ObjectSegmentationService):

    image = service.tracking(dto=request.json)
    
    return image, 200, {'ContentType':'application/json'} 
