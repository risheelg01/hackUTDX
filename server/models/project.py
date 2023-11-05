from sqlalchemy import ARRAY, Column, Integer, String
from models.models import Base

class Project(Base):
    __tablename__ = "projects"
    id:int = Column(Integer, primary_key=True, index=True)
    name:str = Column(String)
    description:str = Column(String)
    owner_id:int = Column(Integer)
    collaborators:list[int] = Column(ARRAY(Integer))
    tags:list[str] = Column(ARRAY(String))
    skills:list[str] = Column(ARRAY(String))
    status:str = Column(String)
    github:str = Column(String)
    email:str = Column(String)