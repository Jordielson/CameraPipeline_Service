from enum import Enum
import cv2 as cv

class ColorCodeEnum(Enum):
    HSV: int = cv.COLOR_BGR2HSV
    GRAY: int = cv.COLOR_BGR2GRAY
    LAB: int = cv.COLOR_BGR2Lab
    LUV: int = cv.COLOR_BGR2Luv