import datetime as dt

class ProcessPipeline():
    id: int
    description: str
    name: str
    amount: int 
    created_at: dt.datetime = dt.datetime.now()

    def __init__(self, id, name, description, amount):
        self.description = description
        self.amount = amount
        self.id = id
        self.name = name