from typing import List
from pydantic import BaseModel, Field


class InProfile(BaseModel):
    name: str
    age: int
    hair_color: str
    eye_color: str
    favorite_book: str
    favorite_music: str
    favorite_quote: str
    favorite_food: str
    favorite_color: str
    hobby: str
    pet: str
    favorite_flower: str
    zodiac_sign: str
    dream: str
    favorite_season: str
    perfect_date: str
    favorite_actor: str
    favorite_drink: str
    loved_on: str  # имя второй половинки
    contact: str


class OutProfile(BaseModel):
    id: int
    name: str
    age: int
    hair_color: str
    eye_color: str
    favorite_book: str
    favorite_music: str
    favorite_quote: str
    favorite_food: str
    favorite_color: str
    hobby: str
    pet: str
    favorite_flower: str
    zodiac_sign: str
    dream: str
    favorite_season: str
    perfect_date: str
    favorite_actor: str
    favorite_drink: str
    loved_on: str  # имя второй половинки
    contact: str

    class Config:
        orm_mode = True


class EditProfile(BaseModel):
    age: int = None
    hair_color: str = None
    eye_color: str = None
    favorite_book: str = None
    favorite_music: str = None
    favorite_quote: str = None
    favorite_food: str = None
    favorite_color: str = None
    hobby: str = None
    pet: str = None
    favorite_flower: str = None
    zodiac_sign: str = None
    dream: str = None
    favorite_season: str = None
    perfect_date: str = None
    favorite_actor: str = None
    favorite_drink: str = None
    loved_on: str = None  # имя второй половинки
    contact: str = None


class ListProfiles(BaseModel):
    items: List[OutProfile]

    class Config:
        orm_mode = True


class GoodResponse(BaseModel):
    status: int = 200
    response: str = "OK"


Filters = EditProfile
