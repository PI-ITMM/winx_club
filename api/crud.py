from __future__ import annotations
from sqlalchemy import and_
from models import Profile
from schemas import *
from sqlalchemy.orm import Session
from fastapi import HTTPException


def crud_get_profiles(db: Session, **kwargs) -> ListProfiles:
    filters = {k: v for k, v in kwargs.items() if v is not None}
    profiles = db.query(Profile).filter_by(**filters).all()
    return ListProfiles(items=[OutProfile(**profile.__dict__) for profile in profiles])


def crud_get_profile(id: int, db: Session) -> OutProfile | BadResponse:
    db_profile = db.query(Profile).filter(Profile.id == id).first()
    if db_profile is None:
        return BadResponse()
    return OutProfile(**db_profile.__dict__)


def crud_login(username: str, password: str, db: Session) -> GoodResponse | BadResponse | HTTPException:
    profile = db.query(Profile).filter(and_(Profile.name == username, Profile.password == password)).first()
    if profile:
        return GoodResponse()
    else:
        return BadResponse()


def crud_create_profile(profile: InProfile, db: Session) -> GoodResponse:
    db_profile = Profile(**profile.dict())
    db.add(db_profile)
    db.commit()
    db.refresh(db_profile)
    return GoodResponse()


def crud_edit_profile(id: int, profile: EditProfile, db: Session) -> OutProfile | BadResponse:
    db_profile = db.query(Profile).filter(Profile.id == id).first()
    if db_profile is None:
        return BadResponse()
    for k, v in profile.dict().items():
        setattr(db_profile, k, v)
    db.commit()
    new_profile = db.query(Profile).filter(Profile.id == id).first()
    return OutProfile(**new_profile.__dict__)


def crud_delete_profile(id: int, db: Session) -> GoodResponse | BadResponse | HTTPException:
    db_profile = db.query(Profile).filter(Profile.id == id).first()
    if db_profile is None:
        return BadResponse()
    db.delete(db_profile)
    db.commit()
    return GoodResponse()
