from injector import inject
from .dto import FaceMatchingDTO
from .dto import FaceMatchingRegistryDTO
from .repository import FaceMatchingRespository
from camerapipeline.shared.utlis.image import *

import typing
import numpy as np 

schema: FaceMatchingDTO = FaceMatchingDTO()
register_schema: FaceMatchingRegistryDTO = FaceMatchingRegistryDTO()

class FaceMatchingService():
    @inject
    def __init__(self, repository: FaceMatchingRespository):
        self.repository = repository
        self.anchors = {}

    def face_matching(self, frame: np.ndarray, data: dict):
        dto = schema.load(data)

        face_crops = dto['face_crops']
        threshold = dto['threshold']

        anchors = self.load_anchors()

        for key, value in face_crops.items():
            distances = self.cosine_distance(value['face_encoding'], list(anchors.values()))

            if np.max(distances) > threshold:
                face_crops[key]["name"] = list(anchors.keys())[np.argmax(distances)]

        return (frame, schema.dump({
            'face_crops': face_crops,
            })
        )


    def register_face_matching(self, frame: np.ndarray, data: dict):
        dto = register_schema.load(data)

        if len(dto['face_crops']) == 1:
            face_encoding = dto['face_crops'][0]['face_encoding']

            data = {
                'name': dto['name'],
                'face_encoding': face_encoding
            }
            self.repository.register(data)

            self.load_anchors(force_load=True)

            dto['face_crops'][0]['name'] = dto['name']
            return (frame, register_schema.dump(dto))
        else:
            raise ValueError("No face detected or more than one face detected")
    
    def cosine_distance(self, a: np.ndarray, b: typing.Union[np.ndarray, list]) -> np.ndarray:
        if isinstance(a, list):
            a = np.array(a)

        if isinstance(b, list):
            b = np.array(b)

        return np.dot(a, b.T) / (np.linalg.norm(a) * np.linalg.norm(b))
    
    def load_anchors(self, force_load: bool = False):
        if self.anchors and not force_load:
            return self.anchors

        for face_resource in self.repository.all():
            self.anchors[face_resource['name']] = face_resource['face_encoding']

        return self.anchors

