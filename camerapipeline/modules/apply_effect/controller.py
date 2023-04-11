from flask import Blueprint, request
from camerapipeline.shared.enums.http_verb import HttpVerbENUM
from .service import EffectImageService

blueprint = Blueprint("ApplyEffect", __name__, url_prefix="/api/apply-effect")

@blueprint.route('/', methods=[HttpVerbENUM.POST.value])
def apply_effect(service: EffectImageService):

    resp = service.apply_effect(dto=request.json)
    
    return resp, 200, {'ContentType':'application/json'} 
