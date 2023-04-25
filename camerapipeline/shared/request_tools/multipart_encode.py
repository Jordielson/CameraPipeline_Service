from requests_toolbelt.multipart import decoder
from requests_toolbelt import MultipartEncoder
from ..utlis.utils import chunked_reader
from .encode import Encode
import json
from flask import Response
import json

import re

import requests

class MultipartEncode(Encode):
    CONTENT_TYPE = {'multipart/form-data'}

    def __init__(self, data: dict={}, files: dict={}):  
        self.files = files
        super(MultipartEncode, self).__init__(
            data=data,
            headers={}
        )

    #Override
    def decode_request(self, request):
        return self.decode(request)
    
    #Override
    def decode_response(self, response):
        return self.decode(response)

    def decode(self, data):
        multipart_data = decoder.MultipartDecoder.from_response(data)
        for part in multipart_data.parts:
            # print(part.headers)
            if b'Content-Type' in part.headers and part.headers[b'Content-Type'] == b'application/json':
                self.data = json.loads(part.content.decode('utf-8'))
            else:
                content_disposition = part.headers[b'Content-Disposition'].decode('utf-8')
                try:
                    name = re.search(r'name="(.+?)"', content_disposition).group(1)
                    filename = re.search(r'filename="(.+?)"', content_disposition).group(1)
                    self.add_file(name, filename, part.content)
                except AttributeError as e:
                    raise e
        return self.data

    def add_file(self, name, filename, file):
        self.files[name] = (filename, file)


    def find_data(self, key):
        return self.data[key]
    
    def find_file(self, key):
        return self.files[key]

    #Override
    def encode_data(self):
        mp = self.create_mp()
        return Response(
            chunked_reader(mp), content_type=mp.content_type,
            headers={'Content-Length': mp.len}
        )

    #Override
    def post(self, url:str):
        mp = self.create_mp()
        return requests.post(
            url, 
            data=mp,
            headers=self.headers
        )
    
    #Override
    def add_value(self, key:str, value):
        self.data[key] = value

    def create_mp(self):
        fields = self.files
        fields['data'] = (None, json.dumps(self.data), 'application/json')
        mp_encoder = MultipartEncoder(
            fields=fields,
        )
        self.headers = {
            'Content-Type': mp_encoder.content_type,
        }
        return mp_encoder