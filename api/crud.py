from __future__ import annotations
from models import Profile
from schemas import *
from sqlalchemy.orm import Session
from fastapi import HTTPException


def crud_get_profiles(db: Session, filters) -> ListProfiles:
    return db.query(Profile).all()
    # TODO: get filters


def crud_get_profile(id: int, db: Session) -> OutProfile:
    return db.query(Profile).filter(Profile.id == id).first()


def crud_login(username: str, password: str, db: Session) -> GoodResponse | HTTPException:
    pass


def crud_signup(username: str, password: str, db: Session) -> GoodResponse | HTTPException:
    pass


def crud_create_profile(profile: InProfile, db: Session) -> OutProfile:
    pass


def crud_edit_profile(id: int, profile: EditProfile, db: Session) -> OutProfile:
    pass


def crud_delete_profile(id: int, db: Session) -> GoodResponse | HTTPException:
    pass
