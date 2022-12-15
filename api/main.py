from __future__ import annotations

import uvicorn
from fastapi import Depends, FastAPI
from database import SessionLocal, engine, Base
from crud import *


Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Анкета для друзей",
    version="0.0.1"
)


def get_db():
    db = SessionLocal()
    try:
        return db
    finally:
        db.close()


@app.post("/login/")
def login(username: str, password: str, db: Session = Depends(get_db)):
    return crud_login(username, password, db)


@app.get("/profiles/")
def get_profiles(field: str = None, value: str = None, db: Session = Depends(get_db)):
    return crud_get_profiles(db, field=field, value=value)


@app.get("/profiles/{id}")
def get_profile(id: int, db: Session = Depends(get_db)):
    return crud_get_profile(id, db)


@app.post("/profile/")
def create_profile(profile: InProfile, db: Session = Depends(get_db)):  # создание анкеты = регистрация
    return crud_create_profile(profile, db)


@app.put("/profile/{id}")
def edit_profile(id: int, profile: EditProfile, db: Session = Depends(get_db)):
    return crud_edit_profile(id, profile, db)


@app.delete("/profile/{id}")
def delete_profile(id: int, db: Session = Depends(get_db)):
    return crud_delete_profile(id, db)


if __name__ == '__main__':
    uvicorn.run('main:app', host='127.0.0.1', port=8000)
