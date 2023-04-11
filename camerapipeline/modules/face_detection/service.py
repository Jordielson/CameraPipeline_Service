from typing import List
from .dto import FaceDetectionDTO
from camerapipeline.shared.utlis.image import *

import typing
import numpy as np
import mediapipe as mp

class FaceDetectionService():
    def __init__(self) -> None:
        super()

    def face_detection(self, dto: FaceDetectionDTO) -> dict:
        img = image_decode(dto['image'])
        self.mp_face_detection = mp.solutions.face_detection
        self.face_detection = self.mp_face_detection.FaceDetection(model_selection=dto['model_selection'], min_detection_confidence=dto['confidence'])
        
        frame: np.array = np.array(img.convert('RGB'))
        face_crops = {}

        results = self.process(frame)
        
        if results.detections:
            face_crops = {index: {"name": "Ignoto", "tlbr": tlbr.tolist()} for index, tlbr in enumerate(self.tlbr(frame, results.detections))}

        return {
            "image": image_encode_nparray(frame),
            "face_crops": face_crops,
        }
            
    
    def process(self, frame: np.ndarray) -> np.ndarray:
        return self.face_detection.process(frame)

    def tlbr(self, frame: np.ndarray, mp_detections: typing.List) -> np.ndarray:
        detections = []
        frame_height, frame_width, _ = frame.shape
        for detection in mp_detections:
            height = int(detection.location_data.relative_bounding_box.height * frame_height)
            width = int(detection.location_data.relative_bounding_box.width * frame_width)
            left = max(0 ,int(detection.location_data.relative_bounding_box.xmin * frame_width))
            top = max(0 ,int(detection.location_data.relative_bounding_box.ymin * frame_height))

            detections.append([top, left, top + height, left + width])

        return np.array(detections)