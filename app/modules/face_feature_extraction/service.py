from .dto import FaceFeatureExtractionDTO
from app.shared.utlis.image import *

import os
import cv2
import stow
import numpy as np 
import onnxruntime as ort
schema: FaceFeatureExtractionDTO = FaceFeatureExtractionDTO()

class FaceFeatureExtractionService():
    def __init__(self):
        super()
        """
        Download Model in https://drive.google.com/file/d/1M_LGbX_Sfe3iKRxf8LIO0QZ3hlkRhRVY/view?usp=sharing.
        Create an environment variable in your .env file with the name FACE_FEATURE_MODEL_PATH 
        that specifies the location of the model.
        """
        self.model_path = os.environ["FACE_FEATURE_MODEL_PATH"]


    def face_feature_extraction(self, frame: np.ndarray, data: dict):
        dto = schema.load(data)

        if not stow.exists(self.model_path):
            raise Exception(f"Model doesn't exists in {self.model_path}")

        providers = ['CPUExecutionProvider']
        self.ort_sess = ort.InferenceSession(self.model_path, providers=providers)
        self.input_shape = self.ort_sess._inputs_meta[0].shape[1:3]

        face_crops: dict = dto['face_crops']

        for key, value in face_crops.copy().items():
            t, l, b, r = value["tlbr"]
            face_crops[key]['face_encoding'] = self.encode(frame[t:b, l:r]).tolist()

        return (frame, schema.dump({
            'face_crops': face_crops,
            })
        )
        
    def encode(self, face_image: np.ndarray) -> np.ndarray:
        face = self.normalize(face_image)
        face = cv2.resize(face, self.input_shape).astype(np.float32)

        encode = self.ort_sess.run(None, {self.ort_sess._inputs_meta[0].name: np.expand_dims(face, axis=0)})[0][0]
        normalized_encode = self.l2_normalize(encode)

        return normalized_encode

    def normalize(self, img: np.ndarray) -> np.ndarray:
        mean, std = img.mean(), img.std()
        return (img - mean) / std
    
    def l2_normalize(self, x: np.ndarray, axis: int = -1, epsilon: float = 1e-10) -> np.ndarray:
        output = x / np.sqrt(np.maximum(np.sum(np.square(x), axis=axis, keepdims=True), epsilon))
        return output
    
    def load_anchors(self, faces_path: str):
        anchors = {}
        if not stow.exists(faces_path):
            return {}

        for face_path in stow.ls(faces_path):
            anchors[stow.basename(face_path)] = self.encode(cv2.imread(face_path.path))

        return anchors