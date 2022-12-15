from sqlalchemy import Column, ForeignKey, Integer, String, Float, LargeBinary
from sqlalchemy.orm import relationship
from database import Base


class Profile(Base):
    __tablename__ = "profile"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)  # имя и фамилия - уникальное значение
    age = Column(String, nullable=False)
    hair_color = Column(String, nullable=False)
    eye_color = Column(String, nullable=False)
    favorite_book = Column(String, nullable=False)
    favorite_music = Column(String, nullable=False)
    favorite_quote = Column(String, nullable=False)
    favorite_food = Column(String, nullable=False)
    favorite_color = Column(String, nullable=False)
    hobby = Column(String, nullable=False)
    pets = Column(String, nullable=False)
    favorite_flowers = Column(String, nullable=False)
    zodiac_sign = Column(String, nullable=False)
    dream = Column(String, nullable=False)
    favorite_season = Column(String, nullable=False)
    perfect_date = Column(String, nullable=False)
    favorite_actor = Column(String, nullable=False)
    favorite_drink = Column(String, nullable=False)
    loved_one = Column(String, nullable=False)  # имя второй половинки
    contacts = Column(String, nullable=False)
    password = Column(String, nullable=False)

