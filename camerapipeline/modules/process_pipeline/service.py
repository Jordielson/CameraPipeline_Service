from injector import inject
from typing import List
from .model import ProcessPipeline
from .dto import ProcessPipelineSchema
from .dto import ServiceSchema

class ProcessPipelineService():
    @inject
    def __init__(self):
        super()

    def process_pipeline(self, dto: ProcessPipelineSchema):
        services: List[ServiceSchema] = dto['pipeline']['pdilist']
        root_list: list = self.find_root(services=services)
        for service in services:
            if service['index'] in root_list:
                self.process_sequence(service=service, services=services)

    def find_root(self, services: List[ServiceSchema]) -> List[int]:
        root_list: List[int] = []
        children: List[int] = []

        for service in services:
            children.extend(service['children'])

        for service in services:
            if not service['index'] in children:
                root_list.append(service['index'])

        return root_list

    def process_sequence(self, service: ServiceSchema, services: List[ServiceSchema]):
        print(service)