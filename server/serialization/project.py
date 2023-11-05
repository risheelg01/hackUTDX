from pydantic import BaseModel

class Project(BaseModel):
    name:str
    description:str
    owner_id:int
    collaborators:list[int]
    tags:list[str]
    skills:list[str]
    status:str
    github:str
    email:str

    class config:
        orm_mode = True