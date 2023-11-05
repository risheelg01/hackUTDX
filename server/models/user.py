from sqlalchemy import Column, Integer, String, ARRAY
from models.models import Base

class User(Base):
    __tablename__ = "users"
    id: int = Column(Integer, primary_key=True, index=True)
    name: str = Column(String,)
    email: str = Column(String,)
    areas_of_interest: list[str] = Column(ARRAY(String))
    bio: str = Column(String)
    accessToken: str = Column(String)