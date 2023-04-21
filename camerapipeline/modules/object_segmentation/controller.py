from flask import Blueprint, request
from camerapipeline.shared.enums.http_verb import HttpVerbENUM
from .service import ObjectSegmentationService

from camerapipeline.shared.process.process import process

blueprint = Blueprint("ObjectSegmentation", __name__, url_prefix="/api/object-segmentation")

@blueprint.route('/', methods=[HttpVerbENUM.POST.value])
def object_segmentation(service: ObjectSegmentationService):

    return process(request, service.tracking)
