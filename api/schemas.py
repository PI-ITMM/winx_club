from typing import List
from pydantic import BaseModel, Field


class InProfile(BaseModel):
    name: str
    age: str
    hair_color: str
    eye_color: str
    favorite_book: str
    favorite_music: str
    favorite_quote: str
    favorite_food: str
    favorite_color: str
    hobby: str
    pets: str
    favorite_flowers: str
    zodiac_sign: str
    dream: str
    favorite_season: str
    perfect_date: str
    favorite_actor: str
    favorite_drink: str
    loved_one: str  # имя второй половинки
    contacts: str
    password: str


class OutProfile(BaseModel):
    id: int
    name: str
    age: str
    hair_color: str
    eye_color: str
    favorite_book: str
    favorite_music: str
    favorite_quote: str
    favorite_food: str
    favorite_color: str
    hobby: str
    pets: str
    favorite_flowers: str
    zodiac_sign: str
    dream: str
    favorite_season: str
    perfect_date: str
    favorite_actor: str
    favorite_drink: str
    loved_one: str  # имя второй половинки
    contacts: str

    class Config:
        orm_mode = True


class EditProfile(BaseModel):
    age: str = None
    hair_color: str = None
    eye_color: str = None
    favorite_book: str = None
    favorite_music: str = None
    favorite_quote: str = None
    favorite_food: str = None
    favorite_color: str = None
    hobby: str = None
    pets: str = None
    favorite_flowers: str = None
    zodiac_sign: str = None
    dream: str = None
    favorite_season: str = None
    perfect_date: str = None
    favorite_actor: str = None
    favorite_drink: str = None
    loved_one: str = None  # имя второй половинки
    contacts: str = None
    password: str


class ListProfiles(BaseModel):
    items: List[OutProfile]

    class Config:
        orm_mode = True


class GoodResponse(BaseModel):
    status: int = 200
    response: str = "OK"

