from typing import List
from .dto import PipelineSchema
from .dto import ServiceSchema
from app.shared.utlis.file import file_extension
from app.shared.utlis.image import *
from app.shared.request_tools.encode import *
from app.shared.request_tools.multipart_encode import *
from app.shared.request_tools.encode_factory import *
from app.shared.utlis.config import *
from app.shared.process.process import encode_h264

class ProcessPipelineService():
    def __init__(self):
        super()
        self.pipeline_schema = PipelineSchema()

    def process_pipeline(self, encode: Encode) -> Encode:
        data = self.pipeline_schema.load(encode.data['pipeline'])

        services: List[ServiceSchema] = data['pdilist']
        root_list: list = self.find_root(services=services)

        del encode.data['pipeline']
        for service in services:
            if service['index'] in root_list:
                encode = self.custom_processing(
                    service=service, 
                    services=services, 
                    encode=encode
                )
        
        return encode

    def find_root(self, services: List[ServiceSchema]) -> List[int]:
        root_list: List[int] = []
        children: List[int] = []

        for service in services:
            children.extend(service['children'])

        for service in services:
            if not service['index'] in children:
                root_list.append(service['index'])

        return root_list

    def custom_processing(self, service: ServiceSchema, services: List[ServiceSchema], encode: Encode) -> dict:
        url: str = service['digitalProcess']['url']

        for value_parameter in service['valueParameters']:
            value = value_parameter['value']

            if value:
                if value_parameter['parameter']['type'] == 'NUMBER':
                    value = float(value)
                elif value_parameter['parameter']['type'] == 'BOOL':
                    if value == 'true':
                        value = True
                    else:
                        value = False
                        
                encode.add_value(value_parameter['parameter']['name'], value)

        response = encode.post(url=url)

        encode = EncodeFactory.factory(response.headers['Content-Type'])
        encode.decode_response(response=response)

        if response.status_code != 200:
            raise Exception('{} {}'.format(service['digitalProcess']['name'], 'could not process the file'))
        if len(service['children']):
            for serv in services:
                if serv['index'] in service['children']:
                    return self.custom_processing(service=serv, services=services, encode=encode)
        else:
            return encode

    def process(self, encode: Encode) -> Encode: 
        encoder: Encode = self.process_pipeline(
            encode=encode,
        )

        file: bytes = None
        filename: str = None
        if type(encoder) is JsonEncode:
            file = decode(encoder.find_data('input'))
            filename = 'image_output.png'
        elif type(encoder) is MultipartEncode:
            filename, file = encoder.find_file('file')
            if 'video' in encoder.data \
                and 'encode' in encoder.data['video'] \
                and encoder.data['video']['encode'] != 'h264':
                file = encode_h264(file)
        else:
            return encoder
        
        encode_out = self.create_output_encoder(filename, file)

        return encode_out
        
    def create_output_encoder(self, filename, data):
        file_ext = file_extension(filename)
        file_type: str = ''
        if file_ext in ALLOWED_IMAGE_EXTENSIONS:
            file_type = 'image'
        elif file_ext in ALLOWED_VIDEO_EXTENSIONS:
            file_type = 'video'
        else:
            file_type = 'undefined'

        content_type = f'{file_type}/{file_ext}'

        encode_out = EncodeFactory.factory(file_type)
        encode_out.headers = {'Content-Type': content_type, 'Content-Disposition': 'attachment; filename="%s"' % filename}
        encode_out.data = data
        
        return encode_out