from flask import Blueprint, request
from camerapipeline.shared.enums.http_verb import HttpVerbENUM
from .service import EffectImageService

from camerapipeline.shared.process.process import process

blueprint = Blueprint("ApplyEffect", __name__, url_prefix="/api/apply-effect")

@blueprint.route('/', methods=[HttpVerbENUM.POST.value])
def apply_effect(service: EffectImageService):

    return process(request, service.apply_effect)
