from injector import inject
from .model import ProcessPipeline

class ProcessPipelineService():
    @inject
    def __init__(self):
        super()
    def process_pipeline(self):
        return ProcessPipeline(id=1, name='test', description='test', amount=3)