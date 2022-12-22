from __future__ import annotations
from sqlalchemy import and_
from models import Profile
from schemas import *
from sqlalchemy.orm import Session
from fastapi import HTTPException


def crud_get_profiles(db: Session, field: str = None, value: str = None) -> ListProfiles:
    if not field or not value:
        profiles = db.query(Profile).all()
    else:
        profiles = db.query(Profile).filter(getattr(Profile, field).contains(value)).all()
    return ListProfiles(items=[OutProfile(**profile.__dict__) for profile in profiles])


def crud_get_profile(id: int, db: Session) -> OutProfile | HTTPException:
    db_profile = db.query(Profile).filter(Profile.id == id).first()
    if db_profile is None:
        raise HTTPException(status_code=404, detail="Profile not found")
    return OutProfile(**db_profile.__dict__)


def crud_login(username: str, password: str, db: Session) -> OutProfile | HTTPException:
    profile = db.query(Profile).filter(and_(Profile.name == username, Profile.password == password)).first()
    if profile:
        return OutProfile(**profile.__dict__)
    else:
        raise HTTPException(status_code=404, detail="Profile not found")


def crud_create_profile(profile: InProfile, db: Session) -> OutProfile:
    db_profile = Profile(**profile.dict())
    db.add(db_profile)
    db.commit()
    db.refresh(db_profile)
    return OutProfile(**db_profile.__dict__)


def crud_edit_profile(id: int, profile: EditProfile, db: Session) -> OutProfile | HTTPException:
    db_profile = db.query(Profile).filter(Profile.id == id).first()
    if db_profile is None:
        raise HTTPException(status_code=404, detail="Profile not found")
    for k, v in profile.dict().items():
        setattr(db_profile, k, v)
    db.commit()
    new_profile = db.query(Profile).filter(Profile.id == id).first()
    return OutProfile(**new_profile.__dict__)


def crud_delete_profile(id: int, db: Session) -> GoodResponse | HTTPException:
    db_profile = db.query(Profile).filter(Profile.id == id).first()
    if db_profile is None:
        raise HTTPException(status_code=404, detail="Profile not found")
    db.delete(db_profile)
    db.commit()
    return GoodResponse()