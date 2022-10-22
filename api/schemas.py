from typing import List
from pydantic import BaseModel, Field


class Profile(BaseModel):
    first_name: str
    last_name: str
    age: int
