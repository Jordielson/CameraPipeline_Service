from typing import List
import cv2
from .dto import CropImageDTO
from .dto import CropFaceDTO
from camerapipeline.shared.utlis.image import *

class CropImageService():
    def __init__(self):
        super()

    def crop_image(self, dto: CropImageDTO):
        image = image_decode(dto['image'])
        
        cropped_image = image.crop((dto['position_x'], dto['position_y'], dto['width'], dto['height']))

        return {
            "image":image_encode(cropped_image)
        }
    
    def crop_face(self, dto: CropFaceDTO):
        if len(dto['face_crops']) == 1:
            t, l, b, r = dto['face_crops'][0]['tlbr']
            
            img = image_decode(dto['image'])
            image_np = np.array(img)
            crop = image_np[t:b, l:r]

            return {
                "image":image_encode_nparray(crop)
            }
        else:
            raise ValueError("No face detected or more than one face detected")