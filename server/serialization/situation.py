from pydantic import BaseModel
from typing import List
from serialization.option import Option

class Situation(BaseModel):
    title:str
    description:str
    options: List[Option]

    class config:
        orm_mode = True