from typing import List
from .dto import ObjectSegmentationSchema
from camerapipeline.shared.utlis.image import *

class ObjectSegmentationService():
    def __init__(self):
        super()

    def tracking(self, dto: ObjectSegmentationSchema):
        image = image_decode(dto['image'])
        
        return image_encode(image)