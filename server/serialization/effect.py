from pydantic import BaseModel

class Effect(BaseModel):
    is_positive:bool
    attribute:str
    amount:int

    class config:
        orm_mode = True