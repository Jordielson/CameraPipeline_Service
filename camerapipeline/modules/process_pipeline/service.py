from typing import List
from .dto import ProcessPipelineSchema
from .dto import ServiceSchema
from camerapipeline.shared.utlis.image import image_encode
import requests
from PIL import Image

class ProcessPipelineService():
    def __init__(self):
        super()

    def process_pipeline(self, dto: ProcessPipelineSchema):
        images: list = []
        r = requests.get(dto['input'], stream=True)
        if r.status_code != 200:
            raise Exception("Image is not present")

        im = Image.open(r.raw)
        encoded_string = image_encode(im)

        services: List[ServiceSchema] = dto['pipeline']['pdilist']
        root_list: list = self.find_root(services=services)
        for service in services:
            if service['index'] in root_list:
                images.append(
                    self.process_sequence(
                        service=service, 
                        services=services, 
                        image=encoded_string
                    )
                )
        return images[0]

    def find_root(self, services: List[ServiceSchema]) -> List[int]:
        root_list: List[int] = []
        children: List[int] = []

        for service in services:
            children.extend(service['children'])

        for service in services:
            if not service['index'] in children:
                root_list.append(service['index'])

        return root_list

    def process_sequence(self, service: ServiceSchema, services: List[ServiceSchema], image: str):
        url: str = service['digitalProcess']['url']
        json: dict = {
            "image": image,
        }
        for value_parameter in service['valueParameters']:
            value = value_parameter['value']

            if value_parameter['parameter']['type'] == 'NUMBER':
                value = float(value)
            elif value_parameter['parameter']['type'] == 'BOOL':
                if value == 'true':
                    value = True
                else:
                    value = False
            
            json[value_parameter['parameter']['name']] = value

        response = requests.post(url, json=json)
        if response.status_code != 200:
            raise Exception('{} {}'.format(service['digitalProcess']['name'], 'could not process the file'))

        if len(service['children']):
            for serv in services:
                if serv['index'] in service['children']:
                    return self.process_sequence(service=serv, services=services, image=response.content.decode('utf-8'))
        else:
            return response.content