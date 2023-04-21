
from abc import ABC, abstractmethod

class Encode(ABC):       
    def __init__(self, data, headers):
        self.data = data
        self.headers = headers

    @abstractmethod
    def decode_request(self, request):
        pass

    @abstractmethod
    def decode_response(self, response):
        pass

    @abstractmethod
    def encode_data(self):
        pass

    @abstractmethod
    def post(self, url:str):
        pass

    @abstractmethod
    def find_data(self, key):
        pass
    
    def add_value(self, key:str, value):
        self.data[key] = value

    def set_values(self, data):
        self.data = data

    