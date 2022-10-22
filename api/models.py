from sqlalchemy import Column, ForeignKey, Integer, String, Float, LargeBinary
from sqlalchemy.orm import relationship
from database import Base


class Profile(Base):
    __tablename__ = "profile"

    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
