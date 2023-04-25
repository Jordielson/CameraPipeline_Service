from .dto import EffectImageSchema
from .enums import ColorCodeEnum
from camerapipeline.shared.utlis.image import *
import cv2 as cv
import numpy as np
from PIL import Image

schema: EffectImageSchema = EffectImageSchema()

class EffectImageService():
    def __init__(self):
        super()

    def apply_effect(self, frame, data: dict):
        dto = schema.load(data)

        # Convert RGB to BGR 
        open_cv_image = frame[:, :, ::-1].copy() 
        code: ColorCodeEnum = ColorCodeEnum[dto['effect'].upper()]

        hsv = cv.cvtColor(open_cv_image, code.value)

        return (hsv, dto)