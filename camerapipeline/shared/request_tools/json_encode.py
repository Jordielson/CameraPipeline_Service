from .encode import Encode
import requests

from flask import make_response

class JsonEncode(Encode):
    CONTENT_TYPE = {'application/json'}

    def __init__(self, data: dict):
        super(JsonEncode, self).__init__(
            data=data,
            headers={
                'Content-Type': 'application/json',
                'Accept': 'application/json'
            }
        )
        
    #Override
    def decode_request(self, request):
        self.data = request.json
        self.headers = request.headers
        return self.data
    
    #Override
    def decode_response(self, response):
        self.data = response.json()
        self.headers = response.headers
        return self.data

    #Override
    def encode_data(self):
        response = make_response(self.data)
        response.headers.set('Content-Type', self.headers['Content-Type']) 
        response.headers.set('Accept', self.headers['Accept']) 
        return response

    #Override
    def find_data(self, key):
        return self.data[key]
    
    #Override
    def post(self, url:str):
        return requests.post(
            url, 
            json=self.data,
            headers=self.headers
        )