
import base64
from PIL import Image
from io import BytesIO
import numpy as np
import cv2

def image_encode(image: Image) -> str:
    buffered = BytesIO()
    image.save(buffered, format="PNG")
    encoded_string = base64.b64encode(buffered.getvalue())
    return encoded_string.decode('utf-8')

def encode(bytes: bytes) -> str:
    encoded_string = base64.b64encode(bytes)
    return encoded_string.decode('utf-8')

def image_encode_nparray(image: np.array) -> str:
    return image_encode(Image.fromarray(image))

def image_decode_nparray(data: str) -> np.array:
    return np.array(image_decode(data))

def image_encode_bytes(frame: np.array) -> bytes:
    return decode(image_encode_nparray(frame))

def image_decode_bytes(image_bytes: bytes) -> np.array:
    return np.array(Image.open(BytesIO(image_bytes))) 

def image_decode(data: str) -> Image:
    image_data = data.encode("utf-8")
    buffered = BytesIO(base64.b64decode(image_data))
    image = Image.open(buffered)
    
    return image.convert('RGB')

def decode(data: str) -> bytes:
    img_data = data.encode()
    content = base64.b64decode(img_data)

    return content
