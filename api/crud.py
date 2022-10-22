from models import *
from schemas import *
from sqlalchemy.orm import Session
from fastapi import HTTPException


def crud_get_profiles(db: Session) -> list:
    return db.query(Profile).all()


def crud_get_profile(id: int, db: Session) -> dict:
    return db.query(Profile).filter(Profile.id == id).first()
