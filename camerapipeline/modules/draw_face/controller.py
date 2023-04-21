from flask import Blueprint, request
from camerapipeline.shared.enums.http_verb import HttpVerbENUM
from .service import DrawFaceService

from camerapipeline.shared.process.process import process

blueprint = Blueprint("DrawFace", __name__, url_prefix="/api/draw-face")

@blueprint.route('/', methods=[HttpVerbENUM.POST.value])
def draw_face(service: DrawFaceService):

    return process(request, service.draw_face)
