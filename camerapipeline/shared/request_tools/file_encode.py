from .encode import Encode
import requests
from flask import make_response

class FileEncode(Encode):
    CONTENT_TYPE = {'image/jpeg', 'image/jpg', 'video/mp4'}

    def __init__(self, data: dict):
        self.data = ''
        super(FileEncode, self).__init__(
            data=data,
            headers={}
        )
        
    #Override
    def decode_request(self, request):
        return self.decode(request)

    def encode_data(self):
        response = make_response(self.data)
        response.headers.set('Content-Type', self.headers['Content-Type']) 
        response.headers.set('Content-Disposition', self.headers['Content-Disposition']) 
        return response
    
    #Override
    def decode_response(self, response):
        return self.decode(response)
    
    def decode(self, data):
        self.headers = data.headers
        self.data = data.content
        return data.content

    #Override
    def find_data(self, key):
        return self.data
    
    #Override
    def post(self, url:str):
        return requests.post(
            url, 
            data=self.data,
            headers=self.headers
        )