from typing import List
from .dto import CropImageSchema
from camerapipeline.shared.utlis.image import *

class CropImageService():
    def __init__(self):
        super()

    def crop_image(self, dto: CropImageSchema):
        image = image_decode(dto['image'])
        
        cropped_image = image.crop((dto['position_x'], dto['position_y'], dto['width'], dto['height']))

        return image_encode(cropped_image)