from typing import List
import numpy as np
import cv2
from .dto import CropImageDTO
from .dto import CropFaceDTO
from camerapipeline.shared.utlis.image import *

schema: CropImageDTO = CropImageDTO()
schema_tlbr: CropFaceDTO = CropFaceDTO()

class CropImageService():
    def __init__(self):
        super()

    def crop(self, frame, json: dict):
        if 'face_crops' not in json:
            data = self.crop_image(frame, dto=schema.load(json))
        else:
            data = self.crop_face(frame, dto=schema_tlbr.load(json))

        return data

    def crop_image(self, frame: np.ndarray, dto: CropImageDTO):
        
        cropped_image = frame[dto['position_x']: dto['width'], dto['position_y']: dto['height']]

        return (cropped_image, dto)
    
    def crop_face(self, frame: np.ndarray, dto: CropFaceDTO):
        if len(dto['face_crops']) == 1:
            t, l, b, r = dto['face_crops'][0]['tlbr']
            
            crop = frame[t:b, l:r]

            return (crop, dto)
        else:
            raise ValueError("No face detected or more than one face detected")