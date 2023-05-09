from .dto import DrawFaceDTO
from .dto import DrawFaceResponseDTO
from app.shared.utlis.image import *

import cv2
import typing
import stow
from matplotlib import colors
import numpy as np


schema: DrawFaceDTO = DrawFaceDTO()
resp_schema: DrawFaceResponseDTO = DrawFaceResponseDTO()

class DrawFaceService():
    def __init__(self) -> None:
        super()

    def draw_face(self, frame:np.ndarray, data: dict) -> dict:
        dto = schema.load(data)

        face_crops = dto['face_crops']
        color: typing.Tuple[int, int, int] = tuple(i*255 for i in colors.to_rgb(dto['color']))
        thickness: int = dto['thickness']

        for value in face_crops.values():
            t, l, b, r = value["tlbr"]
            
            cv2.rectangle(frame, (l, t), (r, b), color, thickness)
            cv2.putText(frame, stow.name(value['name']), (l, t - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, color, thickness)

        return (frame, resp_schema.dump(dto))