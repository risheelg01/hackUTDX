from pydantic import BaseModel
from typing import List
from serialization.effect import Effect

class Option(BaseModel):
    title:str
    effect_on_player: List[Effect]

    class config:
        orm_mode = True