
import base64
from PIL import Image
from io import BytesIO

def image_encode(image: Image):
    buffered = BytesIO()
    image.save(buffered, format="PNG")
    encoded_string = base64.b64encode(buffered.getvalue())
    return encoded_string.decode('utf-8')

def image_decode(data: str):
    image_data = data.encode("utf-8")
    buffered = BytesIO(base64.b64decode(image_data))
    image = Image.open(buffered)

    return image