from flask import Blueprint, request
from camerapipeline.shared.enums.http_verb import HttpVerbENUM
from .dto import DrawFaceDTO
from .dto import DrawFaceResponseDTO
from .service import DrawFaceService

blueprint = Blueprint("DrawFace", __name__, url_prefix="/api/draw-face")

schema: DrawFaceDTO = DrawFaceDTO()
resp_schema: DrawFaceResponseDTO = DrawFaceResponseDTO()

@blueprint.route('/', methods=[HttpVerbENUM.POST.value])
def draw_face(service: DrawFaceService):
    draw_face = schema.load(request.json)
    
    resp = service.draw_face(dto=draw_face)
    
    return resp_schema.dump(resp), 200, {'ContentType':'application/json'} 
