from .dto import EffectImageSchema
from .enum import ColorCodeEnum
from camerapipeline.shared.utlis.image import *
import cv2 as cv
import numpy as np
from PIL import Image

class EffectImageService():
    def __init__(self):
        super()

    def apply_effect(self, dto: EffectImageSchema):
        image = image_decode(dto['image'])

        # Convert pil image to cv image 
        open_cv_image = np.array(image) 
        # Convert RGB to BGR 
        open_cv_image = open_cv_image[:, :, ::-1].copy() 
        code: ColorCodeEnum = ColorCodeEnum[dto['effect'].upper()]

        hsv = cv.cvtColor(open_cv_image, code.value ) 

        im_pil = Image.fromarray(hsv)

        return image_encode(im_pil)