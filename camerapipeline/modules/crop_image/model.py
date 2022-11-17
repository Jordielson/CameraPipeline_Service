import datetime as dt

class ProcessPipeline():
    image: str
    width: int
    height: int
    position_x: int
    position_y: int

    def __init__(self, image, width, height, position_x, position_y):
        self.image = image
        self.width = width
        self.height = height
        self.position_x = position_x
        self.position_y = position_y