from pydantic import BaseModel

class User(BaseModel):
    name: str
    email: str
    areas_of_interest: list[str]
    bio: str
    accessToken: str

    class config:
        orm_mode = True